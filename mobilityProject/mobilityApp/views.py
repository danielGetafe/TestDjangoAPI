from django.db import IntegrityError
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site

from .validationManager import sendValidationEmail, sendValidationSMS
from .. import settings
from .models import CabUser
from .serializers import UserSerializer


# Create your views here.

@api_view(['GET'])
def getUser(request, username=None):
    """ Gets the user passed like a parameter

    returns the JSON object with the user data
    return status 400 if the username parameter is empty
    return status 404 if no user with that username was found"""

    if username == '':
        return Response(data={'detail':'username parameter cannnot be empty'}, status=status.HTTP_400_BAD_REQUEST)

    user_profile = CabUser.objects.filter(userName=username)
    
    if not user_profile.exists():
        return Response(data={'detail':'User not found'}, status=status.HTTP_404_NOT_FOUND)

    else:
        serializer = UserSerializer(user_profile.first())
        return Response(serializer.data)


@api_view(['POST'])
def createUser(request):
    """ Creates a new user in the system and send validation
    email and SMS
    
    returns JSON object if the user was created successfully
    returns status 409 if a conflict exists with the current data
    returns status 400 if parameters are missing or not valid"""

    if len(request.data['userName']) < 4:
        return Response(data={'detail':'userName must have, at least, 4 chracters'},
        status=status.HTTP_400_BAD_REQUEST)
    
    if request.data['lastName'] == '':
        return Response(data={'detail':'lastName cannot be empty'},
        status=status.HTTP_400_BAD_REQUEST)

    if not request.data['phoneNumber'].startswith('+'):
        return Response(data={'detail':'phoneNumber must have country prefix'},
        status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(): 

        try:
            serializer.save()
        except IntegrityError as e: 
            return Response(data={'detail':'Conflict in data introduced: ' + str(e.__cause__)},
            status=status.HTTP_409_CONFLICT)

        if not settings.DEBUG: # Send validation email and SMS only from production env
            siteDomain = get_current_site(request).domain
            sendValidationEmail(siteDomain, request.data['userName'],
            request.data['emailAddress'])
            sendValidationSMS(siteDomain, request.data['userName'],
            request.data['phoneNumber'])

        return Response(serializer.data)
    
    else:
        return Response(data={'detail':'Parameters missing or not valid'}, status=status.HTTP_400_BAD_REQUEST)
