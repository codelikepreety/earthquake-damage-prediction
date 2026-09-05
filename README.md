# Earthquake Damage Prediction

A machine learning project that predicts the damage grade of a building after an earthquake based on its structural, geographic, and building-related characteristics.

## Problem

The goal is to predict the damage grade of a building using information such as:

- Geographic location
- Building age
- Number of floors
- Building area and height
- Foundation type
- Roof type
- Ground floor type
- Structural materials
- Secondary building usage

The target variable is `damage_grade`.

## Damage Grades

- Grade 1 — Low damage
- Grade 2 — Moderate damage
- Grade 3 — Severe damage

## Dataset

The project uses the earthquake damage dataset containing:

- `train_values.csv` — building features
- `train_labels.csv` — damage grade labels

The dataset contains 260,601 building records.

## Machine Learning Workflow

```text
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Train/Test Split
     ↓
Categorical Feature Encoding
     ↓
Preprocessing Pipeline
     ↓
Random Forest Classifier
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Saved Model
     ↓
Streamlit Application