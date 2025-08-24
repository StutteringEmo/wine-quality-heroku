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

Example request:
```json
{
  "features": [7.4, 0.70, 0.00, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]
}
```

Example response:
```json
{
  "prediction": 5.0
}
```

