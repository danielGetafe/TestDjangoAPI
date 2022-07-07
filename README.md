# Django Test REST API

> ### Interview technical test. Django Rest API for User sign in and individual profile request

## Installation

1. Clone this repository: `git clone https://github.com/danielGetafe/TestDjangoAPI.git`.
2. `cd` into the project: `cd TestDjangoAPI`.
3. Install Python 3.8.10: `apt install python3 python3-pip`.
4. Install python3-venv: `apt install python3.8-venv`.
5. Create a new virtualenv called `venv`: `python -m venv venv`.
6. Set the local virtualenv to `venv`: `source venv\bin\activate`.
7. Install requirements.txt packages: `pip install -r requirements.txt`

## For production environment

1. Rename settings.py to settings-local.py
2. Rename settings-production.py to settings.py
3. Create SECRET_KEY environment variable: `export SECRET_KEY="django-insecure-u0xhq*ch1u@&p1r2r&=$u07nbyj&@i0tr(u#uzqocqx(nwd+q7"`

## Project description

This REST API developed using Django the the REST Framework has only 2 endpoints, one to sign up new users and another one to display saved user fields details

## API endpoints

```http
GET /profile/<username>
```

Return the user profile data whose username was sent like a parameter
STATUS 404 NOT FOUND will be returned if there is no user with the specified username in the system

Curl example

```bash
curl http://localhost:8000/profile/Daniel
   -H "Accept: application/json"
```

| Parameter  | Type     | Description                   |
| :--------- | :------- | :---------------------------- |
| `username` | `string` | **Required**. Unique username |

```http
POST /user/
```

Inserts a new user in the system. If the user was created successfully, data with all the information will be returned.
STATUS 409 CONFLICT will be returned if there is a conflict with the current data in the system.
STATUS 400 BAD REQUEST will be return if any parameter is missing or not valid.

Curl example

```bash
curl -X POST http://localhost:8000/user
   -H 'Content-Type: application/json'
   -H 'Accept: application/json'
   -d '{"userName":"Daniel","lastName":"Sanchez","emailAddress":"username@example.com","phoneNumber":"+34987506937","hobbies":"Document APIs in README.md files."}'
```

| Parameter      | Type     | Description                                              |
| :------------- | :------- | :------------------------------------------------------- |
| `username`     | `string` | **Required**. Unique username. Minumum 4 characters long |
| `lastName`     | `string` | **Required**. Last name                                  |
| `emailAddress` | `string` | **Required**. Valid full email address                   |
| `phoneNumber`  | `string` | **Required**. Phone number including country prefix      |
| `hobbies`      | `string` | **Optional**. User hobbies description. Empty by default |

## Responses

Both API endpoints return the same JSON representation. The data corresponds to the user that was just created in the POST user operation or the user data requested of the resources created or edited. However, if an invalid request is submitted, or some other error occurs, Gophish returns a JSON response in the following format:

```python
{
  "userName"        : string,
  "lastName"        : string,
  "emailAddress"    : string,
  "phoneNumber"     : string,
  "hobbies"         : string,
  "validatedEmail"  : boolean,
  "validatedNumber" : boolean,
}
```

The `userName` attribute references teh unique username in the system. In case no user with taht username is found, "Not found" status is returned.

The `lastName` attribute is the last name of the user.

The `emailAddress` attribute contains the email address of the user returned.

The `phoneNumber` attribute contains the phone number of the user, which may contain the prefix of the country.

The `hobbies` attribute is a description of the user hobbies. If the parameter not specified in the creation of the user, the field will be empty by default

The `validatedEmail` attribute indicates that the email address of the user was validated if True. Otherwise, it means the user did not validate the email address yet.

The `validatedNumber` attribute indicates that the phone number of the user was already validated if True. Otherwise, it means the user did not validate the phone number yet.

## Status Codes

MobilityApp returns the following status codes API:

| Status Code | Description             |
| :---------- | :---------------------- |
| 200         | `OK`                    |
| 404         | `NOT FOUND`             |
| 400         | `BAD REQUEST`           |
| 409         | `CONFLICT`              |
| 500         | `INTERNAL SERVER ERROR` |
