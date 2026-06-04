for number in range(1, 11):
    print(number)

print('-------')

count = 0
while count < 11:
    print(count)
    count = count + 1
else: 
    print('done')

for number in reversed(range(1, 11)):
    print(number)
else:
    print('done')

reversed_count = 10
while reversed_count > 0:
    print(reversed_count)
    reversed_count = reversed_count - 1

hashtags = ''

while len(hashtags) < 7:
    hashtags += '#'
    print(hashtags)
else:
    print('stop')

for i in range(8):
    for j in range(8):
        print('# ', end='')
    print()

counting = 0

while counting < 11:
    result = counting * counting
    print(f'{counting} * {counting} = {result}')
    counting += 1
else:
    print('counting finished')

item_ls = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in item_ls:
    print(item)

for x in range(0, 101, 2):
    print(x)

for y in range(0, 101):
    if y % 2 != 0:
        print(y)

num = 0
for number in range(0, 101):
    num += number
print('total sum of the number is', num)

num_even = 0
for number_even in range(0, 101, 2):
    num_even += number_even

num_odd = 0
for number_odd in range(0,101):
    if number_odd % 2 != 0:
        num_odd += number_odd
    
print(f'The sum of all evens is {num_even}. And the sum of all odds is {num_odd}.')

from countries import countries_list

for countriesss in countries_list:
    if 'land' in countriesss.lower():
        print(countriesss)

fruit = ['banana', 'orange', 'mango', 'lemon']

for fruits in reversed(fruit):
    print(fruits)

from countries_data import countries_data
all_language = []
for country_data in countries_data:
    all_language.extend(country_data['languages'])

total_language = len(set(all_language))
print(f'total language is {total_language}')

language_counts = {}

for country_lang in countries_data:
    for lang in {country_lang['languages']}:
        if lang in language_counts:
            language_counts[lang] += 1
        else:
            language_counts[lang] = 1

sorted_language = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)

ten_most_spoken = sorted_language[:10]
print('10 most spoken language', ten_most_spoken)

sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print('10 most populated countries:')
for i in range(10):
    country = sorted_by_population[i]
    print(f"{i+1}. {country['name']}: {country['population']}")