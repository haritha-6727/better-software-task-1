from flask import Flask, jsonify
from flask_cors import CORS

from bin.blueprints import api_blueprint, img_assets_blueprint, react_blueprint
from modules.authentication.rest_api.authentication_rest_api_server import AuthenticationRestApiServer
from modules.account.rest_api.account_rest_api_server import AccountRestApiServer
from modules.task.rest_api.task_rest_api_server import TaskRestApiServer
from modules.application.errors import AppError


app = Flask(__name__)
CORS(app, origins="*")


# ---- auth ----
auth_bp = AuthenticationRestApiServer.create()
api_blueprint.register_blueprint(auth_bp, url_prefix="/auth")

# ---- accounts ----
acc_bp = AccountRestApiServer.create()
api_blueprint.register_blueprint(acc_bp, url_prefix="/accounts")

# ---- tasks (with comments) ----
task_bp = TaskRestApiServer.create()
api_blueprint.register_blueprint(task_bp)


# mount
app.register_blueprint(api_blueprint, url_prefix="/api")

# static assets
app.register_blueprint(img_assets_blueprint)
app.register_blueprint(react_blueprint)


@app.errorhandler(AppError)
def handle_error(exc):
    return jsonify({"message": exc.message}), exc.http_code or 500


if __name__ == "__main__":
    app.run(debug=True)
