letter = '''Hello <|Name|>,
Greeting from an ABC company coding
House, I am Happy to Tell You that
you are selected!
Bill Regards, 
on Date - <|Date|>
Thank-You!
'''

name = input("Enter Your Name: ")
date = input("Enter Your Name: ")

letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)