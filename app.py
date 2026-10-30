import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Smart Agriculture Automation", page_icon="🌱", layout="wide")

st.title("🌱 Smart Agriculture Automation System")
st.write("Monitor field conditions and get simple irrigation recommendations.")

st.sidebar.header("Farm Settings")
crop = st.sidebar.selectbox("Select crop", ["Wheat", "Rice", "Tomato", "Sugarcane", "Cotton"])
auto_mode = st.sidebar.toggle("Automatic irrigation mode", value=False)

st.subheader("🌤️ Live Sensor Dashboard")
col1, col2, col3 = st.columns(3)

# Demo sensor readings; replace these with real IoT sensor readings when hardware is connected.
soil_moisture = random.randint(20, 80)
temperature = round(random.uniform(22, 38), 1)
humidity = random.randint(35, 85)

col1.metric("Soil Moisture", f"{soil_moisture}%", help="Demo value")
col2.metric("Temperature", f"{temperature} °C", help="Demo value")
col3.metric("Air Humidity", f"{humidity}%", help="Demo value")

st.caption(f"Last updated: {datetime.now().strftime('%d %b %Y, %I:%M:%S %p')}")

threshold = st.slider("Soil moisture threshold for irrigation (%)", 10, 70, 35)
irrigation_needed = soil_moisture < threshold

st.subheader("💧 Irrigation Status")
if irrigation_needed:
    st.warning("Soil moisture is below the selected threshold. Irrigation is recommended.")
    if auto_mode:
        st.success("Demo automatic mode: irrigation status is ON.")
    else:
        st.info("Automatic mode is OFF. Turn it on in the sidebar to see the demo ON status.")
else:
    st.success("Soil moisture is sufficient. Irrigation is not required right now.")

status = "ON (demo)" if (irrigation_needed and auto_mode) else "OFF"
st.metric("Pump Status", status)

st.subheader("📊 Sample Sensor History")
history = pd.DataFrame({
    "Reading": list(range(1, 11)),
    "Soil Moisture (%)": [random.randint(20, 80) for _ in range(10)],
    "Temperature (°C)": [round(random.uniform(22, 38), 1) for _ in range(10)],
})
st.line_chart(history.set_index("Reading"))

st.subheader("🌾 Crop Information")
crop_tips = {
    "Wheat": "Keep soil moisture consistent during germination and flowering.",
    "Rice": "Rice generally needs more water; avoid relying on this demo alone for field decisions.",
    "Tomato": "Avoid irregular watering; check soil moisture near the root zone.",
    "Sugarcane": "Monitor soil moisture regularly, especially during dry weather.",
    "Cotton": "Avoid waterlogging and check moisture during flowering and boll development."
}
st.write(crop_tips[crop])

st.info("This is a software demo using simulated sensor values. It does not connect to real sensors or control a physical water pump.")
