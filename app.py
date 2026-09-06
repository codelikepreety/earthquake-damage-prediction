import streamlit as st
import pandas as pd
#import joblib
import requests

API_URL = "https://earthquake-damage-api.onrender.com"
# --------------------------------
# Load trained model
# --------------------------------

#model = joblib.load("models/earthquake_damage_model_final.pkl")


# --------------------------------
# Page configuration
# --------------------------------

st.set_page_config(
    page_title="Earthquake Damage Predictor",
    page_icon="🏚️",
    layout="wide"
)


# --------------------------------
# Title
# --------------------------------

st.title("🏚️ Earthquake Damage Predictor")

st.write(
    "Predict the expected damage grade of a building "
    "using a machine learning model."
)


# --------------------------------
# Location Information
# --------------------------------

st.header("📍 Location Information")

col1, col2, col3 = st.columns(3)

with col1:
    geo_level_1_id = st.number_input(
        "Geo Level 1 ID",
        min_value=0,
        value=6
    )

with col2:
    geo_level_2_id = st.number_input(
        "Geo Level 2 ID",
        min_value=0,
        value=1350
    )

with col3:
    geo_level_3_id = st.number_input(
        "Geo Level 3 ID",
        min_value=0,
        value=3790
    )


# --------------------------------
# Building Characteristics
# --------------------------------

st.header("🏠 Building Characteristics")

col1, col2, col3 = st.columns(3)

with col1:
    count_floors_pre_eq = st.number_input(
        "Number of Floors",
        min_value=1,
        value=3
    )

with col2:
    age = st.number_input(
        "Building Age",
        min_value=0,
        value=60
    )

with col3:
    count_families = st.number_input(
        "Number of Families",
        min_value=0,
        value=1
    )

col1, col2 = st.columns(2)

with col1:
    area_percentage = st.number_input(
        "Area Percentage",
        min_value=0,
        value=12
    )

with col2:
    height_percentage = st.number_input(
        "Height Percentage",
        min_value=0,
        value=8
    )
# --------------------------------
# Construction Information
# --------------------------------

st.header("🔨 Construction Information")

col1, col2 = st.columns(2)

with col1:

    land_surface_condition_label = st.selectbox(
        "Land Surface Condition",
        ["Flat", "Moderate slope", "Steep slope"]
    )

    foundation_type_label = st.selectbox(
        "Foundation Type",
        [
            "Other",
            "Mud",
            "Wood",
            "Brick",
            "Cement"
        ]
    )

    roof_type_label = st.selectbox(
        "Roof Type",
        [
            "Other",
            "Bamboo/wood",
            "Cement"
        ]
    )

    ground_floor_type_label = st.selectbox(
        "Ground Floor Type",
        [
            "Mud",
            "Other",
            "Brick/stone",
            "Timber",
            "Cement"
        ]
    )

with col2:

    other_floor_type_label = st.selectbox(
        "Other Floor Type",
        [
            "Not applicable",
            "Timber",
            "RCC",
            "Other"
        ]
    )

    position_label = st.selectbox(
        "Building Position",
        [
            "Not specified",
            "Attached to another building",
            "Detached",
            "Corner"
        ]
    )

    plan_configuration_label = st.selectbox(
        "Plan Configuration",
        [
            "Rectangular",
            "Square",
            "U-shaped",
            "L-shaped",
            "T-shaped",
            "Other",
            "Irregular"
        ]
    )

    legal_ownership_status_label = st.selectbox(
        "Legal Ownership Status",
        [
            "Private",
            "Public",
            "Other"
        ]
    )

# --------------------------------
# Convert user-friendly labels
# to dataset values
# --------------------------------

land_surface_map = {
    "Flat": "n",
    "Moderate slope": "o",
    "Steep slope": "t"
}

foundation_map = {
    "Other": "r",
    "Mud": "w",
    "Wood": "u",
    "Brick": "i",
    "Cement": "h"
}

roof_map = {
    "Other": "n",
    "Bamboo/wood": "q",
    "Cement": "x"
}

ground_floor_map = {
    "Mud": "f",
    "Other": "m",
    "Brick/stone": "v",
    "Timber": "x",
    "Cement": "z"
}

other_floor_map = {
    "Not applicable": "q",
    "Timber": "s",
    "RCC": "x",
    "Other": "j"
}

position_map = {
    "Not specified": "s",
    "Attached to another building": "t",
    "Detached": "j",
    "Corner": "o"
}

plan_configuration_map = {
    "Rectangular": "d",
    "Square": "q",
    "U-shaped": "u",
    "L-shaped": "s",
    "T-shaped": "m",
    "Other": "c",
    "Irregular": "a"
}

legal_ownership_map = {
    "Private": "v",
    "Public": "a",
    "Other": "r"
}

land_surface_condition = land_surface_map[
    land_surface_condition_label
]

foundation_type = foundation_map[
    foundation_type_label
]

roof_type = roof_map[
    roof_type_label
]

ground_floor_type = ground_floor_map[
    ground_floor_type_label
]

other_floor_type = other_floor_map[
    other_floor_type_label
]

position = position_map[
    position_label
]

plan_configuration = plan_configuration_map[
    plan_configuration_label
]

legal_ownership_status = legal_ownership_map[
    legal_ownership_status_label
]


# --------------------------------
# Structural Features
# --------------------------------

st.header("🏗️ Structural Features")

with st.expander("🏗️ Superstructure Features", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        has_superstructure_adobe_mud = st.checkbox(
            "Adobe / Mud Structure"
        )

        has_superstructure_mud_mortar_stone = st.checkbox(
            "Mud Mortar Stone Structure"
        )

        has_superstructure_stone_flag = st.checkbox(
            "Stone Flag Structure"
        )

        has_superstructure_cement_mortar_stone = st.checkbox(
            "Cement Mortar Stone Structure"
        )

        has_superstructure_mud_mortar_brick = st.checkbox(
            "Mud Mortar Brick Structure"
        )

        has_superstructure_cement_mortar_brick = st.checkbox(
            "Cement Mortar Brick Structure"
        )

    with col2:

        has_superstructure_timber = st.checkbox(
            "Timber Structure"
        )

        has_superstructure_bamboo = st.checkbox(
            "Bamboo Structure"
        )

        has_superstructure_rc_non_engineered = st.checkbox(
            "Non-Engineered Reinforced Concrete"
        )

        has_superstructure_rc_engineered = st.checkbox(
            "Engineered Reinforced Concrete"
        )

        has_superstructure_other = st.checkbox(
            "Other Superstructure"
        )


with st.expander("🏢 Secondary Building Use", expanded=False):

    col1, col2 = st.columns(2)

    with col1:

        has_secondary_use = st.checkbox(
            "Has Secondary Use"
        )

        has_secondary_use_agriculture = st.checkbox(
            "Agricultural Use"
        )

        has_secondary_use_hotel = st.checkbox(
            "Hotel Use"
        )

        has_secondary_use_rental = st.checkbox(
            "Rental Use"
        )

        has_secondary_use_institution = st.checkbox(
            "Institutional Use"
        )

        has_secondary_use_school = st.checkbox(
            "School Use"
        )

    with col2:

        has_secondary_use_industry = st.checkbox(
            "Industrial Use"
        )

        has_secondary_use_health_post = st.checkbox(
            "Health Post Use"
        )

        has_secondary_use_gov_office = st.checkbox(
            "Government Office Use"
        )

        has_secondary_use_use_police = st.checkbox(
            "Police Use"
        )

        has_secondary_use_other = st.checkbox(
            "Other Secondary Use"
        )

# --------------------------------
# Create Input DataFrame
# --------------------------------

input_data = pd.DataFrame([{
    "geo_level_1_id": geo_level_1_id,
    "geo_level_2_id": geo_level_2_id,
    "geo_level_3_id": geo_level_3_id,

    "count_floors_pre_eq": count_floors_pre_eq,
    "age": age,
    "area_percentage": area_percentage,
    "height_percentage": height_percentage,
    "count_families": count_families,

    "land_surface_condition": land_surface_condition,
    "foundation_type": foundation_type,
    "roof_type": roof_type,
    "ground_floor_type": ground_floor_type,
    "other_floor_type": other_floor_type,
    "position": position,
    "plan_configuration": plan_configuration,
    "legal_ownership_status": legal_ownership_status,

    "has_superstructure_adobe_mud": int(has_superstructure_adobe_mud),
    "has_superstructure_mud_mortar_stone": int(has_superstructure_mud_mortar_stone),
    "has_superstructure_stone_flag": int(has_superstructure_stone_flag),
    "has_superstructure_cement_mortar_stone": int(has_superstructure_cement_mortar_stone),
    "has_superstructure_mud_mortar_brick": int(has_superstructure_mud_mortar_brick),
    "has_superstructure_cement_mortar_brick": int(has_superstructure_cement_mortar_brick),
    "has_superstructure_timber": int(has_superstructure_timber),
    "has_superstructure_bamboo": int(has_superstructure_bamboo),
    "has_superstructure_rc_non_engineered": int(has_superstructure_rc_non_engineered),
    "has_superstructure_rc_engineered": int(has_superstructure_rc_engineered),
    "has_superstructure_other": int(has_superstructure_other),

    "has_secondary_use": int(has_secondary_use),
    "has_secondary_use_agriculture": int(has_secondary_use_agriculture),
    "has_secondary_use_hotel": int(has_secondary_use_hotel),
    "has_secondary_use_rental": int(has_secondary_use_rental),
    "has_secondary_use_institution": int(has_secondary_use_institution),
    "has_secondary_use_school": int(has_secondary_use_school),
    "has_secondary_use_industry": int(has_secondary_use_industry),
    "has_secondary_use_health_post": int(has_secondary_use_health_post),
    "has_secondary_use_gov_office": int(has_secondary_use_gov_office),
    "has_secondary_use_use_police": int(has_secondary_use_use_police),
    "has_secondary_use_other": int(has_secondary_use_other)
}])

# --------------------------------
# Damage Grade Information
# --------------------------------

st.header("ℹ️ Damage Grade Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Grade 1")
    st.write("Low damage")

with col2:
    st.write("### Grade 2")
    st.write("Moderate damage")

with col3:
    st.write("### Grade 3")
    st.write("Severe damage")


# --------------------------------
# Prediction
# --------------------------------

st.header("🔮 Prediction")

if st.button("Predict Damage Grade", type="primary"):

    try:
        # Convert DataFrame row into JSON-compatible dictionary
        payload = input_data.to_dict(orient="records")[0]

        # Send prediction request to FastAPI
        response = requests.post(
            f"{API_URL}/predict",
            json=payload,
            timeout=30
        )

        # Raise an error if API returned 4xx/5xx
        response.raise_for_status()

        # Get JSON response
        result = response.json()

        prediction = result["damage_grade"]

        probabilities = [
            result["probabilities"]["grade_1"],
            result["probabilities"]["grade_2"],
            result["probabilities"]["grade_3"]
        ]

        grade_descriptions = {
            1: "Low damage",
            2: "Moderate damage",
            3: "Severe damage"
        }

        description = grade_descriptions[prediction]

        confidence = probabilities[prediction - 1] * 100

        # Prediction result
        st.success(f"Predicted Damage Grade: {prediction}")

        st.info(
            f"**{description}** — "
            f"The model assigns a probability of "
            f"**{confidence:.1f}%** to this grade."
        )

        # Probability metrics
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Grade 1",
            f"{probabilities[0] * 100:.1f}%"
        )

        col2.metric(
            "Grade 2",
            f"{probabilities[1] * 100:.1f}%"
        )

        col3.metric(
            "Grade 3",
            f"{probabilities[2] * 100:.1f}%"
        )

        # Probability chart
        probability_df = pd.DataFrame({
            "Damage Grade": [
                "Grade 1",
                "Grade 2",
                "Grade 3"
            ],
            "Probability": probabilities
        })

        st.bar_chart(
            probability_df.set_index("Damage Grade")
        )

    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the FastAPI backend. "
            "Make sure the API is running."
        )

    except requests.exceptions.Timeout:
        st.error(
            "The prediction request timed out. "
            "Please try again."
        )

    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")