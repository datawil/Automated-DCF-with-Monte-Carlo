# Step 1 Data Collection

import yfinance as yf
ticker = yf.Ticker("AAPL")
cash_flows = ticker.cashflow  # Get 5 years of cash flows


# Step 2 Build DCF Logic

import numpy as np
from numpy_financial import npv

# Sample cash flow data
fcf = np.array([100, 110, 120])

# Define your DCF function

def dcf_valuation(fcf, wacc=0.08, terminal_growth=0.02):
    terminal_value = fcf[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    all_cash_flows = np.append(fcf, terminal_value)
    return npv(wacc, all_cash_flows)

# Monte Carlo Simulation

def monte_carlo_dcf(fcf_mean, fcf_std, iterations=1000):
    simulations = []
    for _ in range(iterations):
        simulated_fcf = np.random.normal(fcf_mean, fcf_std, size=5)  # 5-year projection
        simulations.append(dcf_valuation(simulated_fcf))
    return np.percentile(simulations, [5, 50, 95])  # 90% CI


# Step 3 Dash Dashboard

import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Slider(id="wacc-slider", min=0.05, max=0.15, step=0.01, value=0.08),
    dcc.Graph(id="dcf-plot")
])

@app.callback(Output("dcf-plot", "figure"), Input("wacc-slider", "value"))
def update_graph(wacc):
    valuation = dcf_valuation(fcf, wacc)
    return px.bar(x=["DCF Value"], y=[valuation], title=f"Enterprise Value: ${valuation:,.2f}")

app.run(mode='inline')

