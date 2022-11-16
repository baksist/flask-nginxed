from flask import Flask

app = Flask(__name__)

@app.route("/")
def make_app():
    
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Everything in its right place."
    
    return app