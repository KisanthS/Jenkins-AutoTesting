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
        logger.info(f"{test_name}: {operation} = {result}")
        assert result == expected, f"Expected {test_name} to be {expected}, but got {result}"

    def test_add(self):
        a, b = 1, 2
        start_time = time.time()  # Start timer
        logger.info(f"Testing addition: {a} + {b}")
        result = self.calc.add(a, b)
        logger.info(f"Addition: {a} + {b} = {result}")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nAddition took {end_time - start_time:.4f} seconds\n")  # Added newline for spacing
        self.log_and_assert(f"{a} + {b}", result, 3, "Addition")

    def test_subtract(self):
        a, b = 5, 2
        start_time = time.time()  # Start timer
        logger.info(f"Testing subtraction: {a} - {b}")
        result = self.calc.subtract(a, b)
        logger.info(f"Subtraction: {a} - {b} = {result}")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nSubtraction took {end_time - start_time:.4f} seconds\n")  # Added newline for spacing
        self.log_and_assert(f"{a} - {b}", result, 3, "Subtraction")

    def test_multiply(self):
        a, b = 2, 3
        start_time = time.time()  # Start timer
        logger.info(f"Testing multiplication: {a} * {b}")
        result = self.calc.multiply(a, b)
        logger.info(f"Multiplication: {a} * {b} = {result}")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nMultiplication took {end_time - start_time:.4f} seconds\n")  # Added newline for spacing
        self.log_and_assert(f"{a} * {b}", result, 6, "Multiplication")

    def test_divide(self):
        a, b = 10, 2
        start_time = time.time()  # Start timer
        logger.info(f"Testing division: {a} / {b}")
        result = self.calc.divide(a, b)
        logger.info(f"Division: {a} / {b} = {result}")  # Log the result clearly
        end_time = time.time()  # End timer
        logger.info(f"\nDivision took {end_time - start_time:.4f} seconds\n")  # Added newline for spacing
        self.log_and_assert(f"{a} / {b}", result, 5, "Division")

    def test_divide_by_zero(self):
        a, b = 1, 0
        logger.info(f"Testing divide by zero: {a} / {b}")
        start_time = time.time()  # Start timer
        try:
            self.calc.divide(a, b)
        except ValueError as e:
            end_time = time.time()  # End timer
            logger.info(f"\nDivide by zero test took {end_time - start_time:.4f} seconds\n")  # Added newline for spacing
            logger.info(f"Expected error: {str(e)}")
            # Assert that the exception was indeed raised
            assert str(e) == "Cannot divide by zero"
