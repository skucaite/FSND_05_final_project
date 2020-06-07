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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkOGQ0NTEzMzIwMDMwYjdmNWRlNmZkIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTUyOTczNywiZXhwIjoxNTkxNTM2OTM3LCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicmVhZDpndWlkZXMiLCJyZWFkOnRyYXZlbHMiXX0.EAlyT9CEZ7vsAjaf6F7NbK_9wvpUi6XVtlrXH9-vw4iHJltz22gDimvBe6eu0oVf3v1n-SejeOzUMFyD8tt_UzbLyXWLYdEZTIVpIXMG959sxZ-Aob89P20VEFvE4L-QgnyZhYcT-k6OEMrNe5JOidoodZve9ock6S9KzFo_MYY0Yg2afv1r-KTkBDyQM-LAu7nNVetaHyRA3RG8jOJIUw1Iiir2Z2v63p6zuMm7cGRnf5wk3ilBmLjNB_Tm4_LyxR7wxxsJjZUeotqZ3ABrW99PT6WyDzLPRylhfNpJt9j828bV8fjlU2UvliqfsHX0hM3eq7UkUesWTRqFYOrB3g
```

Travel agency admin - can view, create, edit and delete guides and travels.
Travel agency admin Authentication Token:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkYjZhOGNhMTFjN2YwMDFhMTZjZTYzIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTUyOTg5NiwiZXhwIjoxNTkxNTM3MDk2LCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd1aWRlcyIsImNyZWF0ZTp0cmF2ZWxzIiwiZGVsZXRlOmd1aWRlcyIsImRlbGV0ZTp0cmF2ZWxzIiwiZWRpdDpndWlkZXMiLCJlZGl0OnRyYXZlbHMiLCJyZWFkOmd1aWRlcyIsInJlYWQ6dHJhdmVscyJdfQ.IBwTakWHOgmKvM1MMbkasgCuGqZuEUDrhqJ0H8JyyRszJr11DUmsAn91c-SxG5ZyKZ2hkjQJ2i-Xs_mO6A3CRQrG4U8RApeNnHRXi437h_FChF46QlChXYoDv5WWDPxlrD5gnXrIPXKmxyetxbD4JXavDUG-2zmUcuJUq4xUPpgsqda9cO4QAQBiCtMVYK83Dx-5b6jNc6AksMV0Z-wak3YbewcHbSTv4CpVqh11zlOP_S8iMe2jkFTCQZ8ZGWwv3chPMzytS6acAfVX8W1C-KSugy9W5Ftd19dPxuOVuhsndJMtQ2fJ6WQAA0GEN71F4XDwjHu3BmGGvVcNVTic3g
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
