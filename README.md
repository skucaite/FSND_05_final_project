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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkOGRhMjMzMzIwMDMwYjdmNWRmNTRiIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTUwNzM1MCwiZXhwIjoxNTkxNTE0NTUwLCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicmVhZDpndWlkZXMiLCJyZWFkOnRyYXZlbHMiXX0.GuKAZX5gd0GrxhFHjdaVq4uaoenWmwZUqN_wAnm-ECqJg-kB0lgz0DR_oa1FXAYbWsFNs3F-rXbR3eQCekJtzBC76K6A_c4LRSS1mZ2sixxc7aLwXB2Ai0WgjNuCm2D2YQX7UlGoAv1fRqRLDSKbc9TtPwy6Cv9bLVxdE0IpU5tF-PWhccx3Opw_hY3E63m2carUJnVzK8v4LxZfTVXYpGRpJnaFLX-iEK3Bo4q4Vy1CntHloM8GmGb6gcxZwt8d3cA6jh7v91gFHCfpR35l3hRcAqIrUHUBC1YRqRJV8f9UA-4dDLgQnKkyK8Gs62pdRFyzA_gYOsYAH9J4ianh1A
```

Travel agency admin - can view, create, edit and delete guides and travels.
Travel agency admin Authentication Token:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkYjZhOGNhMTFjN2YwMDFhMTZjZTYzIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTUwNzU1NCwiZXhwIjoxNTkxNTE0NzU0LCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd1aWRlcyIsImNyZWF0ZTp0cmF2ZWxzIiwiZGVsZXRlOmd1aWRlcyIsImRlbGV0ZTp0cmF2ZWxzIiwiZWRpdDpndWlkZXMiLCJlZGl0OnRyYXZlbHMiLCJyZWFkOmd1aWRlcyIsInJlYWQ6dHJhdmVscyJdfQ.gr_YwtLVPxJoHyfElteo0axRAELA1MBQAGPcWG5V5L83lq1bsjeLrvN5zwYtFlYaOIm2PfBZ3VHJ5v8J_H-B2AXzqEz4TYl4WAeXWepRAbvQHvXM8O4rJJJJHM_uHLvRDtrbv6rCNu0OKTnxBUpIgBuhuc14YkvaD5aInGVGEPjLTSF_KIaTVTlhw4W5z88609owlkbtCYAnJZjm6-KD8rB7v76StRu16Vyb7aBVCNYv5vrBQWjzBaI4JQ35L3GWZ59v7vQl2yRbBqdFIP3gmfXc14_gFuvdKntB1rVUne6w8fg8obNdE6zYy-y7rWdd75xqytQCP6Yf7Qmlt8s2pA
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
