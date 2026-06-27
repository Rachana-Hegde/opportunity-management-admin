# 🧩 Opportunity Management Admin Dashboard

A full-stack **Opportunity Management Web Application** built as part of a screening assignment.  
It allows admins to securely manage opportunities with full CRUD functionality and data isolation.

---

## 🚀 Features

### 🔐 Authentication

- Admin Signup & Login  
- Session-based authentication (Flask-Login)  
- Captcha validation for login security  
- Protected routes  

---

### 📋 Opportunity Management

- Create new opportunities  
- View only your own opportunities (multi-admin isolation)  
- Edit existing opportunities  
- Delete opportunities with confirmation  
- View detailed information in modal  

---

### 💻 Frontend

- HTML, CSS, JavaScript  
- Responsive UI (provided template)  
- Dynamic rendering using API calls  
- No page refresh required  

---

### ⚙️ Backend

- Python (Flask)  
- RESTful APIs  
- Flask-Login for authentication  
- Flask-SQLAlchemy ORM  

---

### 🗄️ Database

- SQLite  
- Structured schema for admin and opportunities  
- Persistent data storage  

---

## 🛠️ Tech Stack

| Layer    | Technology              |
| -------- | ---------------------- |
| Frontend | HTML, CSS, JavaScript  |
| Backend  | Flask (Python)         |
| Database | SQLite                 |
| Auth     | Flask-Login, Sessions  |

---

## 📁 Project Structure

```

project-root/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── dashboard.html
│
├── instance/
│   └── database.db
│
├── app.py
├── routes.py
├── models.py
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

---

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/opportunity-management-admin.git
cd opportunity-management-admin
````

---

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Run the Application

```bash
python app.py
```

---

### ▶️ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### 🔐 Authentication

| Method | Endpoint         | Description    |
| ------ | ---------------- | -------------- |
| POST   | `/signup`        | Register admin |
| POST   | `/login`         | Login admin    |
| POST   | `/logout`        | Logout admin   |
| GET    | `/check-session` | Check session  |

---

### 📋 Opportunities

| Method | Endpoint             | Description             |
| ------ | -------------------- | ----------------------- |
| GET    | `/opportunities`     | Get admin opportunities |
| POST   | `/opportunities`     | Create opportunity      |
| PUT    | `/opportunities/:id` | Update opportunity      |
| DELETE | `/opportunities/:id` | Delete opportunity      |

---

## 🔐 Security

* Each admin can access only their own data
* Unauthorized edit/delete operations are blocked
* Session-based authentication prevents unauthorized access
* Captcha prevents bot login attempts

---

## ⚠️ Notes

* No hardcoded data used
* All opportunities stored in database
* UI strictly follows provided design
* Real-time UI updates without page refresh

---

## 📌 Conclusion

This project demonstrates:

* Full-stack web development
* Authentication & access control
* Database design & relationships
* REST API integration
* Dynamic UI rendering

---

## 👩‍💻 Author

**Rachana Hegde**
🔗 GitHub: [https://github.com/Rachana-Hegde](https://github.com/Rachana-Hegde)

## 🌐 Live API

https://opportunity-app.onrender.com
