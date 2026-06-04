#day2 30 days python

first_name = "Nicholas"
last_name = "Lim"
full_name = "Nicholas Fernando Lim"
country = "Indonesia"
city = "jakarta"
age = 18
year = 2026
is_married = False

fn_lenght = len(first_name)
ln_lenght = len(last_name)

comparison = fn_lenght - ln_lenght
print("comparison between first and last name is: ",comparison)

num_one = 5
num_two = 4

add = num_one + num_two
subtract = num_one - num_two
multiply = num_one * num_two
divide = num_one / num_two
modulus = num_one % num_two
power = num_one ** num_two
powerdiv = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius * radius
circum_of_circle = 2 * 3.14 * radius

pencarian = input("mau cari apa?: ")
if pencarian == "first name":
    print(first_name)
elif pencarian == "last name":
    print(last_name)
elif pencarian == "age":
    print(age)
elif pencarian == "country":
    print(country)
elif pencarian == "radius":
    print(radius)
elif pencarian == "luas lingkaran":
    print(area_of_circle)
elif pencarian == "keliling lingkaran":
    print(circum_of_circle)

else:
    print("Pilihan tidak ditemukan")