animal = "dog"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat =f"I'm \\ a \\ {animal}."

fat_cat = f"""
I'll do a list:
\t* {animal} food
\t* Fishies
\t* Catnip\n\t* Grass
""" 

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat, end = "  ")
print("\t\256")
