from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def beginning():

	list = ['You are a','Hey you','You want to','Sup my','How are','You happy','Can you']
	
	return list[random.randrange(6)]