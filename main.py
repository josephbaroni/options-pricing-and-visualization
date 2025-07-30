import streamlit as st
import numpy as np
import plotly.graph_objects as go
from options_pricing import black_scholes_price, greeks

st.title("Options Pricing Visualizer")

st.sidebar.header("Input Parameters")

S = st.sidebar.number_input("Asset Price (S)", value=100.0)
K = st.sidebar.number_input("Strike Price (K)", value=100.0)
tau = st.sidebar.slider("Time to Maturity (years)", min_value=0.01, max_value=2.0, value=1.0, step=0.01)
r = st.sidebar.slider("Risk-Free Rate (%)", min_value=0.0, max_value=10.0, value=2.0) / 100
sigma = st.sidebar.slider("Volatility (%)", min_value=1.0, max_value=100.0, value=20.0) / 100
option_type = st.sidebar.selectbox("Option Type", ["call", "put"])

price = black_scholes_price(S, K, tau, r, sigma, option_type)
greek_vals = greeks(S, K, tau, r, sigma, option_type)

st.metric("Option Price", f"${price:.2f}")

st.subheader("Option Greeks")
for key, val in greek_vals.items():
    st.write(f"**{key}**: {val:.4f}")

# 3D plot

st.subheader("Price vs Spot and Volatility")

spot_range = np.linspace(S * 0.5, S * 1.5, 30)
vol_range = np.linspace(0.01, 0.8, 30)
spot_grid, vol_grid = np.meshgrid(spot_range, vol_range)

price_grid = np.array([
    [black_scholes_price(s, K, tau, r, v, option_type) for s in spot_range]
    for v in vol_range
])

fig = go.Figure(data=[go.Surface(
    z=price_grid, x=spot_range, y=vol_range,
    colorscale='Viridis'
)])
fig.update_layout(
    scene=dict(
        xaxis_title='Asset Price',
        yaxis_title='Volatility',
        zaxis_title='Option Price'
    ),
    width=700,
    margin=dict(r=20, b=10, l=10, t=10)
)
st.plotly_chart(fig)
