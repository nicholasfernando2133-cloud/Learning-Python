#number 1
age = 18
#number 2
height = 170.0
#number 3
complex_num = 1j

#number 4
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area_of_triangle = 0.5*base*height

print("area of the triangle is: ", area_of_triangle)

#number 5
side_a = float(input("side a: "))
side_b = float(input("side b: "))
side_c = float(input("side c: "))

perimeter =  side_a + side_b + side_c

print("perimeter of the triangle is ",perimeter)

#number 6

rectangle_length =  float(input("rectangle length: "))
rectangle_width = float(input("rectangle width: "))

rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

print("area of rectangle is: ", rectangle_area)
print("perimeter of the rectangle is: ", rectangle_perimeter)

#number 7

radius = float(input("circle radius: "))

circle_area = 3.14 * radius * radius
circle_circumference = 2 * 3.14 * radius

print("circle area is: ", circle_area)
print("circle circumference is: ", circle_circumference)

#number 8

slope_num8 = float(input("slope: "))

x_zero = 0
y_intercept = (slope_num8 * x_zero) - slope_num8

y_zero = 0
x_intercept = (y_zero + slope_num8) / slope_num8

print("slope: ", slope_num8)
print("y intercept", y_intercept)
print("x intercept", x_intercept)

#number 9

x1 = 2
x2 = 6
y1 = 2
y2 = 10

slope_num9 = (y2 - y1) / (x2 - x1)
distance =  ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("slope adalah: ",slope_num9)
print("distance adalah: ",distance)

#number 10
if slope_num8 == slope_num9:
    print("slope nomor 8 dan 9 sama")
else: print("slope nomor 8 dan 9 beda")

#number 11
x = float(input("berapa x nya?: "))
y = float(x**2 + 6 * x + 9)

print("hasil y: ",y)

#number 12
dragon = len("dragon")
python = len("python")

if python == dragon:
    print ("python dan dragon punya total huruf yang sama")
else:
    print("python dan dragon tidak mempunyai total huruf yang sama")

#number 13
if "on" in "python" and "on" in "dragon":
    print("python dan dragon ada kata on nya")
else:
    print ("python dan dragon gak ada on nya")

#number 14
if "jargon" in "i hope this course is not full of jargon":
    print("jargon is in the sentence")
else:
    print("jargon is not in the sentence")

#number 15
if "on" not in "dragon" and "on" not in "python":
    print("benar, on tidak ada di dragon dan python")
else:
    print ("salah, ada on di dragon dan python")

#number 16
length_python = len("python")

float_py = float(python)
print("hasil float: ",float_py)
string_py = str(float_py)
print("hasil string: ",string_py)

#number 17
nomor = int(input("number: "))
if nomor % 2 == 0:
    print("number is even")
else:
    print("number is not even")

#number 18
if 7 // 3 == int(2.7):
    print("equal")
else:
    print("not equal")

#number 19
if type("10") == type(10):
    print("equal")
else:
    print("not equal")

#number 20
float_convert = int(float('9.8'))
if float_convert ==  10:
    print("equal")
else:
    print("not equal")

#number 21
hours = input("enter hours: ")
rate_per_hour = input("enter rate per hour: ")
weekly_earning = int(hours) * int(rate_per_hour)
print("your weekly earning is: ",weekly_earning)

#number 22
years = input("number of years you have lived: ")

lived = int(years) * 31536000

print("you have lived for ",lived," years")

#number 23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")