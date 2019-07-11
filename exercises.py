#Exercise 0

#Lists
fav_colours = ['blue', 'black', 'red', 'orange']
family_ages = [32, 38, 37, 30, 64, 63]
coin_flips = ['heads', 'tails', 'heads', 'heads', 'tails']
fav_artists = ['Nightwish', 'Pink Floyd', 'Hawkwind', 'Kamelot', 'Tool']

#Dictionaries
unique_words = { 'polypod': 'a many-legged animal', 'gamophobia': 'the fear of marriage', 'logodaedalus': 'an artificer in words' }
fav_movies = { 'Ex Machina': 2014, 'Back to the Future':1985, 'Predestination':2014 }
pop_cities = { 'Boston': 685100, 'Toronto':2930000, 'Halifax':431500, 'Hamburg':1810000 }
sibling_ages = { 'Lucas':38, 'Erin':37, 'Kathleen':30, 'Justin':30, 'Patrick':31 }


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