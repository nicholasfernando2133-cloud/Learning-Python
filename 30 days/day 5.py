#1
empty_list = list()
print(len(empty_list))

#2
lst = ('item1','item2','item3','item4','item5')
first_item, second_item, third_item, *rest, last = lst

print(first_item)
print(second_item)
print(third_item)
print(rest)

#3
print(len(lst))

#4
print(first_item)
print(third_item)
print(last)

#5
mixed_data_type = ['Nicholas','18','170cm','married','kedoya']

#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first, second, third, middle, *rest, last = it_companies

#7
print(mixed_data_type)

#8
print(len(it_companies))

#9
print(first, middle, last)

#10
it_companies[0] = 'Meta'
print(it_companies)

#11
it_companies.append('Tiktok')
print(it_companies)

#12
it_companies.insert(4, 'Steam')
print(it_companies)

#13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14
it_companies_string = '#; '.join(it_companies)
print(it_companies_string)

#15
if 'Google' in it_companies:
    print('google is in IT COMPANIES')
else:
    print('google is not in IT COMPANIES')

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse
print(it_companies)

#18
first_three = it_companies[0:3]
print(first_three)

#19
last_three = it_companies[-3:]
print(last_three)

#20
middle = it_companies[4]
print(middle)

#21
it_companies.remove('Amazon')
print(it_companies)

#22
it_companies.remove('META')
print(it_companies)

#23
it_companies.remove('Tiktok')
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_and_back = front_end + back_end

print(front_and_back)

#27
front_back_copy = front_and_back.copy()
front_back_copy.insert(5, 'python')
front_back_copy.insert(6, 'SQL')

print(front_back_copy)

#excersise level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#1
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)

#2
ages.append(min_age)
ages.append(max_age)
print(ages)

ages.sort()
print('sorted ages:', ages)

#3
n = len(ages)
if n % 2 == 1:
    median = ages[n//2]
else:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
print(f'median: {median}')

average = sum(ages) / len(ages)
print(f"average: {average}")

age_range = max_age - min_age
print(f'range: {age_range}')

value1 = abs(min_age - average)
value2 = abs(max_age - average)

print(value1)
print(value2)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
first_country, second_country, third_country, *scandic = countries

tengah = len(countries) // 2
negara_tengah = countries[tengah]
print(negara_tengah)

jumlah = len(countries)

if jumlah % 2 == 0:
    titik_tengah = jumlah // 2
else:
    titik_tengah = (jumlah // 2) + 1

banyak_pertama = countries[:titik_tengah]
banyak_kedua = countries[titik_tengah:]

print(banyak_pertama)
print(banyak_kedua)
print("---")
print(first_country)
print(second_country)
print(third_country)
print("---")
print('jumlah negara sisa: ', len(scandic))
print(scandic)