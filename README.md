# Nutri-Concierge

Nutri-Concierge is a multi-agent nutrition assistant that uses the Edamam Food API + ADK agents + Streamlit UI to provide dynamic nutrition queries, meal planning, and macros calculation.

## Features
- Edamam-powered food database lookups
- Multi-agent orchestration (search, planner, coordinator)
- Memory for session-aware suggestions
- Streamlit UI: search, compare, meal planning, recipe builder
- Secure configuration via environment variables

## Project Structure
nutri_concierge/
├── backend/
├── ui/
├── requirements.txt
├── .env
└── README.md

## Quickstart (local)
```bash
# create venv
python -m venv venv
# activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1
# or macOS / Linux
source venv/bin/activate

pip install -r requirements.txt

# Create a .env file with:
# GOOGLE_API_KEY=...
# EDAMAM_APP_ID=...
# EDAMAM_APP_KEY=...

streamlit run ui/app.py

