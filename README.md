# Nutri-Concierge

Nutri-Concierge is a multi-agent nutrition assistant that uses the Edamam Food API + ADK agents + Streamlit UI to provide dynamic nutrition queries, meal planning, and macros calculation.

## Features
- Edamam-powered food database lookups  
- Multi-agent orchestration (search, planner, coordinator)  
- Memory for session-aware suggestions  
- Streamlit UI: search, compare, meal planning, recipe builder  
- Secure configuration via environment variables  

## Project Structure
```bash
nutri_concierge/
├── backend/
├── ui/
├── requirements.txt
├── .env
└── README.md
```

# Create Virtual Environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Or macOS / Linux
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Create .env file with:
### GOOGLE_API_KEY=...
### EDAMAM_APP_ID=...
### EDAMAM_APP_KEY=...

# run app
streamlit run ui/app.py
