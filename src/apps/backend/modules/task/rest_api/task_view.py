from flask import request, jsonify
from flask.views import MethodView

from modules.authentication.rest_api.access_auth_middleware import access_auth_middleware
from modules.task.task_service import TaskService


class TaskView(MethodView):

    @access_auth_middleware
    def post(self, account_id):
        body = request.get_json()
        return jsonify(TaskService.create_task(account_id, body)), 201


    @access_auth_middleware
    def get(self, account_id, task_id=None):
        if task_id:
            task = TaskService.get_task(account_id, task_id)
            return jsonify(task), 200

        return jsonify(TaskService.get_tasks(account_id)), 200


    @access_auth_middleware
    def patch(self, account_id, task_id):
        body = request.get_json()

        updated = TaskService.update_task(account_id, task_id, body)

        if not updated:
            return jsonify({"message": "Task not found"}), 404

        return jsonify(updated), 200


    @access_auth_middleware
    def delete(self, account_id, task_id):
        TaskService.delete_task(account_id, task_id)
        return "", 204


