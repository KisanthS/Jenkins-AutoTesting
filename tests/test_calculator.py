import logging
import pytest
from app.calculator import Calculator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        logger.info("Testing addition")
        assert self.calc.add(1, 2) == 3

    def test_subtract(self):
        logger.info("Testing subtraction")
        assert self.calc.subtract(5, 2) == 3

    def test_multiply(self):
        logger.info("Testing multiplication")
        assert self.calc.multiply(2, 3) == 6

    def test_divide(self):
        logger.info("Testing division")
        assert self.calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        logger.info("Testing divide by zero")
        with pytest.raises(ValueError):
            self.calc.divide(1, 0)
