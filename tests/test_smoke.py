import inspect
import unittest

from src import task

FUNCTION_NAME = "clamp"
PARAMETERS = ("value", "minimum", "maximum")


class BaselineSmokeTests(unittest.TestCase):
    def test_function_and_signature(self):
        function = getattr(task, FUNCTION_NAME)
        self.assertTrue(callable(function))
        self.assertEqual(
            tuple(inspect.signature(function).parameters),
            PARAMETERS,
        )