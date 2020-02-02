import os
import json
list = os.listdir("C:/Users/h/Google Drive/scripts/kirbybot") # dir is your directory path
number_files = len(list)


user = {"number":1234567890, "placeInQueue": 0, "sentToday": False }
print(list[user["placeInQueue"]])
