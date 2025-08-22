# Social Media API

## 0. Setup

pip install django djangorestframework djangorestframework-simplejwt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver




# Posts & Comments API

## 1. Endpoints

### Posts
- `GET /api/posts/` → List posts (paginated, searchable by `title` or `content`)
- `POST /api/posts/` → Create post (requires Token in header)
- `GET /api/posts/{id}/` → Retrieve single post with comments
- `PUT /api/posts/{id}/` → Update post (author only)
- `DELETE /api/posts/{id}/` → Delete post (author only)

### Comments
- `GET /api/comments/` → List comments
- `POST /api/comments/` → Add comment to a post
- `PUT /api/comments/{id}/` → Update comment (author only)
- `DELETE /api/comments/{id}/` → Delete comment (author only)

## Example Request
```http
POST /api/posts/
Authorization: Token <your_token>
{
  "title": "My First Post",
  "content": "Excited to join this platform!"
}





# Follows & Feed

## 2. Endpoints

### Follow Management
- `POST /api/accounts/follow/{user_id}/` → Follow a user
- `POST /api/accounts/unfollow/{user_id}/` → Unfollow a user

### Feed
- `GET /api/feed/` → Returns posts from users you follow, newest first.

## Example
```http
POST /api/accounts/follow/2/
Authorization: Token <your_token>
Response: { "detail": "You are now following johndoe." }






# Like and Notifications
## 3. Likes & Notifications Functionality

### Like a Post

Endpoint:  
- POST /api/posts/<post_id>/like/
Authentication:  
- Required (JWT or session-based)
Request:
- No body required. Just the URL with `<post_id>`.
Response (Success):  
{
  "detail": "Post liked."
}
Response (Error, already liked):
{
  "detail": "You already liked this post."
}
Notes:
- Automatically generates a notification for the post author.
- Users cannot like their own post more than once.

### Unlike a Post
Endpoint:
POST /api/posts/<post_id>/unlike/
Authentication:
- Required
Request:
- No body required. Just the URL with <post_id>.
Response (Success):
{
  "detail": "Post unliked."
}
Response (Error, not liked yet):
{
  "detail": "You have not liked this post."
}
### List Notifications
Endpoint:
- GET /api/notifications/
Authentication:
- Required
Response (Success):
[
  {
    "id": 1,
    "actor_username": "john_doe",
    "verb": "liked",
    "target_str": "My First Post",
    "is_read": false,
    "timestamp": "2025-08-22T15:30:00Z"
  },
  {
    "id": 2,
    "actor_username": "jane_smith",
    "verb": "commented",
    "target_str": "My First Post",
    "is_read": false,
    "timestamp": "2025-08-22T16:10:00Z"
  }
]
### Notes:
- Notifications are sorted by timestamp (latest first).
- is_read indicates whether the user has read the notification.
- Users only see their own notifications.

### Notification Creation Rules:
- Liking someone else’s post → creates a notification.
- Commenting on someone else’s post → creates a notification.
- Following another user → can also generate a notification (if implemented).
- Users do not receive notifications for their own actions.

### Benefits
- Engages users by notifying them of interactions.
- Encourages interaction (likes/comments).
- Helps users track activity related to their content.



# 4. Deployment Overview
##deploying
- The social_media_api Django project is now production-ready. The project has been configured to use environment variables for sensitive data, secure settings for HTTPS, and static file management with Whitenoise.
##Environment Variables
- All sensitive data and environment-specific settings are stored in a .env file.
## Database Configuration
- Local: SQLite database (db.sqlite3) is used.
- Production: Configured to use DATABASE_URL (PostgreSQL, MySQL, or any supported database).
## Static & Media Files
- Static files are served using Whitenoise in production.
- Run the command to collect static files.
- Media files (user uploads) are stored in MEDIA_ROOT.
##Deployment Process
- Push code to GitHub repository.
- Prepare server environment:
- Install Python, pip, virtualenv.
- Install required packages from requirements.txt:
- pip install -r requirements.txt
- Configure .env with production variables.
- Run database migrations:
- python manage.py migrate
- Collect static files:
- python manage.py collectstatic
- Start the web server (example with Gunicorn):
- gunicorn social_media_api.wsgi:application --bind 0.0.0.0:8000
- (Optional) Set up Nginx as reverse proxy and configure HTTPS if deploying on a public server.

## Testing in Production
- Test the following after deployment:
- Access API endpoints via the deployed URL.
- Test user registration, login, and authentication.
- Test posts, likes, and notifications functionality.
- Ensure static files and media files load correctly.
- Verify HTTPS and security headers (XSS, CSRF, etc.) are applied.

## Maintenance Plan
- Monitor server logs for errors.
- Schedule regular database backups.
- Update Django and Python dependencies periodically.
- Check that environment variables are secure and not exposed.