from application import app
import random


@app.route('/randomphrase', methods=['GET'])
def ending():

	list = ['Okay','doing good','amazing feels','alright','enthusiasstic','well?','understanding?']
	
	return list[random.randrange(6)]