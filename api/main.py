from pathlib import Path
import os

import joblib
import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from huggingface_hub import hf_hub_download
from pydantic import BaseModel, Field
load_dotenv()

# --------------------------------------------------
# Load trained model
# --------------------------------------------------

MODEL_REPO = "codelikepreety/earthquake-damage-prediction"
MODEL_FILENAME = "earthquake_damage_model_final.pkl"

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN environment variable is not set.")

model_path = hf_hub_download(
    repo_id=MODEL_REPO,
    filename=MODEL_FILENAME,
    token=HF_TOKEN
)

model = joblib.load(model_path)


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Earthquake Damage Prediction API",
    description="API for predicting earthquake building damage grades",
    version="1.0.0"
)


# --------------------------------------------------
# Request schema
# --------------------------------------------------

class BuildingFeatures(BaseModel):

    # Location
    geo_level_1_id: int = Field(ge=0)
    geo_level_2_id: int = Field(ge=0)
    geo_level_3_id: int = Field(ge=0)

    # Building characteristics
    count_floors_pre_eq: int = Field(ge=0)
    age: int = Field(ge=0)
    area_percentage: int = Field(ge=0)
    height_percentage: int = Field(ge=0)
    count_families: int = Field(ge=0)

    # Categorical features
    land_surface_condition: str
    foundation_type: str
    roof_type: str
    ground_floor_type: str
    other_floor_type: str
    position: str
    plan_configuration: str
    legal_ownership_status: str

    # Superstructure
    has_superstructure_adobe_mud: int = Field(ge=0, le=1)
    has_superstructure_mud_mortar_stone: int = Field(ge=0, le=1)
    has_superstructure_stone_flag: int = Field(ge=0, le=1)
    has_superstructure_cement_mortar_stone: int = Field(ge=0, le=1)
    has_superstructure_mud_mortar_brick: int = Field(ge=0, le=1)
    has_superstructure_cement_mortar_brick: int = Field(ge=0, le=1)
    has_superstructure_timber: int = Field(ge=0, le=1)
    has_superstructure_bamboo: int = Field(ge=0, le=1)
    has_superstructure_rc_non_engineered: int = Field(ge=0, le=1)
    has_superstructure_rc_engineered: int = Field(ge=0, le=1)
    has_superstructure_other: int = Field(ge=0, le=1)

    # Secondary use
    has_secondary_use: int = Field(ge=0, le=1)
    has_secondary_use_agriculture: int = Field(ge=0, le=1)
    has_secondary_use_hotel: int = Field(ge=0, le=1)
    has_secondary_use_rental: int = Field(ge=0, le=1)
    has_secondary_use_institution: int = Field(ge=0, le=1)
    has_secondary_use_school: int = Field(ge=0, le=1)
    has_secondary_use_industry: int = Field(ge=0, le=1)
    has_secondary_use_health_post: int = Field(ge=0, le=1)
    has_secondary_use_gov_office: int = Field(ge=0, le=1)
    has_secondary_use_use_police: int = Field(ge=0, le=1)
    has_secondary_use_other: int = Field(ge=0, le=1)


# --------------------------------------------------
# Root endpoint
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Earthquake Damage Prediction API is running"
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict_damage(building: BuildingFeatures):

    try:
        input_data = pd.DataFrame([building.model_dump()])

        prediction = int(model.predict(input_data)[0])

        probabilities = model.predict_proba(input_data)[0]

        return {
            "damage_grade": prediction,
            "probabilities": {
                "grade_1": float(probabilities[0]),
                "grade_2": float(probabilities[1]),
                "grade_3": float(probabilities[2])
            }
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )