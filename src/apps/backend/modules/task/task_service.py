class TaskService:

    tasks = {}
    next_id = 1

    @staticmethod
    def create_task(account_id, body):
        task = {
            "id": TaskService.next_id,
            "account_id": account_id,
            "title": body["title"],
            "description": body["description"],
        }
        TaskService.tasks[TaskService.next_id] = task
        TaskService.next_id += 1
        return task


    @staticmethod
    def get_task(account_id, task_id):
        return TaskService.tasks.get(int(task_id))


    @staticmethod
    def get_tasks(account_id):
        return list(TaskService.tasks.values())


    @staticmethod
    def update_task(account_id, task_id, body):
        task = TaskService.tasks.get(int(task_id))
        if not task:
            return None

        task["title"] = body.get("title", task["title"])
        task["description"] = body.get("description", task["description"])

        return task


    @staticmethod
    def delete_task(account_id, task_id):
        TaskService.tasks.pop(int(task_id), None)





