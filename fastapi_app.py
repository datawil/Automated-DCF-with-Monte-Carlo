from fastapi import FastAPI
import numpy as np
from numpy_financial import npv

app = FastAPI()

# Reuse your DCF function (or import from dcf_dash.py)
def dcf_valuation(fcf, wacc=0.08, terminal_growth=0.02):
    terminal_value = fcf[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    return npv(wacc, np.append(fcf, terminal_value))

# API Endpoint
@app.get("/dcf")
def get_dcf(wacc: float = 0.08):
    fcf = np.array([100, 110, 120])  # Replace with your data
    return {"valuation": dcf_valuation(fcf, wacc)}