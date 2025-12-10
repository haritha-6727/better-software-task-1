# SIMPLE IN-MEMORY STORAGE FOR DEMO USE
class TaskService:

    tasks = {}
    next_id = 1

    @staticmethod
    def create_task(*, params):
        task = {
            "id": TaskService.next_id,
            "account_id": params.account_id,
            "title": params.title,
            "description": params.description,
        }
        TaskService.tasks[TaskService.next_id] = task
        TaskService.next_id += 1
        return task

    @staticmethod
    def get_task(*, params):
        return TaskService.tasks.get(int(params.task_id))

    @staticmethod
    def get_paginated_tasks(*, params):
        return list(TaskService.tasks.values())

    @staticmethod
    def update_task(*, params):
        task = TaskService.tasks.get(int(params.task_id))
        if not task:
            return None
        
        task["title"] = params.title
        task["description"] = params.description
        return task

    @staticmethod
    def delete_task(*, params):
        TaskService.tasks.pop(int(params.task_id), None)
        return {"deleted": True}



