from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
from app import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/test'
db = SQLAlchemy(app)

# def get_data():
#     list = []
#     with open('./data/emissions_data.json') as data_file:    
#         data = json.load(data_file)
#         for v in data:
#             data = (v['Average'], v['Date'], v['Interpolated'], v['Number of Days'],v['Trend'])
#             list.append(data)
#     return list

#Members API Route
# @app.route("/members")
# def members():
#     list = get_data()
#     return list



class Event(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    average = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Event: {self.average}"

    def __init__(self, average):
        self.average = average

@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)