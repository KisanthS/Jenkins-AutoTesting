import logging
import pytest
import time
from app.calculator import Calculator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def log_and_assert(self, operation, result, expected, test_name):
        logger.info(f"{test_name}: {operation} = <b>{result}</b>")
        assert result == expected, f"Expected {test_name} to be {expected}, but got {result}"

    def test_add(self):
        a, b = 1, 2
        start_time = time.time()  # Start timer
        logger.info(f"Testing addition: <b>{a}</b> + <b>{b}</b>")
        result = self.calc.add(a, b)
        logger.info(f"Addition: <b>{a}</b> + <b>{b}</b> = <b>{result}</b>")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nAddition took <b>{end_time - start_time:.4f}</b> seconds\n")  # Space after the log
        self.log_and_assert(f"{a} + {b}", result, 3, "Addition")

    def test_subtract(self):
        a, b = 5, 2
        start_time = time.time()  # Start timer
        logger.info(f"Testing subtraction: <b>{a}</b> - <b>{b}</b>")
        result = self.calc.subtract(a, b)
        logger.info(f"Subtraction: <b>{a}</b> - <b>{b}</b> = <b>{result}</b>")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nSubtraction took <b>{end_time - start_time:.4f}</b> seconds\n")  # Space after the log
        self.log_and_assert(f"{a} - {b}", result, 3, "Subtraction")

    def test_multiply(self):
        a, b = 2, 3
        start_time = time.time()  # Start timer
        logger.info(f"Testing multiplication: <b>{a}</b> * <b>{b}</b>")
        result = self.calc.multiply(a, b)
        logger.info(f"Multiplication: <b>{a}</b> * <b>{b}</b> = <b>{result}</b>")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nMultiplication took <b>{end_time - start_time:.4f}</b> seconds\n")  # Space after the log
        self.log_and_assert(f"{a} * {b}", result, 6, "Multiplication")

    def test_divide(self):
        a, b = 10, 2
        start_time = time.time()  # Start timer
        logger.info(f"Testing division: <b>{a}</b> / <b>{b}</b>")
        result = self.calc.divide(a, b)
        logger.info(f"Division: <b>{a}</b> / <b>{b}</b> = <b>{result}</b>")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nDivision took <b>{end_time - start_time:.4f}</b> seconds\n")  # Space after the log
        self.log_and_assert(f"{a} / {b}", result, 5, "Division")

    def test_divide_by_zero(self):
        a, b = 1, 0
        logger.info(f"Testing divide by zero: <b>{a}</b> / <b>{b}</b>")
        start_time = time.time()  # Start timer
        try:
            self.calc.divide(a, b)
        except ValueError as e:
            end_time = time.time()  # End timer
            logger.info(f"\nDivide by zero test took <b>{end_time - start_time:.4f}</b> seconds\n")  # Space after the log
            logger.info(f"Expected error: <b>{str(e)}</b>")
            # Assert that the exception was indeed raised
            assert str(e) == "Cannot divide by zero"
