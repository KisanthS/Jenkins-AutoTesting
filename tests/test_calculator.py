import logging
import pytest
from app.calculator import Calculator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        a, b = 1, 2
        result = self.calc.add(a, b)
        logger.info(f"Testing addition: {a} + {b} = {result}")
        assert result == 3

    def test_subtract(self):
        a, b = 5, 2
        result = self.calc.subtract(a, b)
        logger.info(f"Testing subtraction: {a} - {b} = {result}")
        assert result == 3

    def test_multiply(self):
        a, b = 2, 3
        result = self.calc.multiply(a, b)
        logger.info(f"Testing multiplication: {a} * {b} = {result}")
        assert result == 6

    def test_divide(self):
        a, b = 10, 2
        result = self.calc.divide(a, b)
        logger.info(f"Testing division: {a} / {b} = {result}")
        assert result == 5

    def test_divide_by_zero(self):
        a, b = 1, 0
        logger.info(f"Testing divide by zero: {a} / {b}")
        with pytest.raises(ValueError):
            self.calc.divide(a, b)
