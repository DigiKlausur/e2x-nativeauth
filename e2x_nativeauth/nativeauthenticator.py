import bcrypt
from nativeauthenticator import NativeAuthenticator
from nativeauthenticator.orm import UserInfo

from .handlers import E2XUsersAPIHandler


class E2XNativeAuthenticator(NativeAuthenticator):
    def get_handlers(self, app):
        handlers = super().get_handlers(app)
        handlers.append((r"/api/e2x_nativeauth/add_user", E2XUsersAPIHandler))
        return handlers

    def admin_create_user(self, username, password):
        """
        Create a new user with the given username and password.
        """
        self.log.info(f"Creating user {username}")
        if self.user_exists(username):
            raise ValueError(f"User {username} already exists")
        encoded_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        infos = {
            "username": username,
            "password": encoded_password,
            "is_authorized": True,
        }

        try:
            user_info = UserInfo(**infos)
        except AssertionError:
            return

        self.db.add(user_info)
        self.db.commit()
        self.log.info(f"User {username} created successfully")
        return user_info
