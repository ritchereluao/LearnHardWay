from sys import argv # importing from sys import argv

script, filename = argv # script, filename

txt = open(filename) # the filename that was typed aboved is saved as txt

print(f"Here's your file {filename}:") # prints this line and the filename
print(txt.read()) # prints the ones being read on the file

print("Type the filename again:") # prompts for file name again
file_again = input("> ") # prompts from above

txt_again = open(file_again) # assigns to txt_again

print(txt_again.read()) # prints the one being read on the file
