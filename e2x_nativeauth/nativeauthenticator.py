from nativeauthenticator import NativeAuthenticator

from .handlers import E2XUsersHandler


class E2XNativeAuthenticator(NativeAuthenticator):

    def get_handlers(self, app):
        handlers = super().get_handlers(app)
        handlers.append((r"/e2x_nativeauth/add_user", E2XUsersHandler))
        return handlers