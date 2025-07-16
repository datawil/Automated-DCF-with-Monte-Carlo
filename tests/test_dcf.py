import pytest
import numpy as np
from models.dcf import DCFModel

class TestDCFModel:
    def test_basic_valuation(self):
        fcf = np.array([100, 110, 120])
        result = DCFModel.calculate(fcf, 0.08)
        assert isinstance(result, float)
        assert result > 0

    def test_invalid_wacc(self):
        with pytest.raises(ValueError):
            DCFModel.calculate(np.array([100, 110]), 0.02, 0.03)  # WACC < growth