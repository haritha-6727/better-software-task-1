from typing import List, Dict

from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from modules.authentication.rest_api.access_auth_middleware import access_auth_middleware


class CommentView(MethodView):
    """
    Simple in-memory comments CRUD for a given task.
    comments = [
      {"id": 1, "task_id": "1", "text": "Nice task"}
    ]
    """

    comments: List[Dict] = []
    next_id: int = 1

    @access_auth_middleware
    def post(self, account_id: str, task_id: str) -> ResponseReturnValue:
        data = request.get_json() or {}
        text = data.get("text")

        if not text:
            return jsonify({"error": "text is required"}), 400

        comment = {
            "id": CommentView.next_id,
            "task_id": task_id,
            "account_id": account_id,
            "text": text,
        }
        CommentView.comments.append(comment)
        CommentView.next_id += 1

        return jsonify(comment), 201

    @access_auth_middleware
    def get(self, account_id: str, task_id: str) -> ResponseReturnValue:
        task_comments = [
            c for c in CommentView.comments
            if c["task_id"] == str(task_id) and c["account_id"] == str(account_id)
        ]
        return jsonify(task_comments), 200

    @access_auth_middleware
    def patch(self, comment_id: str) -> ResponseReturnValue:
        data = request.get_json() or {}
        new_text = data.get("text")

        for c in CommentView.comments:
            if str(c["id"]) == str(comment_id):
                if new_text:
                    c["text"] = new_text
                return jsonify(c), 200

        return jsonify({"error": "Comment not found"}), 404

    @access_auth_middleware
    def delete(self, comment_id: str) -> ResponseReturnValue:
        before = len(CommentView.comments)
        CommentView.comments = [
            c for c in CommentView.comments if str(c["id"]) != str(comment_id)
        ]
        after = len(CommentView.comments)

        if after == before:
            return jsonify({"error": "Comment not found"}), 404

        return jsonify({"deleted": True}), 200
