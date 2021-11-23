
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24*60} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {conversion_unit}"
    else:
        return "incorrect unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered zero")
        else:
            print("You entered a negative number")
    except ValueError:
        print("Your input is not a number")

