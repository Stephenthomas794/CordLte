from flask import Flask

app = Flask(__name__)

from mainApp import projects
from mainApp.projects.project1 import project1_blueprint_factory
