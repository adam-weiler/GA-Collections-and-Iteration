#Exercise 0

#Q1: Lists
fav_colours = ['Blue', 'Black', 'Red', 'Orange']
family_ages = [32, 38, 37, 30, 64, 63]
coin_flips = ['heads', 'tails', 'heads', 'heads', 'tails']
fav_artists = ['Nightwish', 'Pink Floyd', 'Hawkwind', 'Kamelot', 'Tool']

#Q2: Dictionaries
unique_words = { 'polypod': 'a many-legged animal', 'gamophobia': 'the fear of marriage', 'logodaedalus': 'an artificer in words' }
fav_movies = { 'Ex Machina': 2014, 'Back to the Future':1985, 'Predestination':2014 }
pop_cities = { 'Boston': 685100, 'Toronto':2930000, 'Halifax':431500, 'Hamburg':1810000 }
sibling_ages = { 'Lucas':38, 'Erin':37, 'Kathleen':30, 'Jodi':64, 'Dan':63, 'Justin':30, 'Patrick':31 }


#Exercise 1
print('Exercise #1')

#Q1:
print (coin_flips) # ['heads', 'tails', 'heads', 'heads', 'tails']

#Q2:
print (fav_colours[0]) # blue

#Q3:
family_ages.sort()
print (family_ages) # [32, 38, 37, 30, 64, 63]

#Q4:
family_ages.append(0) #Adds 0 to end of family_ages.

#Q5:
print (fav_movies['Predestination']) # 2014


#Exercise 2
print('\nExercise #2')

#Q1:
print (fav_colours[-1]) # orange

#Q2:
pop_cities['San Francisco'] = 884400 #Adds a new city to the dictionary.

#Q3:
coin_flips.reverse() #Reverses the order of the list.

#Q4:
print(pop_cities['Toronto']) # 2930000

#Q5:
for artist in fav_artists:
    print(f'I think that {artist} is awesome!') #Prints five times; once for each artist.


#Exercise 3
print('\nExercise #3')

#Q1:
print(fav_artists[0:2]) # ['Nightwish', 'Pink Floyd']

#Q2:
for movie, year in fav_movies.items():
    print(f'\'{movie}\' came out in {year}.') #Prints three times; once for each movie.

#Q3:
family_ages.sort(reverse = True) #Sorts from smallest to biggest, then reverses the order.

#Q4:
fav_movies['Beauty and the Beast'] = [1991, 2017] #Adds to the end of the dictionary.


#Exercise 4
print('\nExercise #4')

#Q1:
for age in family_ages:
    if (age < 40):
        print(age) #Prints five times; each age less than 40.

#Q2:
print(max(family_ages)) # 64

#Q3:
coin_flips.count('heads') # 3

#Q4:
fav_artists.pop(3) #Removes 'Kamelot' from the list.

#Q5:
pop_cities['Toronto'] = 101101101 #Changes the value in the dictionary.


#Exercise 5
print('\nExercise #5')

#Q1:
print(sum(pop_cities.values())) # 104912101

#Q2:
for name, age in sibling_ages.items():
    if (age >= 40):
        print(f'{name} is a senior.') #Prints two times; each person older than 40.
    else:
        print(f'{name} is just an adult.') #Prints five times; each person younger than 40.

#Q3:
print(fav_colours[-2:]) # ['Red', 'Orange']

#Q4:
family_ages = [age + 1 for age in family_ages]
print(family_ages) # [65, 64, 39, 38, 33, 31, 1]

#Q5:
fav_colours.extend(['Cobalt', 'Silver']) #Adds Cobalt and Silver to the end of the list.


#Exercise 6
print('\nExercise #6')

#Q1:
more_movies = { 'Blank Panther':2018, 'Thor':2011, 'Captain Marvel':2019, 'Harry Potter and the Philosopher\'s Stone':2001, 'Split':2016, 'The Avengers':2012, 'Shazam!':2019, 'Logan':2017, 'Big Hero 6':2014 } #Creates a new dictionary with movie names and years.

#Q2:
phone_buttons = [ [1, 2, 3], [4, 5, 6], ['*', 0, '#']] #Creates a nested list that contains phone buttons.

#Q3:
countries = [ {'name':'Canada', 'continent':'North America', 'island':'no'}, {'name':'Ireland', 'continent':'Europe ', 'island':'yes'}, {'name':'Belgium', 'continent':'Europe', 'island':'no'} ] #Creates a nested list that contains dictionaries about 3 different countries.


#Exercise 7
print('\nExercise #7')


skateboard_list = []
#Q2:
for i in range(0, 20): #Runs 20 times.
    skateboard_list.append('I will not skateboard in the halls') #Appends the message to the list.
    #Q1:
    print(skateboard_list[i]) #Prints the new message.

#Q3:
one_to_fifty = list(range(2, 50)) #Creates a list of numbers between 1 to 50.
print(one_to_fifty)

#Q4:
new_sum = 0
for num in one_to_fifty: #Runs each item in the one_to_fifty list.
    new_sum += num #Adds each number in the list.
print(new_sum) # 1224

#Q5:
new_list = []
for num in range(1, 51): #Runs from 1 to 50.
    for i in range(3): #Runs 3 times.
        new_list.append(num) #Appends the current num to the new_list. Each number appended three times.
print(new_list) # [1, 1, 1, 2, 2, 2, 3, 3, 3, ... , 50, 50, 50]

#Q6:
new_countries = []
for country in countries: #Runs through each country in the countries list.
    if (country['island'] == "no"): #Checks if current country is not an island.
        new_countries.append(country) #Appends to the new_countries list.
print(countries) #Prints the original list: Canada, Ireland, Belgium.
print(new_countries) #Prints the new list: Canada, Belgium.
#As a bonus, try with a filter


#Exercise 8
print('\nExercise #8')

#Q3:
def sum_of_list(input_list): #Takes a list as input.
    #Q2:
    return(sum(input_list)) #Returns the sum of the list.

#Q1:
my_expenses = [5000, 45, 85, 30.95, 16.50, 82]

print(sum_of_list(my_expenses)) #5259.45
print(sum_of_list([250, 7.95, 30.95, 16.50])) # 305.4