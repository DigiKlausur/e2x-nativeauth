from jupyterhub.apihandlers import APIHandler
from nativeauthenticator.handlers import admin_users_scope


class E2XUsersAPIHandler(APIHandler):
    """
    Handler for managing users.
    """
    @admin_users_scope
    async def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        self.authenticator.create_user(username, password)
        user = self.authenticator.get_user(username)
        user.is_authorized = True
        self.authenticator.db.commit()
        self.finish({"status": "success", "message": "User added successfully"})
