import streamlit as st

st.set_page_config(page_title="About", layout="centered")

# Safe CSS styling (only minimal customization allowed)
st.markdown("""
    <style>
        .about-box {
            padding: 1.5rem;
            background-color: #f9f9f9;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .section-title {
            color: #2e7d32;
            font-size: 1.2rem;
            margin-top: 1.5rem;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            color: gray;
            font-size: 0.85rem;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; '>ℹ️ About</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='about-box'>

<p>The <strong>Harumanis Vegetative Stage Soil Fertility Predictor</strong> uses a trained <em>Random Forest Classifier</em> to assess soil fertility based on five key agricultural indicators:</p>

<p class='section-title'>🌿 Input Parameters</p>
<ul>
    <li>Nitrogen (N)</li>
    <li>Phosphorus (P)</li>
    <li>Potassium (K)</li>
    <li>Temperature (°C)</li>
    <li>Humidity (%)</li>
</ul>

<p class='section-title'>🎯 Purpose</p>
<p>
This tool is built for <strong>educational and research purposes</strong> at the Faculty of Computer Science, 
<br><strong>MARA University of Technology (UiTM) – Arau Campus</strong>.
</p>

<p class='section-title'>🌱 Benefits</p>
<p>
It assists farmers and researchers in enhancing <strong>Harumanis mango</strong> production using smart, data-driven insights.
</p>

</div>

<div class='footer'>
    © 2025 Harumanis Soil Intelligence System · All rights reserved.
</div>
""", unsafe_allow_html=True)
