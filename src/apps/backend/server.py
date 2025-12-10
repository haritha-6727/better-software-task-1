from dotenv import load_dotenv
from flask import Flask, jsonify
from flask.typing import ResponseReturnValue
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from bin.blueprints import api_blueprint, img_assets_blueprint, react_blueprint
from modules.account.rest_api.account_rest_api_server import AccountRestApiServer
from modules.authentication.rest_api.authentication_rest_api_server import AuthenticationRestApiServer
from modules.task.rest_api.task_rest_api_server import TaskRestApiServer
from modules.config.config_service import ConfigService
from modules.logger.logger_manager import LoggerManager
from modules.application.errors import AppError

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

LoggerManager.mount_logger()

if ConfigService.has_value("is_server_running_behind_proxy") and \
        ConfigService[bool].get_value("is_server_running_behind_proxy"):
    app.wsgi_app = ProxyFix(app.wsgi_app)


# -----------------------------------
# Register backend under /api
# -----------------------------------

# /api/auth/*
authentication_blueprint = AuthenticationRestApiServer.create()
api_blueprint.register_blueprint(authentication_blueprint, url_prefix="/auth")

# /api/accounts/*
account_blueprint = AccountRestApiServer.create()
api_blueprint.register_blueprint(account_blueprint, url_prefix="/accounts")

# /api/accounts/<id>/tasks
task_blueprint = TaskRestApiServer.create()
api_blueprint.register_blueprint(task_blueprint)


# Mount at root /api
app.register_blueprint(api_blueprint, url_prefix="/api")

# -----------------------------------
# Static
# -----------------------------------
app.register_blueprint(img_assets_blueprint)
app.register_blueprint(react_blueprint)

# -----------------------------------
# Error Handler
# -----------------------------------
@app.errorhandler(AppError)
def handle_error(exc: AppError) -> ResponseReturnValue:
    return jsonify({"message": exc.message, "code": exc.code}), exc.http_code or 500


if __name__ == "__main__":
    app.run(debug=True)
