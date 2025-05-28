import streamlit as st
import joblib
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Harumanis Model Performance", layout="wide")

# Custom CSS for compact layout
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-size: 14px !important;
        }
        h1 {
            color: #2e7d32;
            text-align: center;
            margin-bottom: 0.3rem;
        }
        .metric-label {
            font-weight: bold;
            font-size: 1rem;
            color: #4caf50;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 0.4em 1.2em;
            border-radius: 6px;
            margin-top: 0.5rem;
        }
        .stButton>button:hover {
            background-color: #388e3c;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 Model Performance Dashboard")
# 🔎 Short description
st.markdown("""
<p style="text-align: center; color: #555;">
    This dashboard displays the performance of the Harumanis Soil Fertility Prediction model using test data. 
    It includes key evaluation metrics, a confusion matrix, and feature importance to help you understand how well the model performs.
</p>
""", unsafe_allow_html=True)
# Sample test data
X_test = np.array([
    [12, 7, 9, 27.0, 78],
    [25, 20, 18, 30.5, 65],
    [14, 9, 10, 28.0, 72],
    [10, 5, 8, 27.5, 80],
    [20, 15, 10, 29.0, 70],
    [30, 25, 20, 31.5, 60],
    [15, 10, 12, 28.5, 75]
])
y_test = [1, 0, 1, 1, 1, 0, 1]
y_pred = model.predict(X_test)

# Metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

# Compact and clean HTML table
st.subheader("📋 Performance Metrics")
st.markdown(f"""
    <style>
        .compact-metrics-table {{
            width: 100%;
            font-size: 14px;
            border-collapse: collapse;
            margin: 0 auto 1rem auto;
        }}
        .compact-metrics-table th, .compact-metrics-table td {{
            border: 1px solid #ddd;
            padding: 4px 8px;
            text-align: center;
        }}
        .compact-metrics-table th {{
            background-color: #4CAF50;
            color: white;
        }}
        .compact-metrics-table tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
    <table class="compact-metrics-table">
        <thead>
            <tr>
                <th>Metric</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Accuracy</td>
                <td>{acc:.2f}</td>
            </tr>
            <tr>
                <td>Precision</td>
                <td>{prec:.2f}</td>
            </tr>
            <tr>
                <td>Recall</td>
                <td>{rec:.2f}</td>
            </tr>
            <tr>
                <td>F1 Score</td>
                <td>{f1:.2f}</td>
            </tr>
        </tbody>
    </table>
""", unsafe_allow_html=True)


# Confusion Matrix + Feature Importance side by side
col5, col6 = st.columns(2)

with col5:
    st.subheader("🧮 Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6.0, 3))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Greens", xticklabels=['Not Fertile', 'Fertile'], yticklabels=['Not Fertile', 'Fertile'], ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig, use_container_width=True)

with col6:
    st.subheader("🔍 Feature Importance")
    features = ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)', 'Temperature', 'Humidity']
    importances = model.feature_importances_
    fig2, ax2 = plt.subplots(figsize=(4.5, 3))
    sns.barplot(x=importances, y=features, palette="Greens_r", ax=ax2)
    ax2.set_xlabel("Importance Score")
    st.pyplot(fig2, use_container_width=True)

# Footer
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.8em; margin-top: 1rem;'>
        © 2025 Harumanis Soil Intelligence System · Model evaluation dashboard
    </div>
""", unsafe_allow_html=True)
