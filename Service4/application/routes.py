from application import app
import requests


@app.route('/randomword', methods=['GET'])
def sentence():
    beginning = requests.get('http://Service2:5001/randomstory')
    ending = requests.get('http://Service3:5002/randomstory')
    response = beginning.text + " " + ending.text
    return response