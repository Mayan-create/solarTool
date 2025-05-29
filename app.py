
import streamlit as st
from rooftop_segmentation import detect_rooftop
from solar_estimator import estimate_solar_potential
from PIL import Image
import numpy as np

st.set_page_config(page_title="Solar Rooftop Analyzer", layout="centered")

st.title("☀️ AI-powered Rooftop Solar Potential Analyzer")
st.markdown("Upload a satellite image of a building rooftop to assess its solar installation potential.")

uploaded_file = st.file_uploader("sample image.png", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Detecting rooftop..."):
        rooftop_mask = detect_rooftop(np.array(image))

    st.image(rooftop_mask, caption="Detected Rooftop Area", use_container_width=True)

    with st.spinner("Estimating solar potential..."):
        result = estimate_solar_potential(rooftop_mask)

    st.success("Solar Analysis Completed!")
    st.metric("Estimated Usable Area (sq. m)", f"{result['usable_area']:.2f}")
    st.metric("Estimated System Size (kW)", f"{result['system_size_kw']:.2f}")
    st.metric("Estimated Annual Output (kWh)", f"{result['annual_output_kwh']:.0f}")
    st.metric("Estimated ROI (years)", f"{result['roi_years']:.1f}")
