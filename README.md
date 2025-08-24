# 🍷 Wine Quality Prediction

This project builds a Machine Learning model to predict **wine quality** (0–10) using the [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality) from UCI.  
The model is trained with **Linear Regression**, containerized with **Docker**, and deployed to **Heroku**.  

---

## 📂 Repository Structure
- `Assignment#5_ANA680.ipynb` → Jupyter Notebook (EDA, training, evaluation)  
- `wine_quality_model.pkl` → Trained scikit-learn model  
- `app.py` → Flask API for serving predictions  
- `requirements.txt` → Dependencies  
- `Dockerfile` → Docker build instructions  
- `Procfile` → Heroku entry point  

---

## Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/StutteringEmo/wine-quality-ml.git
cd wine-quality-ml
```

### 2. Local Python Run
```bash
pip install -r requirements.txt
python app.py
```
App runs at: http://127.0.0.1:5000

## Run with Docker

### Build the image
```bash
docker build -t wine-quality-app .
```

### Run the container
```bash
docker run -p 5000:5000 wine-quality-app
```
App available at: http://127.0.0.1:5000

## API Usage

### Base endpoint
```http
GET /
```
➡ Returns: "Wine Quality Prediction API is running!"

### Predict endpoint
```http
POST /predict
Content-Type: application/json
```

## Wine Quality Prediction App

This project is a Machine Learning model deployment using Flask + Docker + Heroku.
It predicts wine quality based on physicochemical properties.

### Features
- Flask API for predictions (/predict)
- Simple web form UI for manual input
- Dockerized for portability
- Deployed on Heroku

### Example Input (Web Form)

Example request:
<img width="322" height="307" alt="image" src="https://github.com/user-attachments/assets/29b2df1b-7948-463d-89c9-6312ce612fa3" />

Example response:
<img width="460" height="50" alt="image" src="https://github.com/user-attachments/assets/f0efdd27-ba66-461b-bbe8-8136b7e6e755" />
