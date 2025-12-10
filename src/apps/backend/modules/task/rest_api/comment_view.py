from typing import List, Dict

from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from modules.authentication.rest_api.access_auth_middleware import access_auth_middleware


class CommentView(MethodView):

    # simple in-memory comments per task
    comments: List[Dict] = []
    next_id = 1

    @access_auth_middleware
    def post(self, account_id: str, task_id: str) -> ResponseReturnValue:
        request_data = request.get_json()

        comment = {
            "id": CommentView.next_id,
            "task_id": task_id,
            "text": request_data.get("text")
        }
        CommentView.comments.append(comment)
        CommentView.next_id += 1

        return jsonify(comment), 201

    @access_auth_middleware
    def get(self, account_id: str, task_id: str) -> ResponseReturnValue:
        task_comments = [c for c in CommentView.comments if c["task_id"] == task_id]
        return jsonify(task_comments), 200

    @access_auth_middleware
    def delete(self, account_id: str, task_id: str, comment_id: str) -> ResponseReturnValue:
        CommentView.comments = [
            c for c in CommentView.comments
            if c["id"] != int(comment_id)
        ]
        return jsonify({"deleted": True}), 200
