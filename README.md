# Udemy Flask REST API - My Code

[Tutorial link](https://www.udemy.com/course/rest-api-flask-and-python)

## Tutorial Sections
- [Section3](https://github.com/mpearso3/udemy_flask_rest_api/section_3)
  - Overview: First REST API
- [Section5](https://github.com/mpearso3/udemy_flask_rest_api/section_5)
  - Overview: Storing resources in a SQL database

## Tools (See Install Guide for details)
1. Flask - Python web framework
2. Python 3.5+
3. REST
4. Postman - API visualization and testing application
  [Postman](https://web.postman.co)

## Install Guide:
- Install vim: `sudo apt install vim`
- Setup bashrc and vimrc from my [Github gists](https://gist.github.com/mpearso3/56e607e1f95a3f2b26401a16ab9cdaaa)
- Install pip (package manager for installing python libraries)
  - `sudo apt install python3-pip`
- Install git: `sudo apt install git`
- Install virtualenv for building virtual environments
  - `pip3 install virtualenv`
- Create virtual environment with python3.6 (3.5 seems to be obsolete, using 3.6 and it's working fine)
  - `virtualenv venv --python=python3.6`
- Activate the virtual environment (run this command in the same location as the previous command)
  - `source venv/bin/activate`
  - You can leave the virtual environment using:
    - `deactivate`
- Inside the virtual environment, install Flask, Flask-RESTful, and Flask-JWT
  - `pip install Flask`
  - `pip install Flask-RESTful`
  - `pip install Flask-JWT`
