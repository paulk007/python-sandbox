from helper import validate_and_execute
import os
import logging

print(os.name)
logger = logging.getLogger("MAIN")
logger.error("Error")

user_input = ""
while user_input != "exit":
    user_input = input("Enter a value \n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)



#my_dictionary = {"days": 20, "unit": "hours", "message": "All good"}
#print(my_dictionary["message"])


