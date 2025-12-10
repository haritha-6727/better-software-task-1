class AccountService:

    # Simple in-memory dummy users
    users = {
        "admin": {
            "id": "1",
            "username": "admin",
            "password": "admin"
        }
    }

    @staticmethod
    def get_account_by_username(username):
        user = AccountService.users.get(username)
        if not user:
            return None
        return user

    @staticmethod
    def get_account_by_username_and_password(username, password):
        user = AccountService.users.get(username)
        if not user:
            return None
        if user["password"] != password:
            return None
        return user

