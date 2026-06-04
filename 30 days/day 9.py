#age comparison

age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to learn to drive.')
else:
    age_needed = 18 - age
    print('You need',age_needed, 'more years to learn to drive.')

age_compare = int(input('How old are you?: '))
my_age = 18

if age_compare >= my_age:
    age_diff = age_compare - my_age
    print('You are', age_diff,'years older than me.')
else:
    print('im older than you')

a = input('Enter number one: ')
b = input('Enter number two: ')

if a > b:
    print(a,'is greater than',b)
else:
    print(a,'is smaller than',b)
if a == b:
    print(a,'is equal to',b)

#scoring method
score = int(input('what is the score?: '))

if score >= 90:
    print('your score is A')
elif score >= 80:
    print('your score is B')
elif score >= 70:
    print('your score is C')
elif score >= 60:
    print('your score is D')
else:
    print('your score is F')

#season
month = input('What month: ').strip().capitalize()

Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April','May']
Summer = ['June', 'July', 'August']

if month in Autumn:
    print('the season of the month is Autumn')
elif month in Winter:
    print('the season of the month is in Winter')
elif month in Spring:
    print('the season of the month is Spring')
else:
    print('the season of the month is Summer')

#fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

search = input('search for fruit: ')

if search in fruits:
    print('the fruit you\'re looking for is in the list')
else:
    search not in fruits
    fruits.append(search)
    print(fruits)

#dictionary
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in list(person.keys()):
    print('skills is in person')
    isi_skills = person['skills'][2]
    print(isi_skills)
else:
    print('There is no skills')

if 'skills' in list(person.keys()):
    print('skills is in person')
    if 'Python' in person['skills']:
        print('Python is in the person\'s skills')
else:
    print('Python is not in his skills')

skills = set(person['skills'])
if skills == {'JavaScript', 'React'}:
    print('he is frontend dev')
elif skills == {'Node', 'Python', 'MongoDB'}:
    print('He is a backend dev')
elif skills == {'React','Node','MongoDB'}:
    print('he is a fullstack developer')
else:
    print('unknown title')

is_married = person['is_married']
country = person['country']

if is_married is True and country is 'Finland':
    print('The person is married and in finland')
elif is_married is True and country is not 'Finland':
    print('The person is married but not in Finland')
else:
    print('The person is not married and not in finland')