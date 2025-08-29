# Social Media API — MVP Authentication

This repo contains a Django + DRF backend with a **custom user model** and **token authentication**. Use this README to run the project locally and test `/register`, `/login`, and `/profile`.

## Tech Stack

* Python 3.10+
* Django 5.x
* Django REST Framework
* PostgreSQL
* DRF Token Auth (`rest_framework.authtoken`)

---


## 2) Endpoints (MVP)

Base path: `http://127.0.0.1:8000/`

* `POST /api/accounts/register/` – create user, returns token + user
* `POST /api/accounts/login/` – login, returns token + user
* `GET  /api/accounts/profile/` – get current user (Auth required)
* `PUT  /api/accounts/profile/` – update profile (Auth required)
* `PATCH /api/accounts/profile/` – partial update (Auth required)

**Auth header**

```
Authorization: Token <your_token_here>
```

---

## 3) Example Requests (for Postman or VS Code Postman extension)

### Example A — Register Bob

```http
POST /api/accounts/register/
Content-Type: application/json

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
    "following": []
  }
}
```

### Example B — Login Alice

```http
POST /api/accounts/login/
Content-Type: application/json

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
    "username": "alice",
    "email": "alice@example.com",
    "bio": "I love coding for fun",
    "profile_picture": null,
    "following": []
  }
}
```

### Example C — Get Alice Profile

```http
GET /api/accounts/profile/
Authorization: Token <token>
```

**Expected 200** – user object

### Example D — Update Alice Profile

```http
PATCH /api/accounts/profile/
Authorization: Token <token>
Content-Type: application/json

{
  "bio": "Updated bio from README"
}
```

---

## 4) Testing Tips (VS Code Postman Extension)

1. Install the **Postman** extension in VS Code.
2. Create a **New Request** → set method & URL.
3. Add header: `Content-Type: application/json`.
4. Paste one of the JSON bodies above and **Send**.
5. Copy the `token` from the response and use it as `Authorization: Token <token>` for the protected endpoints.

---

## 5) Troubleshooting

* `400 Bad Request`: missing/duplicate username/email, or bad JSON.
* `401 Unauthorized`: missing/invalid `Authorization` header for `/profile`.
* `415 Unsupported Media Type`: set header `Content-Type: application/json`.
* For image uploads later: use `multipart/form-data` in Postman and include `profile_picture` file; not required for MVP.

---

## 6) Commit Checklist (MVP Auth)

* [x] Project & `accounts` app scaffolded
* [x] CustomUser model + migrations
* [x] Serializers (Register, Login, User)
* [x] Views + URLs for register/login/profile
* [x] README with testing examples
