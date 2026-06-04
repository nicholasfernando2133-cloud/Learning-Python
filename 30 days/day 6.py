#1
empty_tuple = tuple()

#2
tpl_sisters = ('Ashley','Mashel','Agnes','Meisye')
tpl_brothers = ('Austin','Jason','Jonathan','Justin')
print(tpl_sisters)
print('------------------------------------------------------------------------------------------------------------------------')

print(tpl_brothers)
print('------------------------------------------------------------------------------------------------------------------------')

#3
tpl_siblings = tpl_sisters + tpl_brothers
print(tpl_siblings)
print('------------------------------------------------------------------------------------------------------------------------')

#4
print(len(tpl_siblings))
print('------------------------------------------------------------------------------------------------------------------------')

#5
tpl_parents = ('Angel','Lucifer')

tpl_family_members = tpl_siblings + tpl_parents
print(tpl_family_members)
print('------------------------------------------------------------------------------------------------------------------------')

#level 2
#1
*tpl_siblings , mother, father = tpl_family_members
print('Siblings: ',tpl_siblings)
print('Father: ',father)
print('Mother:', mother)
print('------------------------------------------------------------------------------------------------------------------------')

tpl_fruits = ('Apple','Mango','Banana','Jackfruit')
tpl_vegetables = ('Brocoli','Carrot','Cauliflower','Potato')
tpl_animal_products = ('Beef','Broth','Chicken skin','Pork')

print(tpl_fruits)
print('------------------------------------------------------------------------------------------------------------------------')
print(tpl_vegetables)
print('------------------------------------------------------------------------------------------------------------------------')
print(tpl_animal_products)
print('------------------------------------------------------------------------------------------------------------------------')

tpl_food_stuff = tpl_fruits + tpl_vegetables + tpl_animal_products
print(tpl_food_stuff)
print('------------------------------------------------------------------------------------------------------------------------')

food_stuff_lst = list(tpl_food_stuff)
print(food_stuff_lst)
print('------------------------------------------------------------------------------------------------------------------------')

middle = food_stuff_lst [5:7]
print(middle)
print('------------------------------------------------------------------------------------------------------------------------')

first_three = food_stuff_lst [:3]
print(first_three)
print('------------------------------------------------------------------------------------------------------------------------')

last_three = food_stuff_lst [-3:]
print(last_three)
print('------------------------------------------------------------------------------------------------------------------------')

del tpl_food_stuff

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print('Estonia is in Nordic countries')
else:
    print('Estonia is not in Nordic countries')

print('------------------------------------------------------------------------------------------------------------------------')

if 'Iceland' in nordic_countries:
    print('Iceland is in Nordic countries')
else:
    print('Iceland is not in Nordic countries')

print('------------------------------------------------------------------------------------------------------------------------')
