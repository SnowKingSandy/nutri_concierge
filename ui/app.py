# ui/app.py (top of file) - paste exactly
import sys, pathlib

# --- Ensure project root is on sys.path so 'backend' and 'ui' import work ---
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Now import using absolute package paths
from backend.runner import ask_backend
from ui.components import food_card

import streamlit as st
import asyncio
import json
from backend.runner import ask_backend
from ui.components import food_card

st.set_page_config(page_title="Nutri Concierge 3.0", page_icon="🥗")

st.title("🥗 Nutri Concierge 3.0")
query = st.text_input("Ask something:")

if query:
    with st.spinner("Thinking..."):
        result = asyncio.run(ask_backend(query))

    st.subheader("Assistant Response")
    st.write(result)

    try:
        data = json.loads(result)
    except:
        data = {}

    if "foods" in data:
        st.header("Foods Found")
        for f in data["foods"]:
            food_card(f)

    if "meal_plan" in data:
        st.header("Meal Plan")
        for f in data["meal_plan"]:
            food_card(f)
