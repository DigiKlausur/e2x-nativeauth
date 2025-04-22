from jupyterhub.handlers import BaseHandler
from nativeauthenticator.handlers import admin_users_scope


class E2XUsersHandler(BaseHandler):
    """
    Handler for managing users.
    """
    @admin_users_scope
    async def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        self.create_user(username, password)
        user = self.get_user(username)
        user.is_authorized = True
        self.db.commit()
        self.finish({"status": "success", "message": "User added successfully"})
