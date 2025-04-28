# 🌾 मंडी टोकन प्रबंधन प्रणाली | Mandi Token Management System

An easy-to-use web application to help farmers pre-book their arrival slots at the mandi, reduce waiting time, and get live mandi rates and holiday schedules — all in Hindi 🇮🇳!

---

## 🛠️ Features

- ✅ Token Generation with 15-minute arrival slots
- ✅ Minimum 30-minute delay after booking
- ✅ "Today" and "Tomorrow" token selection
- ✅ Holiday detection (Sundays, 2nd and 4th Saturdays, Govt Holidays)
- ✅ Token Redemption and Cancellation
- ✅ Admin Dashboard to view Today's, Previous, and Future Tokens
- ✅ Download Token as PDF
- ✅ Daily Mandi Crop Price Updates
- ✅ Hindi Language Support
- ✅ Responsive UI with Bootstrap 5

---

## ⚙️ Technologies Used

- Django (Python Backend Framework)
- Python 3.13
- SQLite (Default Django database)
- Bootstrap 5 (Frontend styling)
- Selenium (for scraping mandi rates)
- ReportLab (for PDF generation)
- Holidays (Python package for Indian holidays)

---

## 🚀 How to Run Locally

1. Clone the repository:

    ```bash
    git clone https://github.com/suyashjain11/mandi-token-system.git
    cd mandi-token-system
    ```

2. Create a virtual environment:

    ```bash
    python -m venv mandi-env
    source mandi-env/bin/activate  # For Linux/macOS
    mandi-env\Scripts\activate     # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser (optional for admin login):

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the app at:  
   `http://127.0.0.1:8000/`

---

## 📸 Screenshots

(👉 You can add screenshots here later by uploading in your GitHub repo and linking.)

---

## 📅 Upcoming Improvements

- Hindi dynamic translation using Django i18n
- Farmer SMS Notifications (future)
- OTP Verification on phone number (future)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use and modify!

