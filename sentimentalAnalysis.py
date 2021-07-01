from monkeylearn import MonkeyLearn
ml = MonkeyLearn('Your Monkey Learn API Key')
model_id = 'You Monkey Learn model Id'


print("This program determines whether a text is positive, negative of neutral")
print("Enter Text and to exit enter exit")


body = input("Enter Text: ")
while(body.lower()!="exit"):
	data = []
	data.append(body)
	response = ml.classifiers.classify(model_id, data)
	if (response.body[0]['classifications'][0]['tag_name'] == "Positive"):
		print("\U0001f604 A Positive Text")
	elif (response.body[0]['classifications'][0]['tag_name'] == "Negative"):
		print("\U0001f621 A Negative Text")
	elif (response.body[0]['classifications'][0]['tag_name'] == "Neutral"):
		print("\U0001f636 A Neutral Text")
	body = input("Enter Text: ")
