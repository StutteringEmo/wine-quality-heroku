# 🍷 Wine Quality Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue) 
![Flask](https://img.shields.io/badge/Flask-API-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Container-blue) 
![Heroku](https://img.shields.io/badge/Heroku-Deployed-purple)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)

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
- `app.py` → Flask API for serving predictions and web form
- `requirements.txt` → Python dependencies
- `Dockerfile` → Instructions for building the Docker container
- `Procfile` → Heroku entry point

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository and move into the project directory:
```bash
git clone https://github.com/StutteringEmo/wine-quality-ml.git
cd wine-quality-ml
```

### 2. Local Python Run
Install dependencies and run the Flask app directly:
```bash
pip install -r requirements.txt
python app.py
```
➡ Open your browser at: http://127.0.0.1:5000
This is useful if you just want to test the project locally without Docker or Heroku.

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

## API Usage
Once the app is running (locally or on Heroku), you can interact with the API.

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

## Deployment on Heroku
The app can be deployed online using Heroku + Docker.

Steps performed:

1. Set the stack to container:
```bash
heroku stack:set container -a wine-quality
```

2. heroku container:login
```bash
heroku container:login
```

3. Build and push the Docker image to Heroku registry:
```bash
docker buildx build --platform linux/amd64 \
  -t registry.heroku.com/wine-quality/web \
  --provenance=false --push .
```

4. Release the container:
```bash
heroku container:release web -a wine-quality
```

5. Open the deployed app:
```bash
heroku open -a wine-quality
```

✅ Live demo: https://wine-quality-2ac0aee51517.herokuapp.com

---

## Wine Quality Prediction App

In addition to the raw API, the project also provides a simple HTML form for manual input.
This allows you to test the model without needing external tools.

### Features
- Web form for entering wine properties
- Displays prediction and rounded score
- The HTML form is served from the root endpoint (/) and uses the same Flask backend for predictions. This allows both API and web form testing from the same app, whether running locally, in Docker, or on Heroku.

### Example Input (Web Form)

Example request:
<img width="322" height="307" alt="image" src="https://github.com/user-attachments/assets/29b2df1b-7948-463d-89c9-6312ce612fa3" />

Example response:
<img width="460" height="50" alt="image" src="https://github.com/user-attachments/assets/f0efdd27-ba66-461b-bbe8-8136b7e6e755" />

---

## Troubleshooting

Here are some common issues and fixes:

1. Heroku error: manifest unknown or unsupported
Cause: Image built with wrong platform or provenance enabled.
Fix: Use --platform linux/amd64 --provenance=false in your docker buildx command.

```bash
docker buildx build --platform linux/amd64 \
  -t registry.heroku.com/wine-quality/web \
  --provenance=false --push .
```

2. Heroku error: H81 Blank App / 502
Cause: App is deployed but not starting properly.
Fix: Ensure your Dockerfile CMD is correct:

```dockerfile
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
```
- Also confirm your Flask app is named app in app.py.

3. Version mismatch warning in scikit-learn
Cause: You trained with one version and deployed with another.
Fix: Pin scikit-learn in requirements.txt (same version as your training environment), e.g.:

```ini
scikit-learn==1.5.1
```

4. PowerShell confusion (import sklearn)
Remember: PowerShell is not Python. To check library versions, use:

```bash
python -c "import sklearn; print(sklearn.__version__)"
```

5. Docker cache issues
If rebuilds don’t seem to update, clear cache:

```bash
docker builder prune
```

---

## Summary

This project demonstrates:
- Training and saving an ML model
- Serving predictions via Flask API + web form
- Containerizing with Docker
- Deploying to Heroku with troubleshooting steps

With this guide, you can replicate the process on your own machine or deploy your own ML model to the cloud.



