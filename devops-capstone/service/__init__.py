"""
Package: service
Package for the application models and service routes
This module creates and configures the Flask app and sets up
the logging and SQL database
"""
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_cors import CORS

# Create the Flask aoo
app = Flask(__name__)

# Import the configuration
app.config.from_object("service.config")

# Set up Talisman for security headers
talisman = Talisman(app)

# Set up CORS policies
CORS(app)

# pylint: disable=wrong-import-position, cyclic-import
from service import routes, models  # noqa: F401 E402
from service.common import log_handlers  # noqa: F401 E402

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    models.init_db(app)  # make our sqlalchemy tables
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    # gunicorn requires exit code 4 to stop spawning workers when they die
    sys.exit(4)

app.logger.info("Service initialized!")
