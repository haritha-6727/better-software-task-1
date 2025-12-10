class AuthenticationService:

    @staticmethod
    def create_access_token_by_username_and_password(**kwargs):
        return {"access_token": "TEST-TOKEN"}

    @staticmethod
    def verify_access_token(token):
        return {"account_id": 1}



