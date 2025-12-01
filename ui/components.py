import streamlit as st

def food_card(food):
    n = food.get("nutrients", {})
    st.markdown(
        f"""
        <div style="border:1px solid #ddd;padding:15px;border-radius:12px;background:#fafafa;margin-bottom:10px;">
            <h3 style="margin:0;">{food['label']}</h3>
            <p style="color:#888;margin:0;">{food.get('category','')}</p>
            <ul>
                <li>Calories: {n.get('ENERC_KCAL','N/A')}</li>
                <li>Protein: {n.get('PROCNT','N/A')} g</li>
                <li>Fat: {n.get('FAT','N/A')} g</li>
                <li>Carbs: {n.get('CHOCDF','N/A')} g</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
