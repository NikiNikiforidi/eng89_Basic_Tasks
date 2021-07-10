# Completed basic tasks in class: 23/6/21
## 5 tasks to complete.
- Data collection and control flow task
- Control flow task
- FizzBuzz task
- Calculate year of birth task
- Dictionary task




### Task 1, data collections and control flow :
- Prompt user for input and print strings.

#### Version 1: Define variable `name` and use concatenation to print welcome message

- Make sure to remove white spaces and have the first letter capitalized
```
name = input("Entre your first name: ").strip().title()
print("Welcome",name)
```

#### Version 2: Define variable 'full_name' and use interpolation to print welcome message
- Make sure to remove white spaces and have the first letters capitalized
```
full_name = input("Enter your full name: ").strip().title()
print("Welcome {}".format(full_name))
```



### Task 2, Control flow:
- As a user I should be able to ask the user for the rating, and receive back the appropriate response:

- universal -> everyone can watch
- pg --> General viewing, but some scenes may be unsuitable for young children
- 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12.
- No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
- 15 --> No one younger than 15 may see a 15 film in a cinema.
- 18 --> No one younger than 18 may see an 18 film in a cinema.
```
movie_rating = input("Which movie rating would yo like to check, Universal or PG?: ").title().strip()

if movie_rating == "Universal":
    print("Any age can watch, Enjoy the movie!")

if movie_rating == "Pg":
    print("General viewing, but some scenes may be unsuitable for young children")

viewer_age= int(input("How old is the viewer?:"))
if viewer_age <= 12:
           print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12.")
elif viewer_age <= 15:
            print("No one younger than 15 may see a 15 film in a cinema.")
elif viewer_age <= 18:
            print("No one younger than 18 may see an 18 film in a cinema.")
```


 ### Task 3, FizzBuzz task:
 - Write a program that prints the numbers from 1 to 100.
 - For multiples of three print "Fizz" instead of the number
 - For the multiples of five print "Buzz" instead of the number
 - For numbers which are multiples of both three and five print "FizzBuzz".

```
for num in range(1,101):               # Specifying the numerical range from 1 to 100
    if num % 3 == 0 and num % 5 == 0:  # If the current num is perfectly divisible by both 3 and 5
        print("FizzBuzz")              # then print FizzBuzz.
        continue                       # Skip the rest of the code and continue loop
    elif num %3 ==0:                   # If the current num is perfectly divisible by 3
        print("Fizz")                  # then print Fizz
        continue                       # Skip the rest of the code and continue loop
    elif num %5 ==0:                   # If the current num is perfectly divisible by 5
        print("Buzz")                  # then print Buzz.
        continue                       # Skip the rest of the code and continue loop
    print(num)                         # Display num values
```

### Task 4, dictionary task:

- 1.Define a dictionary call story1, it should have the following keys:
        # 'start', 'middle' and 'end'
- 2. Print the entire dictionary
- 3. Print the type of your dictionary
- 4. Print only the keys
- 5. print only the values
- 6. print the individual values using the keys (individually, lots of print commands
- 7. Now let's add a new key:value pair: 'hero': yourSuperHero
```
# My fantastic story
story1 = {
    "Start" : "Once upon a time,",
    "Middle" : "a fierce engineer named Niki wrote some code. ",
    "End" : "The end"
}
# - Print the entire dict
print(story1)

# - Print type of dict
print(type(story1))

# - Only print KEYS
print(story1.keys())

# - Only print VALUES
print(story1.values())

# - Print individual VALUES using the KEYS
print(story1.get("Start"))
print(story1.get("Middle"))
print(story1.get("End"))

# - A for loop that prints the VALUES of the dict
for data in story1.values():
    print(data)

# - Add a new KEY-VALUE: "Hero":"Your hero"
story1["Hero"]="Don't have one :) "
print(story1)
```


### Task 5:

- define the variables `age` and `name`
- make a calculation for the year in which the person was born
- print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values

#### Second Part

- prompt the user for input and re-assign the variable `age` and `name`
- figure out a way to account for if the persons birthday has already happened this year or not

#### Extra

- go look into the library time
- print out the amount of hour this person has lived

```
import datetime
current_date = datetime.datetime.now()
 
``` 
- Assigning current day, month and year to separate variables

 ```
current_year = int(current_date.strftime("%G"))
current_month = int(current_date.strftime("%m"))
current_day = int(current_date.strftime("%d"))

```
- Getting users name
```
name = input("Enter your name: ").title()
print(f"Hey {name}")

```
- Getting users age and checking if age is a digit
```
age = input("Enter your age: ")
digit_check = age.isdigit()
```
- While the age is not a digit , ask to re-enter age as digit
```
while digit_check != True:
     age = input("Please only use numbers while writing your age: ")
     digit_check = age.isdigit()
```
- Calculating and printing year of birth
```
year_of_birth = current_year - int(age)

print(f"OMG {name}, you are {age} years old, so you were born in {year_of_birth}!!!")

```

#### Second Part
##### Also shows the evolution of my code
C creating a dictionary to story birthday information
```

date_of_birth = {
     "Day" : "nul",
     "Month" : "nul ",
     "Year" : "nul "
}

```
- Looping through Dict and assigning user input birthday information to each key
```
for k, v in date_of_birth.items():
    date_of_birth[k]=input(f"Please enter the {k} of your birthday: ").strip()
    digit_check = date_of_birth[k].isdigit()
```
- While the age is not a digit, ask to re-enter age as digit and assigning it to dict
```

    while digit_check != True:
       v = input("Please only use numbers while writing your birthday: ").strip()
       digit_check = v.isdigit()
       date_of_birth[k] = v
```
- Calculating whether the user has either had their birthday, will have their birthday this month or if it is currently their birthday
```
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

```
