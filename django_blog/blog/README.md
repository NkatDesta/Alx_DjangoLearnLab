#(1)
Django Blog Authentication System
Overview
This project is a Django blog application with a user authentication system. It includes:
- User registration
- Login & logout
- Profile management (view & edit email)
- CSRF protection on all forms
- Styled login & registration pages using static files

Features
1. **User Registration**
   - Located at `/register`
   - Extends Django's `UserCreationForm` with an email field
   - Automatically logs in users after successful registration

2. **Login & Logout**
   - Login: `/login`
   - Logout: `/logout`
   - Uses Django's built-in authentication views

3. **Profile Management**
   - Profile page: `/profile` (only for logged-in users)
   - Allows updating email address
   - POST request updates are saved securely

4. **Security**
   - All forms include `{% csrf_token %}`
   - Passwords are hashed using Django’s built-in algorithms
   - Profile route protected with `@login_required`

Static Files
- Located in `blog/static/blog/`
- Styles applied to login and registration forms

How to Test
1. Run the development server
2. Visit /register and create a new account
3. Log out and log in again via /login
4. Visit /profile to view and update your email


#(2)
## Blog Post Management (CRUD)
### Features
- List all blog posts (`/posts/`) — public
- View post details (`/posts/<id>/`) — public
- Create a post (`/posts/new/`) — requires login
- Edit a post (`/posts/<id>/edit/`) — only the author
- Delete a post (`/posts/<id>/delete/`) — only the author

### Permissions
- Authenticated users can create posts.
- Only authors can edit or delete their own posts.
- All posts are visible to everyone.

### Testing
1. Login and create a new post.
2. View the post list and click into details.
3. Edit and delete posts you own.
4. Verify you cannot edit/delete others’ posts.


#(3)
Comment Functionality
- Add a Comment: Authenticated users can type in the comment form below a blog post and submit it. New comments are immediately displayed under the post.
- Edit a Comment: Only the author of a comment sees the “Edit” link. Clicking it allows the author to modify the content of their comment.
- Delete a Comment: Only the author of a comment sees the “Delete” link. Clicking it removes the comment from the post.
- Permissions: Users cannot edit or delete comments authored by other users, ensuring comment ownership and privacy.
- Display Order: Comments are displayed in chronological order (oldest first) under each blog post, providing a clear discussion thread.


#(4)
Tagging Functionality
- Adding tags to a post: Use the tags field in the post form; separate multiple tags with commas.
- Searching posts: Use the search bar; it searches titles, content, and tags.
- Viewing posts by tag: Click a tag in any post to view all posts with that tag.