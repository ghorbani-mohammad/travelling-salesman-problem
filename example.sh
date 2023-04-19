#!/bin/bash

# Start the services
docker-compose up -d

# Send a message to the inbound channel and see the result from outbound channel
docker exec -it app bash -c "python src/runner.py [[0,0],[1,1]]"