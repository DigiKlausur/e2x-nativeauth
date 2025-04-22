from jupyterhub.apihandlers import APIHandler
from jupyterhub.utils import maybe_future
from nativeauthenticator.handlers import admin_users_scope
from tornado import web


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
        user = self.user_from_username(username)
        try:
            await maybe_future(self.authenticator.add_user(user))
        except Exception as e:
            self.log.error(f"Failed to create user: {username}", exc_info=True)
            self.users.delete(user)
            raise web.HTTPError(400, f"Failed to create user {username}: {e}")
        self.finish({"status": "success", "message": "User added successfully"})
