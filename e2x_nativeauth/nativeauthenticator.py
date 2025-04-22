from nativeauthenticator import NativeAuthenticator

from .handlers import E2XUsersAPIHandler


class E2XNativeAuthenticator(NativeAuthenticator):

    def get_handlers(self, app):
        handlers = super().get_handlers(app)
        handlers.append((r"/api/e2x_nativeauth/add_user", E2XUsersAPIHandler))
        return handlers