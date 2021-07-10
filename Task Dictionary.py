# ### Task 4:

# - 1.Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'
#- 2. Print the entire dictionary
#- 3. Print the type of your dictionary
#- 4. Print only the keys
#- 5. print only the values
#- 6. print the individual values using the keys (individually, lots of print commands
#- 7. Now let's add a new key:value pair.
    # 'hero': yourSuperHero

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

# - Add a new KEY-VALUE "Hero":"Your hero"
story1["Hero"]="Don't have one :) "
print(story1)