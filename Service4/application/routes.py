from application import app
import requests


@app.route('/randomword', methods=['GET'])
def sentence():
    beginning = requests.get('http://localhost:5001/randomphrase')
    ending = requests.get('http://localhost:5002/randomphrase')
    response = beginning.text + " " + ending.text
    return response