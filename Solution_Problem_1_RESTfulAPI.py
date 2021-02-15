from flask import Flask, jsonify
app = Flask (__name__)

person = [
{
"first_name": "John",
"last_name": "Keynes",
"age": "29",
"favourite_colour": "red"
},
{
"first_name": "Sarah",
"last_name": "Robinson",
"age": "54",
"favourite_colour": "blue"
}
        ]

@app.route('/') 
def index():
    return "Solution_Problem_1"

@app.route('/person', methods=['GET']) 
def get():
    return jsonify ({'person':person})

if __name__=="__main__":
    app.run(debug=True)