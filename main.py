# Create a dictionary called `person`, it has three properties, `name` which is a string, `age` which is an integer, `hobbies` which is a list of strings.
person = {
   "name": "Athoob",
   "age": 23,
   "hobbies": ["reading" , "walking"]
}

# Create a function called `change_age` which takes the `person` dictionary and a `number` as arguments, this function changes the age in the dictionary to the `number`. The return value of this function is the updated dictionary.

def change_age(person, number):
    person["age"] = number # by over writing
    return person 

print(change_age(person, 21))


# Create a function called `add_hobby` which takes the `person` dictionary and a `hobby` as arguments. This function adds the hobby to the list of `hobbies` inside the person dictionary. The function will return the updated dictionary.

def add_hobby(person, hobby):
   person["hobbies"].append(hobby)
   return person  

print(add_hobby(person, "Table Tennis"))


# CHALLENGE

# 1. Create a function called `add_job` which takes `person` dictionary and `job` which is a string, as arguments. 
#This function checks, if the dictionary does not have a property called `job` then it will add it to the dictionary.
#The function will return the updated dictionary.

def add_job(person, job):
    '''
    if  "job" not in person: # to check if this key is in the dictionary 
        person.updated ({"job" : "no job"})# to add a key called job to the dictionary 
        return job # to return the updated dictionary with job added to it 
        

print(add_job(person, job)) 
    ''' 

# 2. Create a function called `check_hobbies`, which takes a person dictionary as an argument. This function checks the number of hobbies for this person, if it's more than three hobbies, print to the user a message telling them that they're talented.
def check_hobbies(person):
    #for "hobbies" in person: # to check the key hobbies for the dictionary person 
    if len(person["hobbies"]) == 3: # to check the elements number of the proprty hobbies if = 3 
        print("you are talented person")
        return # to save the value 

print(check_hobbies(person)) 
