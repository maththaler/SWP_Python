from flask import Flask, request
import json
import config
import Rock_Paper_Scissors_Spock_Lizard_DB as db

app = Flask(__name__)

@app.route(config.url, methods = ["POST"])
def index():
    db.insert_data(request.form.to_dict(flat=True))
    return "Success"


if __name__ == "__main__":
    app.run(debug=True)