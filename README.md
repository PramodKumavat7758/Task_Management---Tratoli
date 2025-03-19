# 🚀 Task Management System

A high-performance **Task Management System** built with **Django REST Framework**, **Celery**, **Redis**, **PostgreSQL**, **Django Channels**, and **Docker**.  

## 🌟 Features
- ✅ **User Authentication** (JWT-based authentication)
- ✅ **Task Management** (Create, Assign, Update, Delete)
- ✅ **Multi-threaded Report Generation** (Handles 100,000+ tasks efficiently)
- ✅ **Real-Time Task Updates** (Django Channels & WebSockets)
- ✅ **Asynchronous Notifications** (Celery + Redis)
- ✅ **Caching for Performance** (Redis)
- ✅ **Fully Dockerized Deployment**

## 🚀 Tech Stack
- ✅ **Backend: Django, Django REST Framework (DRF)**
- ✅ **Database: PostgreSQL**
- ✅ **Asynchronous Tasks: Celery, Redis**
- ✅ **Deployment: Docker, Gunicorn**
- ✅ **Authentication: JWT (JSON Web Token)**





## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/task-management.git
cd task-management
```

### **2 Install Requirements**
```bash
pip install -r requirements.txt
```
### **3 Apply Migrations**
```bash
python manage.py migrate
python manage.py createsuperuser
```

### **4 Run Server**
```bash
python manage.py runserver
```

- Open postman Api collection tool http://localhost:8080/api/tasks
     ![Postman](tasks-postman.png)
- Celery Logs
      ![Celery](celery-log.png)
- Redis Logs
      ![Redis](redis-log.png)

