from flask import Flask, request, send_from_directory, send_file

import os


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__, static_folder=os.getcwd() + "/static", static_url_path='/static')
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z]/'
    app.config['MAX_IMAGE_FILESIZE'] = 0.05 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = "static/"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
