# 🌤️ AI-Powered Weather App

A full-stack weather web application built using **FastAPI**, **SQLite**, and **Streamlit**.  
This project was created for the **Software Engineer Intern – AI/ML Application** assessment by **PM Accelerator**.

---

##  Features

- 🌍 Enter any location (City, Zip Code, Landmark, etc.)
- ⚡ Fetch **real-time weather** using OpenWeatherMap API
- 🗓️ View a **5-day weather forecast**
- 💾 Save weather history for future reference
- 🧾 View, update, or delete saved queries
- 🎨 Modern frontend built with Streamlit
- 📡 Clean API backend using FastAPI + SQLite

---

## 📸 Demo

🔗 [Demo video link here][(https://drive.google.com/file/d/1d_gjnwGmGjQ46Ut9VNOCQcdPmpJOXTY_/view?usp=sharing)]

---

## 🧠 About PM Accelerator

**PM Accelerator** is a career accelerator for aspiring product managers and software engineers.  
🔗 [Visit our LinkedIn page][(https://www.linkedin.com/company/product-manager-accelerator/](https://www.linkedin.com/school/pmaccelerator/))

---

## 📂 Folder Structure

```bash
.
├── backend/         # FastAPI backend
│   ├── main.py
│   ├── models.py
│   ├── crud.py
│   └── database.py
├── frontend/
│   └── app.py       # Streamlit UI
├── requirements.txt
├── README.md
└── .env
```

## How to Run Locally

1. Clone the repo
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Add your OpenWeatherMap API key
  
Create a .env file in the root: 
```ini
OPENWEATHER_API_KEY=your_api_key_here
```
4. Start the backend
```bash
uvicorn backend.main:app --reload
```
5. Start the frontend
```bash
streamlit run frontend/app.py
```

## Requirements
- Python 3.8+
- Streamlit
- FastAPI
- SQLite
- OpenWeatherMap API

