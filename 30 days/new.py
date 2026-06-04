from countries_data import countries_data

sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print('10 most populated countries:')
for i in range(10):
    country = sorted_by_population[i]
    print(f"{i+1}. {country['name']}: {country['population']}")