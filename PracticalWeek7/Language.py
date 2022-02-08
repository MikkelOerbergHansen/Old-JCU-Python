"""
practical week 7
"""
from Programming_Language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


print(ruby.is_dynamic())                    # testing the is_dynamic function
print(python.is_dynamic())
print(visual_basic.is_dynamic())

print(ruby)                                 # testing the __str__ function
print(python)
print(visual_basic)

language_list = [ruby, python, visual_basic]    # looping through the list
print("the dynamically typed languages are:")
for language in language_list:
    if language.is_dynamic() is True:
        print(language.name)
