# Smart Agriculture Automation System

A simple Streamlit demo that displays simulated soil moisture, temperature, and humidity readings and provides an irrigation recommendation.

## Files
- `app.py` — main Streamlit application
- `requirements.txt` — Python packages required
- `README.md` — project description and run instructions

## Run locally
1. Install Python 3.9 or later.
2. Open a terminal in this project folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Important
This project uses simulated sensor values. It does not read actual IoT sensors or control a real pump. Real hardware integration requires compatible sensors, a controller, and appropriate electrical safety measures.
