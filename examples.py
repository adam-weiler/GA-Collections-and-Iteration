type(["green", "purple", "orange"]) #<class 'list'>

len(["green", "purple", "orange"]) #3

type([1, 15, 7, 4]) #<class 'list'>

len(["hello", 7, True]) 3

type([]) #<class 'list'>


colours = ["green", "purple", "orange"] #returns nothing

type(colours) #<class 'list'>

len(colours) #3

colours[2] #'orange

type(colours[2]) #<class 'str'>

colours[0].upper() #'GREEN'

colours[2] = "yellow"

colours #['green', 'purple', 'yellow']

colours[-1] #yellow

colours[-2] #purple

colours[3] #returns an error


greeting = "hello"

greetings = [greeting, "hi", "what's up?"]

greetings[0] #hello

greetings[1] #hi

number = 2 

greetings[number] #what's up?

greetings[-1] #what's up?


colours = ["red", "purple", "pink"]

len(colours) #3

colours.append("blue")

len(colours) #4

colours #red, purple, pink, blue

colours[0:3] #red, purple, pink

colours[0:2] #red, purple

colours[1:3] #purple, pink

colours[2:3] #pink

colours[2:2] #[]

colours.append("orange")

"purple" in colours #True

"yellow" in colours #False

colours.sort()

colours #Blue, orange, pink, purple, red

grades = [87, 65, 90, 77, 90]

len(grades) #5

grades.sort()

grades # [65, 77, 87, 90, 90]

grades.reverse()

grades # [90, 90, 87, 77, 65]

grades.count(90) #2

grades.count(77) #1

grades.count(100) #0

grades.index(77) #3

grades.index(90) #0

grades.index(100) #ValueError; 100 is not in the list.

max(grades) #90

min(grades) #65

mixed = [1, 2, "A+"] 

min(mixed) #TypeError ; strings and ints.

mixed.sort() #TypeError ; strings and ints.


visible_colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for each_colour in visible_colours:
  print(each_colour)


numbers = [1,5,22,100]

for current_num in numbers:
  # all these steps will happen once for each number:
  double = current_num * 2
  double_plus_one = double + 1
  no_more_than_one_hundred = max(100, double_plus_one)
  message = "Your score is {}%".format(no_more_than_one_hundred)
  print(message)

# un-indent to end the loop
print("This message displays just once after the loop is done")