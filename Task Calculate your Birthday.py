# ### Task 5:

# - define the variables `age` and `name`
# - make a calculation for the year in which the person was born
# - print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values

# #### Second Part

# - prompt the user for input and re-assign the variable `age` and `name`
# - figure out a way to account for if the persons birthday has already happened this year or not

# #### Extra

# - go look into the library time
# - print out the amount of hour this person has lived




import datetime
current_date = datetime.datetime.now()

# assigning current day, month and year to separate variables

current_year = int(current_date.strftime("%G"))
current_month = int(current_date.strftime("%m"))
current_day = int(current_date.strftime("%d"))


# Getting users name
name = input("Enter your name: ").title()
print(f"Hey {name}")

# Getting users age and checking if age is a digit
age = input("Enter your age: ")
digit_check = age.isdigit()


# While the age is not a digit , ask to re-enter age as digit
while digit_check != True:
     age = input("Please only use numbers while writing your age: ")
     digit_check = age.isdigit()


# Calculating and printing year of birth
year_of_birth = current_year - int(age)
print(f"OMG {name}, you are {age} years old, so you were born in {year_of_birth}!!!")



# # #### Second Part
# ##### Also shows the evolution of my code :)


# creating a dictionary to story birthday information
date_of_birth = {
     "Day" : "nul" ,
     "Month" : "nul",
     "Year" : "nul "
}


# Looping through Dict and assigning user input birthday information to each key
for k, v in date_of_birth.items():
    date_of_birth[k]=input(f"Please enter the {k} of your birthday: ").strip()
    digit_check = date_of_birth[k].isdigit()

# While the age is not a digit, ask to re-enter age as digit and assigning it to dict
    while digit_check != True:
       v = input("Please only use numbers while writing your birthday: ").strip()
       digit_check = v.isdigit()
       date_of_birth[k] = v


# Calculating whether the user has either had their birthday, will have their birthday this month or if it is currently their birthday

if int(date_of_birth["Month"]) < current_month:
    print(f"{name}, you have already celebrated your birthday!!")

if int(date_of_birth["Month"]) == current_month:
    if int(date_of_birth["Day"]) == current_day:
        print(f"Happy Birthday {name}!!")
    elif int(date_of_birth["Day"]) < current_day:
        print(f"You have already celebrated your birthday this month {name}")
    elif int(date_of_birth["Day"]) > current_day:
        birth_days = int(date_of_birth["Day"])- current_day
        print(f"{name} it's your birthday in {birth_days} days!")


