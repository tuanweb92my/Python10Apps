import json

data = json.load(open("data.json"))

def translate(w):
    if w.lower() in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word : ")

print(translate(word))
