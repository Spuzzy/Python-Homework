name = 'Zed A. Shaw'
age = 35 # not a lie
inchesheight = 74 # inches
poundsweight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cmheight = inchesheight * 2.54
kgweight = poundsweight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {inchesheight} inches or {cmheight} cm tall.")
print(f"He's {poundsweight} pounds or {round(kgweight,2)} kg heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + inchesheight + poundsweight
print(f"If I add {age}, {inchesheight}, and {poundsweight} I get {total}.")
