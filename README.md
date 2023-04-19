## The TSP solver

### Structure
Main directory which has the code of project is src. You can see the structure of it in below.
```
src
 ┣ messaging
 ┃ ┣ inbound.py
 ┃ ┣ outbound.py
 ┃ ┗ __init__.py
 ┣ solver
 ┃ ┣ tsp_solver.py
 ┃ ┗ __init__.py
 ┣ utils
 ┃ ┣ distance.py
 ┃ ┗ __init__.py
 ┣ config.py
 ┣ main.py
 ┗ __init__.py
```
- In the inbound and outbound modules I've put related processing when we have a income message and when we have a outbound message.
- In the tsp_solver, I've put codes which used the or-tools package to solve the problem.
- In the distance, I have a function which I've used to calculate euclidean-distance.
- In the config, I've loaded environment variables and logging config has been set.
- And finally, in the main I've connected to the inbound and outbound channel and do calling the related processing functions.

There is another directory named ci, which I've used to check code qualities and running tests. It has its own requirements file so you don't need to install it where they are not beneficial like image. It can be used in the PR section to check quality before reviewing a PR.
```
ci
 ┣ find-python.sh
 ┣ format-python.sh
 ┣ lint-python-one.sh
 ┣ lint-python.sh
 ┣ requirements.txt
 ┗ test-python.sh
```

### Notes
- Before starting don't forget to add a .env file.
- For this mini project, I've used rabbitmq as a message broker.
- I have used docker-compose fo simplify the deploy and running of the project.
- I have add four unit tests for basic functions that I had.
- For easily run the project and check the output I've provided an example.sh file which you
can change the input and see the result.
- I have used black formatter and pylint to improve the quality of the code.
- You can change the level of logging in the .env file and see the logs in the app.log file.
- You can run tests using `make test`.
- You can run formatter using `make format`.
- You can run linter using `make lint`.

### Design
- So we have message broker and app containers.
- The app will subscribe to the inbound channel and processes incoming messages.
- Result messages will be published to the outbound channel. 
- input messages should be like this, an array of locations:
  `[[0,0], [1,2]]`
- output messages would be like this:
  `{"locations": [[0, 0], [1, 1]], "path": [[0, 0], [1, 1], [0, 0]]}`