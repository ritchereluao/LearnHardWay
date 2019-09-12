tabby_cat = "\tI'm tabbed in."
percian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat." # \\ does backslash only

fat_cat = '''
I'll do a list:
\t * Cat food
\t * Fishies
\t * Catnip\n\t * Grass
''' # same when you use """ but different when this message is inside

print(tabby_cat)
print(percian_cat)
print(backslash_cat)
print(fat_cat)

print("I am 6'2\" tall.") # so that the double quote after 2 can be printed
print('I am 6\'2" tall.') # also for the quote to be red inside the single quote
