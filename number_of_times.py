def file_reader() :
    infoFile = open("file.txt", "r") #open text file and read it
    empty = [] #empty array
    for number in infoFile:
        empty.append(int(number))
    return empty



#print(arr)

'''
def welcome_user(empty) :
    print("Welcome to put Group Project")
    num = int(input("Please enter number here : "))
    empty.append(num)
    return empty

element = welcome_user(empty)
print(element)

def number_if_time(arr)
el = empty.count
'''
def number_of_times(arr) :
    count = empty.count(25)
    return count
    
arr = file_reader()
elss = number_of_times(arr)
print(elss)

#print(count)