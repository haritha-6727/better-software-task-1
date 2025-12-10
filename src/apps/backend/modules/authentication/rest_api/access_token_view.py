from dataclasses import asdict

from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from modules.account.account_service import AccountService
from modules.account.types import AccountSearchParams
from modules.authentication.authentication_service import AuthenticationService
from modules.authentication.types import (
    CreateAccessTokenParams,
    EmailBasedAuthAccessTokenRequestParams,
    OTPBasedAuthAccessTokenRequestParams,
    PhoneNumber,
)


class AccessTokenView(MethodView):
    def post(self) -> ResponseReturnValue:
        request_data = request.get_json()
        
        # simple admin login
        if request_data.get("username") == "admin" and request_data.get("password") == "admin":
            token = {"access_token": "TEST_TOKEN"}
            return jsonify(token), 201
        
        return jsonify({"error": "Invalid credentials"}), 401




