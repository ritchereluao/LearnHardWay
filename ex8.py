formatter = "{} {} {} {}" # setting up formatter

print(formatter.format(1, 2, 3, 4)) # .format command sets 1,2,3,4 in printing formatter
print(formatter.format("one", "two", "three", "four")) # same goes for this line
print(formatter.format(True, False, False, True)) # this line
print(formatter.format(formatter, formatter, formatter, formatter)) # and this line. Like printing formatter 16times
print(formatter.format( #this line got printed in one line instead of per line here.
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
