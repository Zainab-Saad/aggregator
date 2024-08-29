## Aggregator for FL integration to kepler model server

To run the project create a virtual env and install the dependencies listed in the `pyproject.toml` file
```
python3 -m venv venv
```
Check into the created env named `venv` and install dependencies
```
source venv/bin/activate && pip install .
```
Run 
```
python3 server.py
```
to start the FL server; clients are started from the `kepler-model-server/src/kepler_model/federated_learning`

Check out of the venv using
```
deactivate
```

Note: on ubuntu virtualenv can be installed using `sudo apt install python3.10-venv`; otherwise on other systems `python3 -m pip install virtualenv` works (this wont work on ubuntu)