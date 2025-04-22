from jupyterhub.apihandlers import APIHandler
from nativeauthenticator.handlers import admin_users_scope


class E2XUsersAPIHandler(APIHandler):
    """
    Handler for managing users.
    """

    @admin_users_scope
    async def post(self):
        data = self.get_json_body()
        if not data:
            self.finish({"status": "error", "message": "No data provided"})
            return
        if "username" not in data or "password" not in data:
            self.finish(
                {"status": "error", "message": "Username and password are required"}
            )
            return
        username = data["username"]
        password = data["password"]
        self.authenticator.admin_create_user(username, password)
        self.finish({"status": "success", "message": "User added successfully"})
