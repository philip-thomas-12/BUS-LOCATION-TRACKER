# 🚌 BusFinder


A simple Django + Google Maps web application that simulates real-time bus tracking.  
Users can view bus locations on an interactive map, similar to Uber-style tracking.

---

## 🚀 Features
- Django backend with clean structure
- Google Maps integration
- Configurable API key via `.env` file
- Ready for deployment on platforms like **Heroku / Render / Railway**
- Requirements file included for easy setup

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/busfinder.git
cd busfinder

2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root and add:
SECRET_KEY=your-django-secret-key
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
5. Apply Migrations
python manage.py migrate
6. Run the Development Server
python manage.py runserver
Visit: http://127.0.0.1:8000/map/
🛠 Deployment
Generate a requirements.txt
pip freeze > requirements.txt
Use Procfile (for Heroku) or config (for Render/Railway).
Set environment variables on the hosting platform.

💡 Future Improvements
Add database for real-time bus positions
Simulate live movement of buses
User login system to track favorite buses
