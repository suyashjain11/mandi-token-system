# 🌾 मंडी टोकन प्रबंधन प्रणाली | Mandi Token System (Django Web App)

Smart and farmer-friendly web app for pre-booking tokens at the mandi (market yard).  
Save time, reduce waiting, and get real-time updates — now in Hindi 🇮🇳!

![Made with Django](https://img.shields.io/badge/Built%20with-Django-blue?logo=django)
![Styled with Bootstrap](https://img.shields.io/badge/Styled%20with-Bootstrap-purple?logo=bootstrap)
![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Live Demo

👉 [Click here to try the app](https://suyashjain685.pythonanywhere.com/)  
*(Replace with correct link if different)*

---

## 📸 Screenshots

*(Upload and insert screenshots later here if needed)*

---

## 💡 Features

- 👨‍🌾 Farmers can easily generate arrival tokens from home
- 🕒 Smart token time assignment (after 30 minutes, in 15-min slots)
- 📅 "Today" and "Tomorrow" booking options
- 🚫 Auto-blocks holidays (Sundays, 2nd/4th Saturdays, Govt Holidays)
- 🛡️ Farmer can **view**, **download PDF**, **cancel** token anytime
- 📈 Mandi Rates page with daily crop prices
- 🗓️ Holiday Calendar showing upcoming mandi holidays
- 📋 Admin Dashboard with Today, Previous, Future tokens
- 📱 Mobile responsive and Hindi-supported design

---

## 🧱 Tech Stack

| Layer       | Tech                 |
| ----------- | -------------------- |
| Backend     | Python, Django        |
| Frontend    | HTML5, Bootstrap 5    |
| Database    | SQLite3 (easily upgradeable) |
| Deployment  | PythonAnywhere        |
| Other Tools | Selenium, ReportLab, Holidays |

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/yourusername/mandi-token-system.git
cd mandi-token-system
python -m venv venv
venv\Scripts\activate      # (Windows)
# OR
source venv/bin/activate    # (Mac/Linux)

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # (Optional for Admin login)
python manage.py runserver
