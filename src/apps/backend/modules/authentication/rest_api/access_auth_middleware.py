from functools import wraps
from flask import request, jsonify


def access_auth_middleware(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Authorization header missing"}), 401
        
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Invalid token format"}), 401
        
        # just accept ANY token
        token = auth_header.split(" ")[1]

        if token != "TEST_TOKEN":
            return jsonify({"error": "Invalid token"}), 401
        
        return fn(*args, **kwargs)
    return wrapper

