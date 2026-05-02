import streamlit as st
import pickle
import time
import numpy as np
import plotly.graph_objects as go

model=pickle.load(open("fish_model.pkl","rb"))
scaler=pickle.load(open("scaler.pkl","rb"))

st.set_page_config(page_title="Smart Aqua: Oxygen & Health Advisor",page_icon="💧",layout="wide")
st.markdown("""
    <style>
    .main { background-color: #f8fbff; }
    .stMetric { border: 2px solid #0077b6; padding: 15px; border-radius: 15px; background: white; }
    .advice-box { border-left: 5px solid #0077b6; padding-left: 15px; background-color: #e0f2fe; padding: 10px; border-radius: 5px;color:black }
    </style>
    """, unsafe_allow_html=True)
st.title("🐟 Smart Aqua: Precision Monitoring & AI Advisor")
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("🧪 Chemistry")
    ph = st.number_input("Water pH", 0.0, 14.0, 7.0, step=0.1, help="Critical for metabolism.")
    amm = st.number_input("Ammonia (ppm)", 0.0, 5.0, 0.0, format="%.3f", help="Toxic nitrogen byproduct.")

with col2:
    st.subheader("🌡️ Physicals")
    temp = st.number_input("Temperature (°C)", 0.0, 45.0, 24.0, format="%.2f", help="Determines oxygen solubility.")
    turb = st.number_input("Turbidity (NTU)", 0.0, 500.0, 15.0, help="Suspended solids in water.")

with col3:
    st.subheader(" Respiration")
    ox = st.number_input("Dissolved Oxygen (mg/L)", 0.0, 20.0, 7.5, format="%.2f", help="The most vital survival parameter.")
    st.info("💡 Note: Warm water holds less oxygen than cold water.")

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = ox,
    title = {'text': "Dissolved Oxygen Status"},
    gauge = {
        'axis': {'range': [0, 12]},
        'steps': [
            {'range': [0, 3], 'color': "#ff4b4b"}, 
            {'range': [3, 5], 'color': "#ffa500"},  
            {'range': [5, 12], 'color': "#00cc96"}], 
        'bar': {'color': "#0077b6"}
    }
))
st.plotly_chart(fig, use_container_width=True)
prediction=None
if st.button("🚀 Analyze Ecosystem Health"):
    with st.spinner('🤖 AI analyzing biological compatibility and survival thresholds...'):
        time.sleep(1.5)
    
        features = np.array([[ph, temp, turb, ox, amm]])
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0].upper()

    res_col1, res_col2 = st.columns([1, 2])

    with res_col1: 
      st.success(f"### Best Match:\n## {prediction}")
      st.write(f"**AI Confidence Score:** {np.max(model.predict_proba(features_scaled))*100:.1f}%")

    with res_col2:
        
        aqua_info = {
        "ROHU": "Requires large pond areas with rich plankton growth. Maintain pH 7.5-8.5 for best weight gain.",
         "SALMON": "Extremely high oxygen requirements (>8mg/L). Needs cold, moving water. High sensitivity to any waste.",
        "SHRIMP": "Bottom feeders sensitive to ammonia spikes at the pond floor. Monitor alkalinity for molting.",
        "TILAPIA": "Resilient to variable water quality. Best for intensive farming with high stocking densities.",
        "TROUT": "Crystal clear water requirement. High turbidity causes gill irritation and reduces growth rates."
        }
        advice = aqua_info.get(prediction, "Ensure standard aquaculture parameters are maintained.")
    st.markdown(f"<div class='advice-box'><strong>💡 Expert Growth Insight for {prediction}:</strong><br>{advice}</div>", unsafe_allow_html=True)

   
    st.markdown("---")
    st.subheader("🚨 Survival Threshold Alerts")
    
    warn_col1, warn_col2 = st.columns(2)
    
    with warn_col1:
        
        if ox < 3.0:
            st.error(f"⚠️ **LETHAL OXYGEN ALERT:** Dissolved Oxygen is {ox} mg/L! Fish will begin suffocating immediately. Activate all aerators and perform surface agitation.")
        elif ox < 5.0:
            st.warning(f"⚠️ **STRESS ALERT:** Low oxygen ({ox} mg/L) will inhibit feeding and growth. Check for organic decay or high temperatures.")
        else:
            st.write("✅ Oxygen levels are healthy and supportive of growth.")

    with warn_col2:
        
        if amm > 0.05:
            st.error(f"⚠️ **TOXICITY ALERT:** Ammonia ({amm} ppm) is at dangerous levels. High risk of gill damage and death. Stop feeding and change water immediately.")
        else:
            st.write("✅ Nitrogen levels are within safe biological limits.")