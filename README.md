# Analyse de donnees de collision routiere de la ville de Montreal

Petit projet maison pour apprendre l'analyse de donnne avec 
Python, base sur des Open-Data fournis par la ville de Montreal.

# Quickstart

We're going to install and configure the latest develop build of this API.

## Clone the project

First of all, you need to clone the project on your computer with :

```
git clone https://github.com/jnoel7/Collisions_routieres_Mtl.git
```

## Create a virtual environment

[Virtualenv](https://virtualenv.pypa.io/) provides an isolated Python environment, which are more practical than installing packages system-wide. They also allow packages to be installed without administrator privileges.

1. Create a new virtual environment
```
virtualenv env
```

2. Activate the virtual environment
```
. env/bin/activate
```

You need to ensure the virtual environment is active each time you want to launch the project.

## Install all requirements

Your OS will need SQLite3 (<3.26) for unit testing.

Requirements of the project are stored in the `requirements.txt` file.
Requirements for development related actions are stored in the `requirements-dev.txt` file.
You can install them with:

**WARNING** : Make sure your virtual environment is active or you will install the packages system-wide.
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Launch the script

```
python ./src/main.py
```
