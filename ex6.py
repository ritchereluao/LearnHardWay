types_of_people = 10
x = f"There are {types_of_people} types of people." #formatted

binary = "binary" #assigning string
do_not = "don't" #assigning string
y = f"Those who know {binary} and those who {do_not}." #formatted

print (x) # printing x
print (y) # printing y

print(f"I said: {x}") # printing the string along with assigned to x
print(f"I also said: '{y}'") # print the string along with assigned to y

hilarious = True # assigning a string
joke_evaluation = "Isn't that joke so funny?! {}" # assigning a string with format

print(joke_evaluation.format(hilarious)) # printing the above in format

w = "This is the left side of..."
e = "a string with a right side."
print(w + e) # concatenate
