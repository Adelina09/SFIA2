from application import app
import random


@app.route('/randomstory', methods=['GET'])
def beginning():

	list = ["Once upon a time, a prince met a princess. ","It is now or never! the prince shouted to his trusted dragon. ","It all started when she was born. ","All the decisions they've ever made are coming back to them like a dream. ","Not so tough now! Let's go Dunbar! ","And so it begins. ","The story begins with their disappearance. "]
	
	return list[random.randrange(6)]