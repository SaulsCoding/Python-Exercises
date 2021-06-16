#def myList(lists) :
    #for x in lists :
       # print(x)

#spam = ['apples', 'bananas', 'tofu', 'cats']
#spam[-2] = 'dogs'

#myList(spam)
#from collections import Counter

#import Counter
'''def file_reader() :
    infoFile = open("file.txt", "r") #open text file and read it
    numbers = [] #empty array
    for number in infoFile:
        numbers.append(int(number))
    return numbers


arr = file_reader()
print(arr)'''

#def welcome_user() :
   # print('Welcome to our Group Project')
    #n= int(input("Please enter a number : "))
    #arrs = []
    #for i in range(n) :
        #arr.append
    


#element = welcome_user()
    
#print(element)
'''
person = {
    'key': 'value',
    'name': 'Kalob',
    'language': 'Python'
}

print(person['key'])'''


#groceries = ["Milk", "Eggs", "Ice cream"]
# tuplate cannot change
#tuplates
'''kids = ('Nathan', 'Zephyr')
print(type(kids))'''

#Set
#foods = {"Pizza", "Tacos", "Ice Cream", "Pizza", "Tacos", "Pizza"}

#Indexing
'''course = "Python 3 Crash Course"
print(course[7])
print(course[9:14])'''

'''foods = ["Pizza", "Dr. Pepper", "Chicken"]
print(foods[1:]) #starts at index 1 and display that rest
primt(foods[:1]) # get everything until item 1 number'''

#dox string
'''def thing():
    """     
    Hello
    """ '''
    #Files
    #create new file and write to it
'''with open("try_me.py", "w") as file_handler :
    file_handler.write("Print('Hello World lololol')")
    file_handler.close()

with open("try_me.py", "r") as fh:
    content = fh.read()
    fh.close()
    print(content)
#good practice to close the file

#append to a file
with open("try_me.py", "a") as fhs :
    fhs.write("\nTesting line #2")
    fhs.close()'''

# \n is a invisible character - make new lines
'''total = None

if total is None :
    print("Is none")

num = 30

if num == 30 :
    print('hi')
elif num == 20 :
    print("bye")
else :
    print("ciao")'''

'''groceries = ['Milk', 'Eggs', 'Ice Cream']
for item in groceries :
    print(item)'''

name = " Python 3 Crash Course"
#name = name.strip()
#print(name)
    
'''for letters in name :
    print(letters)'''

# if the lowercase letter is a vowel then print it out
'''for letter in name:
    l = letter.lower()
    if l in 'aeiouy':
        print("Vowel is : " + l)
        continue
    if l == "3" :
        print("Breaking on 3")
        break'''

'''num = 0
while num < 10 :
    print(num)
    num += 1'''

#List Comparisons
'''nums = [1,2,3,4,5,6,7,8,9,10]
#times_ten = [num*10 for num in nums]
#print(times_ten)
times_ten = [num*10 for num in nums if num % 2 == 0]
print(times_ten)'''

#Functions

'''def name():
    return "A thing"

#print(name())
#by default functions return a NoneType

def greeting(name) :
    print(name + ", Hello to you good sir")


names = greeting("Dale")
print(names)'''


'''def greeting(name, greeting="Hello") :
    return name, greeting + " to you"

x = greeting("Bob")
print(x)'''

#Scope
'''name= "Bob"

def hi():
    print(name)

hi()'''

#OOP
'''class Person:
    pass

kalob = Person()

print(kalob)'''

'''class Person:
    name = 'Kalob'

kalob = Person()

print(kalob.name)

# Classes take the first parameter as 'self' perammeter
class Person :
    def speak(self):
        print("I need Tacos")
hunger = Person()
hunger.speak'''

try:
    1/0
except Exception as e:
    print(e)
    print(type(e))

try:
    10 / 0
except ZeroDivisionError:
    print("Cannot do that")








