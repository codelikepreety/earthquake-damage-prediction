Earthquake Damage Prediction

An end-to-end machine learning application for predicting earthquake building damage.

Predicts earthquake damage grades (1–3) from structural and location-based building features, with a deployed ML API and interactive web interface.

<p align="center">
  <a href="https://earthquake-damage-predictor.streamlit.app/">Live Link</a> •
  <a href="https://github.com/codelikepreety/earthquake-damage-prediction">GitHub</a> •
</p>

✨ Overview

This project takes a building's characteristics as input and predicts its earthquake damage category.

The goal was to build more than a notebook model — the project follows the complete path from data → model → API → deployed application.

Building Features
       ↓
Preprocessing
       ↓
Random Forest Model
       ↓
FastAPI
       ↓
Streamlit
       ↓
Damage Grade + Probabilities

Damage Grades

Grade

Damage

1

Low damage

2

Medium damage

3

Almost complete destruction

🚀 Live Application

Streamlit App: https://earthquake-damage-predictor.streamlit.app/

Backend API: https://earthquake-damage-api.onrender.com

Interactive API Docs: https://earthquake-damage-api.onrender.com/docs

🧠 Model

A Random Forest Classifier was selected after comparing model configurations and evaluating their performance.

The deployment model was optimized to reduce model size while keeping predictive performance close to the larger configurations tested during development.

Final configuration

Random Forest
├── n_estimators = 20
├── max_features = sqrt
├── min_samples_leaf = 2
├── random_state = 42
└── n_jobs = -1

Test Accuracy: ~71.72%
Macro F1: ~0.648

The final serialized model is approximately 72 MB.

🛠️ Tech Stack

Machine Learning
Python · Pandas · NumPy · Scikit-learn · Joblib

Backend
FastAPI · Uvicorn · Pydantic

Frontend
Streamlit · Requests

Deployment
Render · Hugging Face Hub · Streamlit Community Cloud

Development
Jupyter Notebook · VS Code · Git · GitHub

🔌 How It Works

The application is split into a frontend and a model-serving backend.

1. User Input

The Streamlit interface collects building and structural characteristics.

2. API Request

The frontend sends the feature values to the FastAPI /predict endpoint.

3. Model Inference

FastAPI loads the private trained model from Hugging Face and performs the prediction.

4. Result

The API returns the predicted damage grade and class probabilities, which are displayed by Streamlit.

┌──────────────┐
│    User      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Streamlit   │
│   Frontend   │
└──────┬───────┘
       │ POST /predict
       ▼
┌──────────────┐
│   FastAPI    │
│    Render    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Hugging    │
│ Face Model   │
└──────┬───────┘
       │
       ▼
  Damage Grade
  + Probabilities

📊 Dataset

Built using the Richter's Predictor: Modeling Earthquake Damage dataset from DrivenData.

The dataset contains building survey information collected in Nepal following the Gorkha earthquake.

View the competition →

The raw dataset and trained model are intentionally excluded from the public GitHub repository.

📁 Project Structure

earthquake-damage-prediction/
│
├── api/
│   └── main.py
│
├── data/
│   └── raw/              # Local dataset
│
├── models/               # Local model
│
├── notebooks/            # EDA & model development
│
├── app.py                # Streamlit application
├── README.md
├── .gitignore
├── requirements-api.txt
└── requirements-streamlit.txt


🔐 Repository & Deployment

The project keeps sensitive and large assets outside the public repository.

.env is ignored by Git

Raw CSV dataset files are ignored

The trained .pkl model is ignored

The model is hosted privately on Hugging Face

FastAPI retrieves the model securely using an environment variable

This keeps the GitHub repository focused on the source code, notebooks, and application architecture.

🎯 Key Takeaways

This project demonstrates practical experience with:

Building an ML classification pipeline

Handling categorical and numerical features

Evaluating an imbalanced multi-class problem

Optimizing a model for deployment constraints

Serving predictions through a REST API

Connecting a frontend to an ML backend

Hosting a trained model separately from application code

Deploying an end-to-end ML application

👤 Author

Anima Mishra