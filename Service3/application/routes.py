from application import app
import random


@app.route('/randomstory', methods=['GET'])
def ending():

	list = ["They lived in a poor little village at the end of the world. ","He jumped towards the attacking creature, slashing it's throat and saving the kingdom.","She was due to be the new hairess to the kingdom, but in one swift moment everything changed.","They started questioning whether they should turn around or keep going. Their only hope was their little prince, left all alone back in the castle.","And they both went to discover the cure to their mother's illness. They travelled for 3 days and 3 nights in the most impressive parts of the kingdom.","He who shall not be named, walking around the kingdom as if he now owns it.","Everything was changed. Life as they knew it has transformed into something no one understood."]
	
	return list[random.randrange(6)]