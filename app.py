import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Healthcare Classifier Demo",
    page_icon="🩺",
    layout="centered",
)

MODEL_PATH = Path(__file__).parent / "healthcare_classifier_model.pkl"

@st.cache_resource
def load_model():
    # Only load pickle files that you trust and created yourself.
    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)

st.title("🩺 Healthcare Outcome Classifier")
st.caption("A demonstration interface for your trained Random Forest model.")

st.warning(
    "Educational demonstration only. The training script uses randomly generated "
    "synthetic data. This model is not clinically validated and must not be used "
    "to diagnose, triage, or make treatment decisions."
)

try:
    model = load_model()
except Exception as exc:
    st.error(
        "The model could not be loaded. This can happen when the scikit-learn "
        "version used to train the model differs from the deployment version."
    )
    st.code(str(exc))
    st.stop()

st.subheader("Enter the model inputs")
with st.form("prediction_form"):
    age = st.number_input("Age (years)", min_value=18, max_value=100, value=35, step=1)
    blood_pressure = st.number_input(
        "Blood Pressure", min_value=50, max_value=250, value=120, step=1
    )
    cholesterol = st.number_input(
        "Cholesterol", min_value=50, max_value=500, value=200, step=1
    )
    submitted = st.form_submit_button("Classify", type="primary")

if submitted:
    input_data = pd.DataFrame(
        [[age, blood_pressure, cholesterol]],
        columns=["Age", "Blood_Pressure", "Cholesterol"],
    )
    try:
        prediction = model.predict(input_data)[0]
        st.subheader("Model output")
        st.success(f"Predicted class: **{prediction}**")

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            probability_table = pd.DataFrame(
                {"Class": model.classes_, "Model probability": probabilities}
            ).sort_values("Model probability", ascending=False)
            st.dataframe(
                probability_table.style.format({"Model probability": "{:.1%}"}),
                use_container_width=True,
                hide_index=True,
            )
            st.caption(
                "These are model outputs, not medically meaningful probabilities "
                "or an estimate of an individual's actual health."
            )
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")

with st.expander("About this model"):
    st.write(
        "The supplied training script creates 500 synthetic rows and trains a "
        "scikit-learn RandomForestClassifier using Age, Blood_Pressure, and "
        "Cholesterol. Its target labels are Healthy, At Risk, and Critical."
    )
