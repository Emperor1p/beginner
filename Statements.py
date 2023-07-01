temperature = 307
if temperature == 30:
        print('it is a normal day')
elif temperature > 30:
        print('it is a hot day')
else:
        print('what a lovely day')

name = "Joghr"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a  maximum of 50 character")
else:
    print('Name is good')

#while loop
i =  1
while i <= 5:
    print('$' * i)
    i += 1
print("Done")