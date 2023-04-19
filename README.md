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

### Design
