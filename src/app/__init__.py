from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    app.config.update({"TESTING": True, "DEBUG": True})

    @app.route("/")
    def home():
        return jsonify({"message": "hello world"})

    return app
