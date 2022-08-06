import pyfiglet
message = pyfiglet.figletFormat("Welcome buddy!")
print(message)

name = input('Enter your name: ')

grade = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E']

print("Hello", name.upper())

score = input("Enter your score: ")
if score >= '80':
    print("Excellent! Your score grade is", grade[0])

elif '75' <= score <= '79':
    print("Very good! Your score grade is", grade[1])

elif '70' <= score <= '74':
    print("Good! Your score grade is", grade[2])

elif '65' <= score <= '69':
    print("Your score grade is", grade[3], 'Satisfactory')

elif '60' <= score <= '64':
    print("Your score grade is", grade[4], 'Pass')

elif '55' <= score <= '59':
    print("Your score grade is", grade[5], 'Weak pass')

elif '50' <= score <= '54':
    print("Your score grade is", grade[6], 'Poor')

else:
    print("Your score grade is", grade[7], 'Fail')

import pprint
jokes = " This is for absolute beginners"
pprint.pprint(jokes)


