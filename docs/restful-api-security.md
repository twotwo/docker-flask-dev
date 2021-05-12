# RESTful API - Security

## Users

Users Management.

|URI |GET |POST |PUT |DELETE |
|--|--|--|--|--|
|`/users` |Returns list of users.|Create a new user.|`N/A` |`N/A` |
|`/users/{userId}` |Returns a specific user.|`N/A` |Updates a user's Info. |Delete an existing user.|
|`/users?username={username}` |Returns user info by name. |`N/A` |`N/A` |`N/A` |

Implements

- `app/view/users.py`
- `tests/test_users.py`
- `app/repo/user.py`
- `app/domain/user.py`

## Sessions

Authentication with Session.

|URI |GET |POST |PUT |DELETE |
|--|--|--|--|--|
|`/sessions` |`N/A`|Login.|`N/A` |`N/A` |
|`/sessions/{sessionId}` |Returns specific session Info.|`N/A` |Updates session Info. |Logout.|

Implements

- `app/view/sessions.py`
- `tests/test_sessions.py`
- `app/repo/session.py`
- `app/domain/session.py`
