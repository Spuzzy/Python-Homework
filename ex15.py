from sys import argv
prompt = ":> "
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())
txt.close()

print("Type the filename again: ")
file_again = input(prompt)

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

