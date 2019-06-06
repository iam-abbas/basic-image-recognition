import requests
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def say(str_say) :
    engine.say(str_say)
    engine.runAndWait()

say("Which image do you want me to look at?")
API_KEY = "AIzaSyCw804QomtGBaRFZveQdz3MyjOTGOkRXFk";
image = input("Enter Image URL: ")

api_url = 'https://vision.googleapis.com/v1/images:annotate?key='+API_KEY
data='''{
  "requests": [
    {
      "features": [
        {
          "type": "LABEL_DETECTION"
        }
      ],
      "image": {
        "source": {
          "imageUri": "'''+image+'''"
        }
      }
    }
  ]
} '''

label_dict = {}
response = requests.post(api_url, data=data)
response = response.json()
responses = response['responses']

for response in responses:
        labels = response['labelAnnotations']
        for label in labels:
                label_dict[label['description']] = label['score']
                
#print(label_dict)
say("looks like"+max(label_dict, key=label_dict.get))
