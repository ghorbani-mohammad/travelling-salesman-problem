import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.messaging.outbound import process_message


class TestOutboundProcess(unittest.TestCase):
    def test_process_message(self):
        # Define the input message message
        message = b'This is a message'
        
        # Define the expected output message
        expected_output_message = b'This is a message'

        # Call the function with the input message
        output_message = process_message(message)
        
        self.assertEqual(expected_output_message, output_message)