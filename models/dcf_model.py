import numpy as np
from numpy_financial import npv

class DCFModel:
    @staticmethod
    def calculate(fcf, wacc, growth=0.02):
        """Your original DCF logic with validation"""
        if wacc <= growth:
            raise ValueError("WACC must exceed growth rate")
            
        terminal = fcf[-1] * (1 + growth) / (wacc - growth)
        return npv(wacc, np.append(fcf, terminal))