# 🍷 Wine Quality Prediction

This project builds a Machine Learning model to predict **wine quality** (0–10) using the [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality) from UCI.  
The model is trained with **Linear Regression**, containerized with **Docker**, and deployed to **Heroku**.  

The project demonstrates the full workflow of:

1. Training a model and saving it with scikit-learn
2. Creating a Flask API and a web form UI for predictions
3. Containerizing the app using Docker
4. Deploying it to the cloud with Heroku

---

## 📂 Repository Structure
- `Assignment#5_ANA680.ipynb` → Jupyter Notebook (EDA, training, evaluation)  
- `wine_quality_model.pkl` → Trained scikit-learn model (serialized with pickle)
- `app.py` → Flask app that serves predictions via:
  - `/predict` (API endpoint for JSON input)
  - Web form UI for manual input
- `requirements.txt` → Python dependencies
- `Dockerfile` → Instructions for building the Docker container
- `Procfile` → Tells Heroku how to run the app

---

## Setup Instructions

### 1. Clone the Repository

Download the code from GitHub:
```bash
git clone https://github.com/StutteringEmo/wine-quality-ml.git
cd wine-quality-ml
```

### 2. Local Python Run
If you just want to run it locally with Python (no Docker):
```bash
pip install -r requirements.txt
python app.py
```
➡ Open your browser at: http://127.0.0.1:5000
- You’ll see a simple web form where you can input wine parameters.
- Predictions will be displayed on the page.
- The API can also be called programmatically at /predict with JSON input.

---

## Run with Docker
Docker allows you to package everything (code + dependencies) so it runs the same anywhere.

### Build the image
```bash
docker build -t wine-quality-app .
```

### Run the container
```bash
docker run -p 5000:5000 wine-quality-app
```
➡ App available at: http://127.0.0.1:5000

---

## Deployment on Heroku
Heroku lets you deploy the containerized app to the cloud.

Steps performed:

1. Created a new Heroku app (wine-quality)
2. Set the stack to container:
```bash
heroku stack:set container -a wine-quality
```

3. Built and pushed the Docker image to Heroku registry:
```bash
docker buildx build --platform linux/amd64 -t registry.heroku.com/wine-quality/web --push .
```

4. Released the container:
```bash
heroku container:release web -a wine-quality
```

✅ Live demo: https://wine-quality-2ac0aee51517.herokuapp.com

---

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

{
  "features": [7.4, 0.70, 0.00, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]
}
```

### Example Response:
```json
{
  "prediction": 4.98
}
```

---

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

---

## Summary

This repo demonstrates a full ML deployment pipeline:

1. Train ML model → Save with pickle
2. Build API + UI → Flask app
3. Containerize → Docker
4. Deploy → Heroku

With this setup, you can:
- Run locally with Python
- Run in Docker for portability
- Deploy to Heroku for public access
