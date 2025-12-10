Task 1 — Flask Backend CRUD API

This project implements backend APIs using Flask as requested in the assessment.
It includes:

✔ Simple authentication
✔ GET tasks
✔ CREATE tasks
✔ UPDATE tasks
✔ DELETE tasks

All APIs were tested using Thunder Client.

🚀 Run Backend

Open Terminal in backend folder:

cd src/apps/backend
python server.py


Then backend starts at:

http://127.0.0.1:5000

AUTH (Login)

POST

/api/auth/access-tokens


Body

{
  "username": "admin",
  "password": "admin"
}



Response

{
  "access_token": "TEST_TOKEN"
}

<img width="1356" height="431" alt="image" src="https://github.com/user-attachments/assets/910b3e9e-8fc2-49ce-8a78-b44e98f9e3af" />



Use this header for all task APIs:

Authorization: Bearer TEST_TOKEN

🧩 TASKS CRUD API (main part of this task)

Base URL:

/api/accounts/1/tasks

➕ Create Task

POST

/api/accounts/1/tasks


Body

{
  "title": "First task",
  "description": "Testing"
}

<img width="1011" height="365" alt="image" src="https://github.com/user-attachments/assets/ad63556e-93cb-41cc-97e2-b3aa68af2aaf" />


📥 Get All Tasks

GET

/api/accounts/1/tasks

🔍 Get One Task

GET

/api/accounts/1/tasks/1

<img width="1014" height="374" alt="image" src="https://github.com/user-attachments/assets/4fc76d42-56f1-4064-a154-67a05e6c1660" />


✏ Update Task

PATCH

/api/accounts/1/tasks/1


Body

{
  "title": "Updated",
  "description": "Updated description"
}

<img width="1014" height="382" alt="image" src="https://github.com/user-attachments/assets/2bce44fe-e4eb-4f42-8953-20e7dd75ea1b" />

❌ Delete Task

DELETE

/api/accounts/1/tasks/1

<img width="1009" height="384" alt="image" src="https://github.com/user-attachments/assets/fd32e825-51bd-4384-ab62-2407defa8863" />

✔ Completed in this task

Flask API setup

Authentication endpoint

Task create

Task read

Task update

Task delete


