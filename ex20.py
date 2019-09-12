from sys import argv # usual from sys import argv

script, input_file = argv # script and enter the input file being read

def print_all(f): # function to read the file
    print(f.read())

def rewind(f): # function to rewind and seek to first line
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# Adding this code to create the text file
#input_file = open(input_file, 'w')
#input_file.write(input("Line1: "))
#input_file.write("\n")
#input_file.write(input("Line2: "))
#input_file.write("\n")
#input_file.write(input("Line3: "))
#input_file.write("\n")
#input_file.close()
# Adding the above code to create and write on the text

current_file = open(input_file) # assigning the file opened to current file

print("First let's print the whole file:\n")

print_all(current_file) # used the function above to read all in the file

print("Now let's rewind, lind of like a tape.")

rewind(current_file) # used to seek to the first line

print("Let's print three lines:")

current_line = 1 # assigned to line count / readline - read the line only
print_a_line(current_line, current_file)

current_line = current_line + 1 # same as below
print_a_line(current_line, current_file)

current_line += current_line # same as above
print_a_line(current_line, current_file)
