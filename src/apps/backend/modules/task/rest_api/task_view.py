from typing import Optional

from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from modules.application.common.constants import DEFAULT_PAGINATION_PARAMS
from modules.application.common.types import PaginationParams
from modules.authentication.rest_api.access_auth_middleware import access_auth_middleware
from modules.task.errors import TaskBadRequestError
from modules.task.task_service import TaskService
from modules.task.types import (
    CreateTaskParams,
    DeleteTaskParams,
    GetPaginatedTasksParams,
    GetTaskParams,
    UpdateTaskParams,
)


class TaskView(MethodView):

    @access_auth_middleware
    def post(self, account_id: str) -> ResponseReturnValue:
        request_data = request.get_json()

        create_task_params = CreateTaskParams(
            account_id=account_id,
            title=request_data.get("title"),
            description=request_data.get("description"),
        )

        created_task = TaskService.create_task(params=create_task_params)
        return jsonify(created_task), 201


    @access_auth_middleware
    def get(self, account_id: str, task_id: Optional[str] = None) -> ResponseReturnValue:

        if task_id:
            task = TaskService.get_task(params=GetTaskParams(
                account_id=account_id,
                task_id=task_id
            ))
            return jsonify(task), 200

        pagination_params = PaginationParams(
            page=1, size=20, offset=0
        )

        tasks = TaskService.get_paginated_tasks(
            params=GetPaginatedTasksParams(
                account_id=account_id,
                pagination_params=pagination_params
            )
        )

        return jsonify(tasks), 200


    @access_auth_middleware
    def patch(self, account_id: str, task_id: str) -> ResponseReturnValue:
        request_data = request.get_json()

        updated_task = TaskService.update_task(
            params=UpdateTaskParams(
                account_id=account_id,
                task_id=task_id,
                title=request_data.get("title"),
                description=request_data.get("description"),
            )
        )

        if not updated_task:
            return jsonify({"error": "Task not found"}), 404

        return jsonify(updated_task), 200


    @access_auth_middleware
    def delete(self, account_id: str, task_id: str) -> ResponseReturnValue:

        TaskService.delete_task(
            params=DeleteTaskParams(
                account_id=account_id,
                task_id=task_id
            )
        )

        return jsonify({"deleted": True}), 200

