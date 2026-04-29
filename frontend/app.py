import streamlit as st
import requests
import pandas as pd
import time
API = "http://localhost:8000"
st.set_page_config(
    layout="wide",
    page_title="AI SOC Dashboard",
    page_icon="🛡️"
)
st.markdown("## 🛡️ AI SOC Dashboard")
st.caption("Real-time anomaly detection + AI threat analysis")
if "data" not in st.session_state:
    st.session_state.data = None
if "last_run" not in st.session_state:
    st.session_state.last_run = None
st.sidebar.title("⚙️ Controls")
auto_refresh = st.sidebar.checkbox("Auto Refresh (5s)")
run_btn = st.sidebar.button("Run Analysis")
def fetch_data():
    try:
        res = requests.get(f"{API}/analyze", timeout=10)
        if res.status_code != 200:
            st.sidebar.error("API Error")
            return None
        data = res.json()
        return data.get("alerts", [])
    except requests.exceptions.ConnectionError:
        st.sidebar.error("Backend not reachable")
        return None
    except Exception as e:
        st.sidebar.error(f"Error: {str(e)}")
        return None
if run_btn:
    st.session_state.data = fetch_data()
    st.session_state.last_run = time.strftime("%H:%M:%S")
if auto_refresh:
    st.session_state.data = fetch_data()
    st.session_state.last_run = time.strftime("%H:%M:%S")
    time.sleep(5)
    st.rerun()
data = st.session_state.data
if not data:
    st.info("Click 'Run Analysis' to start")
    st.stop()
df = pd.DataFrame(data)
st.subheader("📊 System Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Logs", len(df))
col2.metric("High Alerts", len(df[df["severity"] == "High"]))
col3.metric("Critical Alerts", len(df[df["severity"] == "Critical"]))
col4.metric("Last Run", st.session_state.last_run or "-")
st.subheader("📈 Severity Distribution")
severity_counts = df["severity"].value_counts()
st.bar_chart(severity_counts)
st.subheader("🔍 Filter Alerts")
selected = st.multiselect(
    "Select Severity",
    options=df["severity"].unique(),
    default=df["severity"].unique()
)
filtered_df = df[df["severity"].isin(selected)]
st.subheader("📋 Alerts Table")
st.dataframe(filtered_df[["severity", "rules"]], use_container_width=True)
st.subheader("🚨 Critical & High Alerts")
for item in data:
    if item["severity"] in ["High", "Critical"]:
        color = "red" if item["severity"] == "Critical" else "orange"
        with st.container():
            st.markdown(f"### 🔥 :{color}[{item['severity']} Alert]")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.json(item["log"])
            with col2:
                st.markdown("**Explanation:**")
                st.write(item.get("explanation", "No explanation available"))
            st.divider()