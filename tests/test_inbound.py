import os
import sys
import json
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.messaging.inbound import process_message

OUTBOUND_QUEUE = "tsp.outbound"

class TestInboundProcess(unittest.TestCase):
    def test_process_message(self):
        # Define the input message
        input_message = {
            "locations": [[0, 0], [1, 1], [2, 2], [3, 3]],
        }
        input_message_json = json.dumps(input_message)

        # Define the expected output message
        expected_output_message = {
            "locations": [[0, 0], [1, 1], [2, 2], [3, 3]],
            "path": [[0, 0], [3, 3], [2, 2], [1, 1], [0, 0]],
        }
        expected_output_message_json = json.dumps(expected_output_message)


        # Call the function with the input message
        output_message = process_message(input_message_json)

        self.assertEqual(output_message, expected_output_message_json)
