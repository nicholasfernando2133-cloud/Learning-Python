dog = {
    'name' : 'Sigma',
    'color' : 'golden brown',
    'breed' : 'husky or sumn idk',
    'legs' : 'honestly idk i dont own a dog',
    'age' : '8',
}

student = {
    'first name' : 'samsul',
    'last name' : 'ma\'arif',
    'gender' : 'male',
    'age' : 18,
    'marital status' : 'single', 
    'skills' : ['Python', 'English','Cybersecurity'], 
    'country' : 'Indonesia', 
    'city address' : 'Palapa V'
}

#print (student)

#print(len(student))

isi_skills = student['skills']
#print(type(isi_skills))
student['skills'].append('HTML')

#print(student)

dog_key_list = list(dog.keys())
dog_value_list = list(dog.values())
print(dog_key_list)
#print(dog_value_list)

dog_list = list(dog.items())
#print(dog_list)

del student['first name']
#print(student)