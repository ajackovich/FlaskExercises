from datetime import datetime

from flask import Flask
    
app = Flask(__name__)

@app.route("/")
def home():
    date = datetime.now()
    return date.strftime("%d/%m/%y")

if __name__ == "__main__":
    app.run(debug=True)