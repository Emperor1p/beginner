name = input('what is your name? ')
favorite_colour = input('what is your favorite colour? ')
print(name + ' likes ' + favorite_colour)

birth_year = input('Birth year ')
age = 2023 - int(birth_year)
print(age)



#string
course = "pyton's for beginners"
print(course)
print(len(course))
print(course[1:-2])
list = [[1,2,[3,4]],[5,6],[7,8,9]]
print(list[0][2][1])

first = 'Peter'
last = 'Ayoola'
msg = f'{first} {last} is a coder'
print(msg)

#sring method
course = 'Python for beginners'
print(course.upper())
print(course.find('g'))
print(course.replace('beginners', 'Absolute beginners'))
