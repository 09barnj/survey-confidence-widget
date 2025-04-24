import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def calculate_margin_of_error(sample_size, population_size, confidence_level=0.95):
    z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
    z = z_scores[confidence_level]
    p = 0.5  # maximum variability (most conservative estimate)
    moe = z * np.sqrt((p * (1 - p)) / sample_size) * np.sqrt((population_size - sample_size) / (population_size - 1))
    return moe * 100  # convert to percentage

st.title("Survey Confidence Calculator")

# Inputs
population_size = st.number_input("Total Tickets Sold (Population Size)", min_value=1000, value=336000, step=1000)
sample_size = st.number_input("Survey Responses (Sample Size)", min_value=10, value=12074, step=10)

# Fixed confidence level at 95%
confidence_level = 0.95

# Calculate Margin of Error
moe = calculate_margin_of_error(sample_size, population_size, confidence_level)
st.markdown(f"### Margin of Error: {moe:.2f}% at 95% confidence")

# Diminishing Returns Graph
sample_range = np.arange(100, min(population_size, 15000), 100)
margins = [calculate_margin_of_error(n, population_size, confidence_level) for n in sample_range]

st.markdown("### Margin of Error vs. Sample Size")
fig, ax = plt.subplots()
ax.plot(sample_range, margins, marker='o', label="Margin of Error")
ax.axhline(y=5, color='red', linestyle='--', label="5% Standard")
ax.set_xlabel("Sample Size (Responses)")
ax.set_ylabel("Margin of Error (%)")
ax.set_title("Diminishing Returns of More Responses")
ax.grid(True)
ax.legend()
st.pyplot(fig)

st.caption("This widget helps demonstrate that beyond a certain sample size, additional responses make minimal impact on accuracy.")
