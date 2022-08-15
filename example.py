import requests

BASE_URL = "http://localhost:8090{path}"

# SignUp
print("-" * 20, "SIGNUP", "-" * 20)
resp = requests.post(
    BASE_URL.format(path="/auth/signup"),
    json={
        "username": "string",
        "password": "string",
        "name": "string",
        "city": "string",
        "occupation": "string"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)

# LogIn
print("-" * 20, "LOGIN", "-" * 20)
resp = requests.post(
    BASE_URL.format(path="/auth/login"),
    json={
        "username": "string",
        "password": "string"
    }
)

access_token = resp.json()["access_token"]
refresh_token = resp.json()["refresh_token"]

print(resp.status_code, resp.json())
print("-" * 50)

# GetUserdata
print("-" * 20, "USER_DATA", "-" * 20)
resp = requests.get(
    BASE_URL.format(path="/data/user"),
    headers={
        "Authorization": f"Bearer {access_token}"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)

# RevokeToken
print("-" * 20, "REVOKE_ACCESS", "-" * 20)
resp = requests.delete(
    BASE_URL.format(path="/auth/access-revoke"),
    headers={
        "Authorization": f"Bearer {access_token}"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)

# GetUserdata
print("-" * 20, "USER_DATA", "-" * 20)
resp = requests.get(
    BASE_URL.format(path="/data/user"),
    headers={
        "Authorization": f"Bearer {access_token}"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)

# RefreshToken
print("-" * 20, "REFRESH ACCESS", "-" * 20)
resp = requests.post(
    BASE_URL.format(path="/auth/refresh"),
    headers={
        "Authorization": f"Bearer {refresh_token}"
    }
)
access_token = resp.json()["access_token"]
refresh_token = resp.json()["refresh_token"]

print(resp.status_code, resp.json())
print("-" * 50)

# GetUserdata
print("-" * 20, "USER_DATA", "-" * 20)
resp = requests.get(
    BASE_URL.format(path="/data/user"),
    headers={
        "Authorization": f"Bearer {access_token}"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)

# RevokeTokens
print("-" * 20, "REVOKE_ACCESS", "-" * 20)
resp = requests.delete(
    BASE_URL.format(path="/auth/access-revoke"),
    headers={
        "Authorization": f"Bearer {access_token}"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)

# RevokeRefresh
print("-" * 20, "REVOKE_REFRESH", "-" * 20)
resp = requests.delete(
    BASE_URL.format(path="/auth/refresh-revoke"),
    headers={
        "Authorization": f"Bearer {refresh_token}"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)

# RefreshToken
print("-" * 20, "REFRESH_ACCESS", "-" * 20)
resp = requests.post(
    BASE_URL.format(path="/auth/refresh"),
    headers={
        "Authorization": f"Bearer {refresh_token}"
    }
)

print(resp.status_code, resp.json())
print("-" * 50)
