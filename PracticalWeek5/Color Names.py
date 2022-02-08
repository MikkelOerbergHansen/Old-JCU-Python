"""
Based on the state name example program above,
create a program that allows you to look up hexadecimal colour codes
like those at http://www.color-hex.com/color-names.html
Use a constant dictionary of about 10 names and write a program that allows a user
to enter a name and get the code, e.g. entering AliceBlue should show #f0f8ff.
"""

COLOR_NAMES = {"red1": "#ff0000", "blue1": "#0000ff", "black": "#000000",
               "gray": "#bebebe", "green1": "#00ff00",
               "yellow1": "#ffff00", "white": "#ffffff", "purple1": "#9b30ff",
               "pink1": "#ffb5c5", "gold1": "#ffd700"}
# print(COLOR_NAMES)

color = input("Enter a color name: ")
color = color.lower()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid name")
    color = input("Enter a color name: ")
    color = color.lower()

for k, v in COLOR_NAMES.items():
    print("{:<10}  {}".format(k, v))
