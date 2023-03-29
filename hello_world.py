import datetime
import requests
import random
currentTime = datetime.datetime.now()

print("================================================================")
print("{} - Welcome to dockerized python script".format(currentTime))
print("================================================================")

randomUserNum = random.randint(1,100)

res = requests.get('https://jsonplaceholder.typicode.com/todos/{}'.format(randomUserNum))
jsonResponse = res.json() 
print(jsonResponse)
print("Data retrieved successfully!!")