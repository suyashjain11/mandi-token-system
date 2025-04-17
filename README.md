# 🌾 Mandi Token System - Django Web App

A smart and simple token management system built for farmers to save time at the mandi (market). Farmers can pre-book their arrival using a token, reducing unnecessary waiting and crowding.

![Made with Django](https://img.shields.io/badge/Built%20with-Django-blue?logo=django)
![Bootstrap](https://img.shields.io/badge/Styled%20with-Bootstrap-purple?logo=bootstrap)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)

---

## 🚀 Live Demo

👉 [Click here to try it out](https://suyashjain685.pythonanywhere.com/)  
*(Replace with your actual deployed link when ready)*

---

## 📸 Demo Preview

![Homepage Screenshot](screenshots/homepage.png)

---

## 💡 Features

- 👨‍🌾 Farmers can generate tokens from home
- 🕒 Estimated arrival times are auto-scheduled
- 👀 View and cancel tokens by contact number
- 🔐 Admin login to see full token dashboard
- 📱 Responsive design with Bootstrap
- 📩 Email alerts (and SMS ready!)
- 🚀 Deployable on PythonAnywhere or Render

---

## 🧱 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, Bootstrap 5
- **Database**: SQLite3 (can be upgraded to PostgreSQL)
- **Deployment**: PythonAnywhere
- **Version Control**: Git & GitHub

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/yourusername/mandi-token-system.git
cd mandi-token-system
python -m venv venv
venv\\Scripts\\activate    # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
