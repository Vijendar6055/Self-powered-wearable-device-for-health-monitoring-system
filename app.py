import streamlit as st
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import joblib  # To load trained model

# ESP32 Web Server IP
ESP32_IP = "http://192.168.242.59"  # Change this to your ESP32's IP

# Load the trained disease prediction model
model = joblib.load(r"C:\New folder\data\random_forest_model.pkl")  # Ensure the model file is in the same directory

# Streamlit UI
st.set_page_config(page_title="Disease Prediction from Sensor Data", layout="wide")
st.title("🩺 Disease Prediction from Sensor Data")

# Tabs for user selection
tab1, tab2 = st.tabs(["📡 Live Sensor Data", "✏️ Manual Input"])

### 📡 TAB 1: Fetch Live Sensor Data ###
with tab1:
    st.subheader("📡 Real-Time Sensor Data")
    if st.button("Get Live Sensor Data"):
        with st.spinner("Fetching live data..."):
            try:
                # Request HTML content from ESP32
                response = requests.get(ESP32_IP, timeout=10)
                html_data = response.text

                # Parse HTML with BeautifulSoup
                soup = BeautifulSoup(html_data, "html.parser")

                # Extract all <p> elements containing sensor values
                paragraphs = soup.find_all("p")

                # Initialize sensor variables
                MPU6050_X, MPU6050_Y, MPU6050_Z, MQ135 = None, None, None, None

                # Loop through paragraphs to find sensor values
                for p in paragraphs:
                    text = p.get_text()

                    if "Acceleration" in text:
                        # Extract acceleration values using regex
                        accel_values = re.findall(r"[-+]?\d*\.\d+|\d+", text)  # Extract numbers
                        MPU6050_X, MPU6050_Y, MPU6050_Z = map(float, accel_values[:3])  # Convert to float

                    elif "MQ-135" in text:
                        MQ135 = int(re.search(r"\d+", text).group())  # Extract first integer found

                # Check if all values were successfully extracted
                if None in [MPU6050_X, MPU6050_Y, MPU6050_Z, MQ135]:
                    st.error("⚠️ Error: Could not extract all sensor values. Check the data format.")
                else:
                    # Display extracted sensor values
                    st.markdown(f"📡 **Live Sensor Data:**  \n"
                                f"🔹 MPU6050_X: **{MPU6050_X}**  \n"
                                f"🔹 MPU6050_Y: **{MPU6050_Y}**  \n"
                                f"🔹 MPU6050_Z: **{MPU6050_Z}**  \n"
                                f"🔹 MQ135: **{MQ135}**")

                    # Prepare data for prediction
                    sensor_data = pd.DataFrame([[MPU6050_X, MPU6050_Y, MPU6050_Z, MQ135]],
                                               columns=["MPU6050_X", "MPU6050_Y", "MPU6050_Z", "MQ135"])

                    # Predict disease
                    prediction = model.predict(sensor_data)[0]

                    # Display prediction result
                    st.success(f"💡 **Predicted Disease:** {prediction}")

            except requests.exceptions.Timeout:
                st.error("⚠️ Error: Connection to ESP32 timed out.")
            except requests.exceptions.ConnectionError:
                st.error("⚠️ Error: Could not connect to ESP32. Check if it's online.")
            except Exception as e:
                st.error(f"⚠️ Unexpected Error: {e}")

### ✏️ TAB 2: Manual Input for Prediction ###
with tab2:
    st.subheader("✏️ Enter Sensor Data Manually")

    # Manual input fields
    MPU6050_X = st.number_input("MPU6050_X", value=0.0, format="%.2f")
    MPU6050_Y = st.number_input("MPU6050_Y", value=0.0, format="%.2f")
    MPU6050_Z = st.number_input("MPU6050_Z", value=0.0, format="%.2f")
    MQ135 = st.number_input("MQ-135 Gas Sensor", value=0, step=1)

    # Predict based on manual input
    if st.button("Predict Disease"):
        input_data = pd.DataFrame([[MPU6050_X, MPU6050_Y, MPU6050_Z, MQ135]],
                                  columns=["MPU6050_X", "MPU6050_Y", "MPU6050_Z", "MQ135"])

        prediction = model.predict(input_data)[0]
        st.success(f"💡 **Predicted Disease:** {prediction}")
