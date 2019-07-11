#Exercise 0

#Lists
fav_colours = ['Blue', 'Black', 'Red', 'Orange']
family_ages = [32, 38, 37, 30, 64, 63]
coin_flips = ['heads', 'tails', 'heads', 'heads', 'tails']
fav_artists = ['Nightwish', 'Pink Floyd', 'Hawkwind', 'Kamelot', 'Tool']

#Dictionaries
unique_words = { 'polypod': 'a many-legged animal', 'gamophobia': 'the fear of marriage', 'logodaedalus': 'an artificer in words' }
fav_movies = { 'Ex Machina': 2014, 'Back to the Future':1985, 'Predestination':2014 }
pop_cities = { 'Boston': 685100, 'Toronto':2930000, 'Halifax':431500, 'Hamburg':1810000 }
sibling_ages = { 'Lucas':38, 'Erin':37, 'Kathleen':30, 'Jodi':64, 'Dan':63, 'Justin':30, 'Patrick':31 }


#Exercise 1
print('Exercise #1')
print (coin_flips) # ['heads', 'tails', 'heads', 'heads', 'tails']
print (fav_colours[0]) # blue
print (family_ages) # [32, 38, 37, 30, 64, 63]
family_ages.append(0) #Adds 0 to end of family_ages.
print (fav_movies['Predestination']) # 2014


#Exercise 2
print('\nExercise #2')
print (fav_colours[-1]) # orange

pop_cities['San Francisco'] = 884400 #Adds a new city to the dictionary.

coin_flips.reverse() #Reverses the order of the list.

print(pop_cities['Toronto']) # 2930000

for artist in fav_artists:
    print(f'I think that {artist} is awesome!') #Prints five times; once for each artist.


#Exercise 3
print('\nExercise #3')
print(fav_artists[0:2]) # ['Nightwish', 'Pink Floyd']

for movie, year in fav_movies.items():
    print(f'\'{movie}\' came out in {year}.') #Prints three times; once for each movie.

family_ages.sort(reverse = True) #Sorts from smallest to biggest, then reverses the order.

fav_movies['Beauty and the Beast'] = [1991, 2017] #Adds to the end of the dictionary.


#Exercise 4
print('\nExercise #4')

for age in family_ages:
    if (age < 40):
        print(age) #Prints five times; each age less than 40.

print(max(family_ages)) # 64

coin_flips.count('heads') # 3

fav_artists.pop(3) #Removes 'Kamelot' from the list.

pop_cities['Toronto'] = 101101101 #Changes the value in the dictionary.


#Exercise 5
print('\nExercise #5')
print(sum(pop_cities.values())) # 104912101

for name, age in sibling_ages.items():
    if (age >= 40):
        print(f'{name} is a senior.') #Prints two times; each person older than 40.
    else:
        print(f'{name} is just an adult.') #Prints five times; each person younger than 40.

print(fav_colours[-2:]) # ['Red', 'Orange']

family_ages = [age + 1 for age in family_ages]
print(family_ages) # [65, 64, 39, 38, 33, 31, 1]

fav_colours.extend(['Cobalt', 'Silver']) #Adds Cobalt and Silver to the end of the list.


#Exercise 6
print('\nExercise #6')

more_movies = { 'Blank Panther':2018, 'Thor':2011, 'Captain Marvel':2019, 'Harry Potter and the Philosopher\'s Stone':2001, 'Split':2016, 'The Avengers':2012, 'Shazam!':2019, 'Logan':2017, 'Big Hero 6':2014 } #Creates a new dictionary with movie names and years.

phone_buttons = [ [1, 2, 3], [4, 5, 6], ['*', 0, '#']] #Creates a nested list that contains phone buttons.

countries = [ {'name':'Canada', 'continent':'North America', 'island':'no'}, {'name':'Ireland', 'continent':'Europe ', 'island':'yes'}, {'name':'Austrailia', 'continent':'Austrailia', 'island':'yes'} #Creates a nested list that contains dictionaries about 3 different countries.
]