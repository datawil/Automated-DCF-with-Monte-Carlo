from fastapi import FastAPI, HTTPException
from fastapi_cache.decorator import cache
from models.dcf_model import DCFModel
from models.monte_carlo import MonteCarlo
from cache_config import setup_caching
import yfinance as yf

# Initialize app
app = FastAPI(title="DCF Valuation API")

# Setup caching on startup
@app.on_event("startup")
async def startup_event():
    setup_caching()

# Main endpoint
@app.get("/dcf/{ticker}")
@cache(expire=1800)  # Cache for 30 minutes specifically
async def calculate_dcf(ticker: str, wacc: float = 0.08):
    """
    Returns DCF valuation with Monte Carlo simulation
    """
    try:
        stock = yf.Ticker(ticker)
        fcf = stock.cashflow.loc['Free Cash Flow'].values[-3:]
        
        return {
            "dcf": DCFModel.calculate(fcf, wacc),
            "monte_carlo": MonteCarlo.simulate(fcf),
            "cache_hit": False  # Would be True if cached
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Render optimization - allows running via `python api/fastapi_app.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)