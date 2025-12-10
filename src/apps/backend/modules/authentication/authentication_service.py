import urllib.parse
from dataclasses import asdict

from modules.account.types import Account, PhoneNumber
from modules.authentication.types import (
    OTP,
    AccessTokenPayload,
    CreateOTPParams,
    OTPBasedAuthAccessTokenRequestParams,
    PasswordResetToken,
    VerifyOTPParams,
)


class FakePayload:
    def __init__(self):
        self.account_id = "1"

class AuthenticationService:

    @staticmethod
    def create_access_token_by_username_and_password(*, account):
        return {"access_token": "DEMO_TOKEN"}

    @staticmethod
    def verify_access_token(*, token: str):
        return FakePayload()


