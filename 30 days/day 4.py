
#number 1
first = 'Thirty'
second = 'Days'
third = 'Of'
fourth = 'Python'

sentence1 = '{} {} {} {}'.format(first, second, third, fourth)

print(sentence1)

#number 2
first_let = 'Coding'
second_let = 'For'
third_let = 'All'

sentence2 = '{} {} {}'.format(first_let, second_let, third_let)

print(sentence2)

#number 3
company = "Coding For All"

#number 4
print(company)

#number 5
print(len(company))

#number 6
print(company.upper())

#number 7
print(company.lower())

#number 8
print(first_let.capitalize(), second_let.title(), third_let.swapcase())

#number 9
kata_pertama = company[:6]

print(kata_pertama)

#number 10
if "Coding" in (first_let, second_let, third_let):
    print("there is \"Coding\" inside")
else:
    print("there is no \"Coding\" inside")

#number 11
company_python = company.replace("Coding", "Python")

print(company_python)

#number 12
py_for_all = "Python For Everyone"
change_py_for_all = py_for_all.replace("Everyone", "All")

print(py_for_all)
print(change_py_for_all)

#number 13
print(company.split())

#number 14
String_Of_Words = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(String_Of_Words.split(", "))

#number 15
print(company[0])

#number 16
print(company[-1])

#number 17
print(company[10])

#number 18
kata = py_for_all.split()

akronim = "".join( word[0] for word in kata)

print(akronim)

#number 19

kata_company = company.split()

akronim_company = "".join( word[0] for word in kata_company)

print(akronim_company)

#number 20
cari_c = company.index("C")
print(cari_c)

#number 21
cari_f = company.index("F")
print(cari_f)

#number 22
textA = "Coding For All People"
cari_a = textA.rfind("l")
print(cari_a)

#number 23
textB = 'You cannot end a sentence with because because because is a conjunction'

cari_because = textB.find("because")
print(cari_because)

#number 24
cari_rindex = textB.rindex("because")
print(cari_rindex)

#number 25
awal = textB.index("because")
akhir = textB.rindex("because") + 7

hasil_potong = textB[awal:akhir]

print(hasil_potong)

#number 26
first_occ = textB.index("because")

print(first_occ)

#number 27

awal = textB.index("because")
akhir = textB.rindex("because") + 7

hasil_potong = textB[awal:akhir]

print(hasil_potong)

#number 28
hasil = company.startswith("Coding")
print(hasil)

#number 29
substring_coding = company.startswith("coding")
print(substring_coding)

#number 30
berantakan = '   Coding For All      '
bersih = berantakan.strip()
print(bersih)

#number 31
teks1 = '30DaysOfPython'
teks2 = 'thirty_days_of_python'

teks1_iden = teks1.isidentifier()
teks2_iden = teks2.isidentifier()

print(teks1_iden)
print(teks2_iden)

#number 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
hasil ='# '.join(libraries)

print(hasil)

#number 33
teksC = "I am enjoying this challenge.\nI just wonder what is next."
#number 34
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#number 35
radius = 10
area = 3.14 * radius ** 2

print("The area of a circle with radius", radius, "is", area, "meters square")

#number 36
a = f"8 + 6 = {8 + 6}"
b = f"8 - 6 = {8 - 6}"
c = f"8 * 6 = {8 * 6}"
d = f"8 / 6 = {8 / 6}"
e = f"8 % 6 = {8 % 6}"
f = f"8 // 6 = {8 // 6}"
g = f"8 ** 6 = {8 ** 6}"

print(a, b, c, d, e, f, g, sep="\n")