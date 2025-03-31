## Django Authentication API (JWT Authentication)

<p>This is a Django-based authentication API using JSON Web Token (JWT) authentication. It provides secure user authentication, including registration, login, logout, and token refresh functionality.</p>


## Features
* User Registration
* User Login with JWT Authentication
* Logout with Token Blacklisting
* Refresh Token Endpoint
* Retrieve Authenticated User Details

## Technologies Used
* Django
* Django REST Framework (DRF)
* Django REST Framework Simple JWT
* PostgreSQL

## INstallation and setup
1. CLone the Repo:<br/>
`git clone https://github.com/alexander784/Django_Auth.git` <br/>
`cd https://github.com/alexander784/Django_Auth.git`<br/>

2. Create a Virtual Environment
`python3 -m venv venv` <br/>
* Activate the env</br>
 `source venv/bin/activate`
3. Install Dependencies
`pip install -r requirements.txt`<br/>

4. Set Up the Database (Postgres)
 <p>IN your settings file:</p>

 `DATABASES = {`
    `'default': {`
        `'ENGINE': 'django.db.backends.postgresql',`</br>
        `'NAME': 'name',`</br>
        `'PASSWORD':'pass',`</br>
        `'USER':'user',`</br>
        `'HOST':'127.0.0.1',`</br>
        `'PORT':'5432'`
   ` }`
`}`
<p>Run Migrations:</p>

 `python3 manage.py migrate` </br>


 ## API Endpoints
1. User Registration
 Endpoint: `POST /auth/register/`

 `{`
  `"email": "mikeross@user.com",`</br>
  `"name": "Mike Ross",`</br>
  `"password": "@9876"`
`}`

2. User Login </br>
   Endpoint: `POST /auth/login/`</br>
   `{`</br>
     `"email": "user@example.com",`</br>
     `"password": "securepassword"`</br>
`}`</br>
   <p>Response:</p>

  `{`
  `"refresh": "your_refresh_token",`</br>
  `"access": "your_access_token",`</br>
     `"user": {`</br>
   ` "id": 1,`</br>
    `"email": "user@example.com",`</br>
    `"name": "John Doe",`</br>
    `"is_admin": false`</br>
 ` }`</br>
`}`</br>

3.Refresh Access Token</br>
<p>Endpoint: POST /auth/token/refresh/</p>

 `{`</br>
 ` "refresh": "your_refresh_token"`</br>
`}`</br>

<p>Response:</p>

`{`</br>
  `"access": "new_access_token"`</br>
`}`</br>

4. Logout (Blacklist Token) </br>
<p>Endpoint: POST /auth/logout/</p>

`{`
  `"refresh": "your_refresh_token"`
`}`

<p>Response:</p>

`{` </br>
  `"message": "Successfully logged out"` </br>
`}` </br>

5. Get Authenticated User Details
<p>Endpoint: GET /auth/user/
Headers: Authorization: Bearer your_access_token
Response:</p>

`{`</br>
  `"id": 1,`</br>
  `"email": "user@example.com",`</br>
  `"name": "John Doe",`</br>
  `"is_admin": false`</br>
`}`

## Auth and Security
* Uses JWT for authentication.

* The Authorization header should include Bearer <access_token>.

* Refresh tokens are required to generate new access tokens.

* Blacklisting is used to prevent reuse of refresh tokens after logout.


 ## License 
This project is licensed under the MIT License.

## Author
Alexander Nyaga



















 


