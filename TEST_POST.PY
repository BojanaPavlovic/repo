import requests
BASE_URL = "https://simple-books-api.glitch.me"
AUTOR = "https://simple-books-api.glitch.me/api-clients" #--> api za registraciju 

response = requests.post(AUTOR,data = {"clientName": "Djordje","clientEmail": "pavlisimo1970jug@gmail.com"}).json()
print(response)

#######################################################################################################################
#UZET TOKEN POSTMANOM 
accessToken = "3dfc194f0f100254eb817599ac8b054411db4477945ded0ba94f6e346f029a34"

DATA = {
   
    "bookId": 4,
    "customerName": "John"
}
POST_URL = "https://simple-books-api.glitch.me/orders/?accessToken=3dfc194f0f100254eb817599ac8b054411db4477945ded0ba94f6e346f029a34"

r = requests.post(POST_URL, data=DATA).json()
print(r)





