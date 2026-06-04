it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))
print('----------------------------------------------------------------------------------------------')

it_companies.add('Twitter')
print(it_companies)
print('----------------------------------------------------------------------------------------------')

new_it_companies = (['Tiktok','ChatGPT','Claude'])
it_companies.update(new_it_companies)
print(it_companies)
print('----------------------------------------------------------------------------------------------')

#kalau remove jadi ada error syntax sedangkan kalau discard gak ada error
it_companies.remove('Tiktok')
print(it_companies)
print('----------------------------------------------------------------------------------------------')

it_companies.discard('tiktok')
print(it_companies)
print('----------------------------------------------------------------------------------------------')

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A)
print(B)
print('----------------------------------------------------------------------------------------------')

item_AB = B.union(A)
print('----------------------------------------------------------------------------------------------')

print(item_AB)
print('----------------------------------------------------------------------------------------------')

intersection = B.intersection(A)
print(intersection)
print('----------------------------------------------------------------------------------------------')

subset = A.issubset(B)
print(subset)
print('----------------------------------------------------------------------------------------------')

disjoint = A.isdisjoint(B)
print(disjoint)
print('----------------------------------------------------------------------------------------------')

joinAB = A.union(B)
joinBA = B.union(A)

print(joinAB)
print(joinBA)
print('----------------------------------------------------------------------------------------------')

symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)
print('----------------------------------------------------------------------------------------------')

del it_companies
del A
del B

age = [22, 19, 24, 25, 26, 24, 25, 24]

set_age = set(age)
print(set_age)
print('----------------------------------------------------------------------------------------------')

age_len = len(age)
set_age_len = len(set_age)
print('age len: ',age_len)
print('set age len: ',set_age_len)

if age_len > set_age_len:
    print('age is bigger than set age')
else:
    print('set age is bigger than age')
print('----------------------------------------------------------------------------------------------')

print('string adalah teks yang tidak dapat diubah')
print('list adalah koleksi berbagai teks yang bisa diubah, dan bisa menyimpan data duplikat')
print('tuple adalah koleksi berurutan yang tidak dapat diubah')
print('koleksi yang tidak berurutan dan tidak boleh ada duplikat')
print('----------------------------------------------------------------------------------------------')

text = 'I am a teacher and I love to inspire and teach people'

words = text.split()

unique = set(words)

print(unique)