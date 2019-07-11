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
print (fav_movies['Predestination']) #2014


#Exercise 2
print('\nExercise #2')
print (fav_colours[-1]) #orange
pop_cities['San Francisco'] = 884400
coin_flips.reverse()
print(pop_cities['Toronto']) #2930000

for artist in fav_artists:
    print(f'I think that {artist} is awesome!') #Prints five times; once for each artist.