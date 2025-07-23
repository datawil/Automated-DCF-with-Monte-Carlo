import numpy as np
from .dcf import DCFModel

class MonteCarlo:
    @staticmethod
    def simulate(fcf, iterations=1000):
        results = []
        for _ in range(iterations):
            sim_fcf = np.random.normal(np.mean(fcf), np.std(fcf), 3)
            results.append(DCFModel.calculate(sim_fcf, 0.08))
            
        return {
            "mean": np.mean(results),
            "median": np.median(results),
            "ci_90": list(np.percentile(results, [5, 95]))
        }
