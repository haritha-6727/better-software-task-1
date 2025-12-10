from flask import request, jsonify
from flask.views import MethodView


class AccessTokenView(MethodView):
    def post(self):
        body = request.get_json()

        if body.get("username") == "admin" and body.get("password") == "admin":
            return jsonify({"access_token": "TEST_TOKEN"}), 200

        return jsonify({"error": "Invalid credentials"}), 401






