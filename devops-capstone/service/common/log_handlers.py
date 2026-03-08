"""
Module: log_handlers
"""
import logging


def init_logging(app, logger_name):
    """Set up logging for production"""
    app.logger.propagate = False
    gunicorn_logger = logging.getLogger(logger_name)
    if gunicorn_logger.handlers:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
        app.logger.info("Logging established")
