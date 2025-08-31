# Social Media API — API Overview

A Django REST Framework–based social media backend where users can:

- Register/Login
- Create posts (with media support - optional)
- Like/Unlike posts
- Comment on posts
- Follow/Unfollow users
- Receive real-time notifications (likes, comments, follows)
- View a personalized feed of posts from followed users (with pagination)

Features

- Authentication
- Custom User Model with follow/unfollow system
- Posts with likes & comments
- Notifications for interactions (likes, comments, follows)
- Feeds showing posts from followed users in reverse chronological order
- Pagination enabled for feed & post lists
---

##  Tech Stack

* Python 3.10+
* Django 5.x
* Django REST Framework
* PostgreSQL
* DRF Token Auth (`rest_framework.authtoken`)

---
##  Setup Instructions

# Clone repo

git clone https://github.com/Robertngatia25/Social_media_api.git
cd social_media_api

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Run server
python manage.py runserver

## 2 Backend Endpoints (MVP)

Base path: `http://127.0.0.1:8000/`

* `POST /api/accounts/register/` – create user, returns token + user
* `POST /api/accounts/login/` – login, returns token + user
* `GET  /api/accounts/profile/` – get current user (Auth required)
* `PUT  /api/accounts/profile/` – update profile (Auth required)
* `PATCH /api/accounts/profile/` – partial update (Auth required)
* `POST /api/posts/` – create post (Auth required)
* `GET /api/posts/` – list posts
* `GET /api/posts/<int:pk>/` – retrieve post
* `PUT /api/posts/<int:pk>/` – update post (Auth required)
* `PATCH /api/posts/<int:pk>/` – partial update post (Auth required)
* `DELETE /api/posts/<int:pk>/` – delete post (Auth required)
* `POST /api/posts/<int:pk>/like/` – like post (Auth required)
* `DELETE /api/posts/<int:pk>/like/` – unlike post (Auth required)
* `POST /api/posts/<int:pk>/comment/` – comment on post (Auth required)
* `POST /api/accounts/<int:pk>/follow/` – follow user (Auth required)
* `DELETE /api/accounts/<int:pk>/follow/` – unfollow user (Auth required)
* `GET /api/posts/feeds/` - Get personalized feeds
* `GET /api/notifications/` - Get notifications
* 
---

**Auth header**

```
Authorization: Token <your_token_here>
```

## 3) Example Requests (for Postman or VS Code Postman extension)

We will use three test users:

James → Jamesstrong!230
Mary → 2025Mary!
Michael → 2025Mary!

1. Register Users

POST /api/accounts/register/
Content-Type: application/json
```json
{
  "username": "James",
  "email": "james@example.com",
  "password": "Jamesstrong!230",
  "bio": "Backend engineer who loves Django",
  "profile_picture": null
}

```

```json
{
  "username": "Mary",
  "email": "mary@example.com",
  "password": "2025Mary!",
  "bio": "Frontend designer passionate about UI/UX",
  "profile_picture": null
}
```
```json
{
  "username": "Michael",
  "email": "michael@example.com",
  "password": "2025Mary!",
  "bio": "Fullstack developer who enjoys Python & React",
  "profile_picture": null
}

```
Login Users

POST /api/accounts/login/
Content-Type: application/json
```json
{
  "username": "james",
  "password": "Jamesstrong!230"
}
```
```json
{
  "username": "mary",
  "password": "2025Mary!"
}
```
```json
{
  "username": "michael",
  "password": "2025Mary!"
}
```
**Expected 200**

```json
{
  "token": "<token>",
  "user": {
    "id": 1,
    "username": "james",
    "email": "james@example.com",
    "bio": "Backend engineer who loves Django",
    "profile_picture": null,
  }
}

{
  "token": "<token>",
  "user": {
    "id": 2,
    "username": "mary",
    "email": "mary@example.com",
  }
}

{
  "token": "<token>",
  "user": {
    "id": 3,
    "username": "michael",
    "email": "michael@example.com",
  }
}
```
Posts
Create Post

POST /api/posts/
Headers: Authorization: Bearer <access_token>
Content-Type: application/json

```json
{
  "title": "My First Post",
  "content": "This is my first post on the platform!",
  "media": null
}
```

*** List All Posts

GET /api/posts/

Retrieve Single Post
GET /api/posts/1/

Update Post (Author Only)

PUT /api/posts/1/
Headers: 
Authorization: Token <token>
```json
{
  "title": "My Updated Post",
  "content": "I just edited my post.",
  "media": null
}
```
Delete Post (Author Only)

DELETE /api/posts/1/
Headers:
Authorization: Token <token>


*** Likes
Toggle Like / Unlike a Post

POST /api/posts/1/like/
Headers: Authorization: Bearer <access_token>

*** Comments
Create Comment

POST /api/posts/1/comment/
Headers: Authorization: Bearer <access_token>
Content-Type: application/json
```json
{
  "content": "Great post!"
}
```
*** Follow/Unfollow

POST /api/accounts/1/follow/
Headers: Authorization: Bearer <access_token>

Get Notifications for Current User

GET /api/notifications/
Headers: Authorization: Bearer <access_token>

Get Personalized Feed

GET /api/posts/feeds/
Headers: Authorization: Bearer <access_token>




ANOTHER EXAMPLE TO USE FOR ONLY REGISTER AND LOGIN PURPOSES 

### Example — Register Bob

http
POST /api/accounts/register/
Content-Type: application/json

```json
{
  "username": "Bob",
  "email": "bob@example.com",
  "password": "BobStrong#2025!",
  "bio": "I love coding for fun",
  "profile_picture": null
}
```

**Expected 201**

```json
{
  "token": "<token>",
  "user": {
    "id": 1,
    "username": "Bob",
    "email": "bob@example.com",
    "bio": "I love coding for fun",
    "profile_picture": null,
  }
}
```

### Example B — Login Bob

http
POST /api/accounts/login/
Content-Type: application/json
Authorization: Token <token>
```json
{
  "username": "bob",
  "password": "BobStrong#2025!"
}
```

**Expected 200**

```json
{
  "token": "<token>",
  "user": {
    "id": 1,
    "username": "bob",
    "email": "bob@example.com",
    "bio": "I love coding for fun",
  }
}
```

### — Get Bob Profile

http
GET /api/accounts/profile/
Authorization: Token <token>


**Expected 200** – user object

### Example D — Update Bob Profile

http
PATCH /api/accounts/profile/
Authorization: Token <token>
Content-Type: application/json
```json
{
  "bio": "Updated bio from README"
}

```
## 4) Testing Tips (VS Code Postman Extension)

1. Install the **Postman** extension in VS Code.
2. Create a **New Request** → set method & URL.
3. Add header: `Content-Type: application/json`.
4. Paste one of the JSON bodies above and **Send**.
5. Copy the `token` from the response and use it as `Authorization: Token <token>` for the protected endpoints.

## 5) Troubleshooting

* `400 Bad Request`: missing/duplicate username/email, or bad JSON.
* `401 Unauthorized`: missing/invalid `Authorization` header for `/profile`.
* `415 Unsupported Media Type`: set header `Content-Type: application/json`.

```