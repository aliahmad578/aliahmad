# Healthcare Classifier — Streamlit demo

This repository runs the supplied `healthcare_classifier_model.pkl` using Streamlit.

## Files

- `app.py` — Streamlit user interface.
- `healthcare_classifier_model.pkl` — your trained Random Forest model.
- `requirements.txt` — Python dependencies.
- `.gitignore` — excludes local environment/cache files.

## Run locally (Windows)

1. Install Python 3.10–3.12.
2. Open Command Prompt or PowerShell in this project folder.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Start the app:

   ```powershell
   streamlit run app.py
   ```

6. Open the local URL printed in the terminal (usually http://localhost:8501).

## Upload to GitHub

1. Sign in at https://github.com.
2. Click **New repository**.
3. Name it `healthcare-classifier-streamlit`.
4. Choose Public or Private, then click **Create repository**.
5. In the new repository, choose **Add file → Upload files**.
6. Upload `app.py`, `requirements.txt`, `README.md`, `.gitignore`, and
   `healthcare_classifier_model.pkl`.
7. Commit the files to the `main` branch.

Keep the model file in the repository root, beside `app.py`.

## Deploy on Streamlit Community Cloud

1. Visit https://share.streamlit.io/ and sign in with GitHub.
2. Click **Create app**.
3. Select your repository, branch `main`, and main file path `app.py`.
4. Click **Deploy**.
5. Wait for the build to finish. Streamlit will provide an app URL ending in
   `streamlit.app`.

When you push changes to the connected GitHub repository, Streamlit Community
Cloud will redeploy the app.

## Important model compatibility note

Pickled scikit-learn models are not guaranteed to work across scikit-learn
versions. The `requirements.txt` gives a reasonable starting environment, but
the exact scikit-learn version used when the pickle was created is not recorded
in the supplied source code. If deployment logs show a model/version error,
recreate the model in a clean environment, record the exact package versions,
and pin those versions in `requirements.txt`.

Only load pickle files you trust. Pickle deserialization can execute code.

## Important healthcare limitation

The supplied training script generates random synthetic data; it does not
train on real patient records or clinically validated labels. The app is
therefore an educational/demo project only, not a medical device or clinical
decision-support system. Do not enter real patient information or use its
outputs for diagnosis, triage, or treatment.
