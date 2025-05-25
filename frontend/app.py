import streamlit as st
import requests

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="Weather App", page_icon="⛅", layout="centered")
st.title("🌤️ Weather App")
st.markdown("---")
st.markdown("✌️**Built by Anand Reddy**")
with st.expander("ℹ️ About PM Accelerator"):
    st.markdown(
        """
        **PM Accelerator** is a career-launching program designed for aspiring Product Managers and Software Engineers.
        
        It offers:
        - Hands-on technical assessments
        - Project-based learning
        - Portfolio-ready experiences
        - Opportunities to work with real mentors and hiring partners
        
        🔗 [Visit PM Accelerator on LinkedIn](https://www.linkedin.com/school/pmaccelerator/)
        """
    )
st.markdown("---")

with st.sidebar:
    location = st.text_input("📍 Enter a location", "Hyderabad")

tabs = st.tabs(["Current Weather", "5-Day Forecast", "Saved History"])

with tabs[0]:
    st.subheader("Current Weather")
    if st.button("Fetch Weather"):
        res = requests.get(f"{API_BASE}/weather/live/{location}")
        if res.ok:
            data = res.json()
            st.metric("Temperature", f"{data['temperature']} °C")
            st.write(f"📍 Location: {data['location']}")
            st.write(f"☁️ Condition: {data['condition']}")
            st.write(f"💧 Humidity: {data['humidity']}%")
            st.write(f"🌬️ Wind Speed: {data['wind_speed']} m/s")
        else:
            st.error("Could not fetch weather for the location.")

    if st.button("Save Weather"):
        res = requests.post(f"{API_BASE}/weather/save/{location}")
        if res.ok:
            st.success("Saved successfully.")
        else:
            st.error("Failed to save.")

with tabs[1]:
    st.subheader("5-Day Forecast")
    res = requests.get(f"{API_BASE}/weather/forecast/{location}")
    if res.ok:
        for day in res.json():
            st.markdown(f"**{day['date']}**")
            st.write(f"🌡️ Avg Temp: {day['avg_temp']} °C")
            st.write(f"⛅ Condition: {day['common_condition']}")
            st.divider()
    else:
        st.error("Could not fetch forecast.")

with tabs[2]:
    st.subheader("🫣 Saved Weather History")
    res = requests.get(f"{API_BASE}/weather/history/")
    if res.ok:
        records = res.json()
        if not records:
            st.info("No records yet.")
        for r in records:
            with st.expander(f"{r['location']} - {r['temperature']} °C"):
                st.caption(r["timestamp"])
                new_loc = st.text_input("Update location", r["location"], key=f"loc_{r['id']}")
                cols = st.columns(2)
                if cols[0].button(" Update", key=f"u_{r['id']}"):
                    update = requests.put(f"{API_BASE}/weather/update/{r['id']}?new_location={new_loc}")
                    st.success("Updated!" if update.ok else "Failed.")
                if cols[1].button(" Delete", key=f"d_{r['id']}"):
                    delete = requests.delete(f"{API_BASE}/weather/delete/{r['id']}")
                    st.success("Deleted!" if delete.ok else "Failed.")
    else:
        st.error("Could not load saved data.")
