import numpy as np
from models.monte_carlo import MonteCarlo

class TestMonteCarlo:
    def test_simulation_shape(self):
        fcf = np.array([100, 110, 120])
        results = MonteCarlo.simulate(fcf, iterations=100)
        assert len(results['ci_90']) == 2
        assert results['mean'] > 0