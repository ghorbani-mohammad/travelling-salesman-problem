import json

from src.solver.tsp_solver import optimize_tsp


# Define a function to handle incoming messages
def process_message(body):
    # Convert the message payload to a Python object
    payload = json.loads(body)

    # Extract the locations from the payload
    locations = payload["locations"]

    # Solve the TSP problem
    solution = optimize_tsp(locations)

    # Prepare the message payload for the outbound queue
    outbound_payload = {
        "locations": locations,
        "path": solution,
    }

    # Convert the payload to a JSON string
    result = json.dumps(outbound_payload)

    return result
