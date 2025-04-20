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
        result = self.calc.add(1, 2)
        logger.info(f"Addition Result: {result}")
        assert result == 3, f"Expected 3 but got {result}"

    def test_subtract(self):
        logger.info("Testing subtraction")
        result = self.calc.subtract(5, 2)
        logger.info(f"Subtraction Result: {result}")
        assert result == 3, f"Expected 3 but got {result}"

    def test_multiply(self):
        logger.info("Testing multiplication")
        result = self.calc.multiply(2, 3)
        logger.info(f"Multiplication Result: {result}")
        assert result == 6, f"Expected 6 but got {result}"

    def test_divide(self):
        logger.info("Testing division")
        result = self.calc.divide(10, 2)
        logger.info(f"Division Result: {result}")
        assert result == 5, f"Expected 5 but got {result}"

    def test_divide_by_zero(self):
        logger.info("Testing divide by zero")
        with pytest.raises(ValueError):
            self.calc.divide(1, 0)
