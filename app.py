from flask import Flask, request
from flask import jsonify
import json
import trader

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify(content="OK")

counter = 0
@app.route('/getURL', methods=['POST'])
def getURL():
    data = json.loads(request.get_data(as_text=True))
    global counter
    counter = counter + 1
    if counter == 1:
        trader.main(data['URL'])
    else:
        pass
    return str(counter)

if __name__ == "__main__": 
    app.run(host='0.0.0.0')