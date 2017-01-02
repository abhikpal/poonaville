# Readme

## Setting up the development environment

*Poonaville* is a Flask based Python app that uses web sockets for real time
game updates. To set up a development environment, make sure that `pip`
and `virtualenv` are installed on the target system.

The use the following commands to setup the development environment

```bash
# clone the repo
git clone 'https://github.com/abhikpal/poonaville/'

# create a new virtualenv for poonaville
virtualenv -p python3 venv

# activate the virtualenv
source venv/bin/activate

# change to the source code directory and install all required libraires
cd poonaville
pip install -r requirements.txt

# create the database
python application.py createdb

# initialize the database with required values
python application.py initdb

# run the server
python applicaiton.py start
```

## Usage

The Flask app starts a webserver on 0.0.0.0:5000.

* Users can view the controller by going to `http://0.0.0.0:5000/` through
their devices. Replace the `0.0.0.0` with the IP address of the machine the
game is running on (on \*nix machines, use `ip addr show` to view the IP
address).

* The main game screen -- the projection -- is broadcasted on
`http://127.0.0.1:5000/projection/`. This should ideally be accessed on the
machine acting as the server.


