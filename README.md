# Full Stack Nanodegree Final Project

## Background

This project showcases many of the skills I've learned through the Udacity Full Stack Nanodgree curriculum. This entire api has been built from the ground up with no starter code.

## Getting Started

This code is currently deployed on Heroku and accessible at the following URL.
```
https://fsnd-travel-api.herokuapp.com/
```

## Installing Dependencies

### Prepare your environment and app

Start Postgresql
```
    install postgres if needed
    create a database
    save the database, username, and password someplace handy
```

### Clone the repository
```
https://github.com/skucaite/FSND/05_final%20project
```

### Update the models.py Update the database name and configure the database path with username and password if you have one.


## PIP Dependencies

First ensure you are working using your created virtual environment.
Once you have your virtual environment setup and running, install dependencies by running:
```pip install -r requirements.txt```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

To run the server, execute:
```
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
```
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.
Setting the FLASK_APP variable to app.py directs flask to use the app.py file as the application


## Roles and Permissions

There are two roles with different permissions setup for this api:

Travel agency user - can view guides and travels.
Travel agency user Authentication Token:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkOGQ0NTEzMzIwMDMwYjdmNWRlNmZkIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTU5OTE5NywiZXhwIjoxNTkxNjg1NTkxLCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicmVhZDpndWlkZXMiLCJyZWFkOnRyYXZlbHMiXX0.WYSKGhlpTk9h6ymMuitxer0LJlztO7bqim3gZpMOhnfCMvYKIHOIhrLeRZed6Ja2vxb5NcaE3kw7--O-kp2IwB_zQoXO1Q111V1rFVzI11l84r4LuP_j5fkjcNMKtgrStgl6X5WJgKpHSEuRQeZDZuyz_CXMESU3NcIn1W_z3-o5SRT_1xlS-JXWkf8zo2ahdCUJnQc9jrwLho-oC0qmnewamrcnxF6F6dj9kqgP0wACLRBEMRJ4tzEnFuwUIGOVBL3ACOx5LhuDeBXW1TulC0KZqM_VFkF4jztAyBCIFw1QAa0vAFN44_U3ktKi4xILDI8-SZ_Zv1T_H3X8iNr4zQ
```

Travel agency admin - can view, create, edit and delete guides and travels.
Travel agency admin Authentication Token:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkYjZhOGNhMTFjN2YwMDFhMTZjZTYzIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTU5OTY2NCwiZXhwIjoxNTkxNjg2MDU4LCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd1aWRlcyIsImNyZWF0ZTp0cmF2ZWxzIiwiZGVsZXRlOmd1aWRlcyIsImRlbGV0ZTp0cmF2ZWxzIiwiZWRpdDpndWlkZXMiLCJlZGl0OnRyYXZlbHMiLCJyZWFkOmd1aWRlcyIsInJlYWQ6dHJhdmVscyJdfQ.T42RUwacSAOStHeOVgdIQ5u9q3ntZsvr4pihSyZBJ1hn305ly0Utci3weENcch623mZhU9rT1n1uCVngCLfNnoGhZuXaIjDRRFHuboHxsPuUoaZweeWNSzcgrrB05HSaP7P6RDiijhLhhL3mgTOrWT_vw7nHG__XGS3czbGpy54_1cXvyOtKoS36HK0lvI8WKYyLkF9vkrMbMTpTAawYePTAAQ_cp6LIx8ScOsf-P_ijyUWadC-SXS_WNUt8kBPjpDKddrrA-ppqmjSP0KpM_LjmySj_qhVVSpg8ZQe_LR2K6_kWrjudH4msd2NTZHiEx9TCsmJHxmo9JQczcfffIQ
```

## Resource endpoint library

Endpoints
- GET '/travels'
- GET '/guides'
- POST '/travels'
- POST '/guides'
- PATCH '/travels/id'
- PATCH '/guides/id'
- DELETE '/travels/id'
- DELETE '/guides/id'


*** GET '/travels'
  - Fetches a list of all travels.
  - Returns travels list and success value.
```
    {
      "success": true,
      "travels": [
        {
          "content": "A lot of sightseeings",
          "guide_id": 1,
          "guide_name": "John",
          "id": 1,
          "title": "Visit London"
        },
        {
          "content": "A lot of sightseeings",
          "guide_id": 1,
          "guide_name": "John",
          "id": 2,
          "title": "Visit London"
        }]}
```
*** GET '/guides'
  - Fetches a list of all guides.
  - Returns guides list and success value.
```
    {
      "guides": [
        {
          "id": 2,
          "name": "Tom",
          "phone": "84579623",
          "surname": "Johnson"
        },
        {
          "id": 1,
          "name": "John",
          "phone": "85475123",
          "surname": "Newman"
        }
      ],
      "success": true
    }
```
*** POST '/travels'
  - Creates new travel with given content, title and guide_id.
  - Returns created travel id, travels list and success value.
```
    {
      "created": 1,
      "success": true,
      "travels": [
        {
          "content": "A lot of sightseeings",
          "guide_id": 1,
          "guide_name": "John",
          "id": 1,
          "title": "Visit London"
        }]}
```
*** POST '/guides'
  - Creates new guide with given name, surname and phone.
  - Returns created guide id, guides list and success value.
```
    {
      "created": 1,
      "success": true,
      "guides": [
        {
          "id": 1,
          "name": "John",
          "phone": "85475123",
          "surname": "Newman"
        }]}
```
*** PATCH '/travels/id'
  - Updates a travel by given id.
  - Returns updated data for the travel and success value.
```
    {
      "success": true,
      "travels": {
        "content": "See a lot of New York sightseeings",
        "guide_id": 2,
        "guide_name": "Tom",
        "id": 3,
        "title": "Visit New York"
      }
    }
```
*** PATCH '/guides/id'
  - Updates a guide by given id.
  - Returns updated data for the guide and success value.
```
    {
      "guides": {
        "id": 1,
        "name": "John",
        "phone": "85475123",
        "surname": "Newman"
      },
      "success": true
    }
```
*** DELETE '/travels/id'
  - Deletes travel by given id.
```
  - Returns deleted id and success value.
    {
      "deleted": "2",
      "success": true
    }
```
*** DELETE '/guides/id'
  - Deletes guide by given id.
  - Returns deleted id and success value.
```
        {
          "deleted": "3",
          "success": true
            }
```
# Errors Handled
Errors that will be handled are:
- 400 - Bad request
- 401 - Unauthorized
- 403 - Forbidden
- 404 - Resource not found
- 422 - Unprocessable

Errors will include a success value, message, and error value.

Example error response:
```
{
  "error": 401,
  "message": "authorization_header_missing",
  "success": false
}
```
