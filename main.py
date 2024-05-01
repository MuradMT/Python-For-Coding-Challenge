#This Repo covers only differences between python and other languages
#Basic things is not adressed
#Key points of python is demonstrated



#-Some tips in python:
# Get number dynamically from screen in python: n = int(input())
# numbers = [int(num) for num in input().split(" ", n)]
# print(numbers)
#Or do like this(generally this used in eolimp):
#num=list(map(int,input().split()))
#for _ in range(MAX)]-if you want loop without index use this
#0<m<n-you can write statements like this
#input.strip()-strip method same with c# trim
#print(f"{arr[0] + arr[1]:.4f}")-you can write-string format with f or use .format(x,y)
# four decimal places of float number
#print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))-align text with > to right 3 space 
#formatting expressions d(int),f(float),s(string)
#add in front of string letter text=letter+text
#add in end of text  of string letter text=text+letter

#print(type(('a')))-type keyword checks the type of variables

#name:str='Murad'->it is python variable annotation by type,you explicitly say it to your program
#at first import typing,otherwise it wont work

#print(7+4.5)->this is implicit conversion example
#print('8'+str(7))->this is explicit conversion example

#Statement vs expression difference
#age=iq/5 -> iq/5 is expression,age=iq/5 is statement

#for i in range(3):
#    print('hello',end=' ')
#end->helps you to write codes in the same line and do not create new line

#mylist=[1,2] 
#print(mylist[::-1])
#prints array in reversed form

#Sorted build in function
#time_list = [12, 2, 32, 19, 57, 22, 14]
#print(sorted(time_list))
#print(time_list)

#Min Max build in function
# time_list = [12, 2, 32, 19, 57, 22, 14]
# print(min(time_list))
# print(max(time_list))

#we can do branching with conditionals such as if


#map(function, iterables)->structure of map
#example of map
#def square(x):
#   return x*x
#numbers=[1, 2, 3, 4, 5] 
#sqrs_of_numbers=map(square, numbers)

#zip example
#numbers = [1,2,3]
#str_numbers = ['One','Two','Three']
#result = zip(numbers, str_numbers)

#slicing and striding examples
# x='hello world'
# print(x[0::2])
# print(x[0:6:2])
# print(x[::1])
# print(x[::-1])

#recursion->imagine you are in a queue,there are 6 person here
#last person ask in front of him how many people left after  you
#and when you finish to latest one,then you come back with answers
#this is how recursion works
# def factorial(n):
#   if n < 2:
#     return 1
#   return n * factorial(n-1)

#finding power of number with recursion
def is_power_of(number, base):
 # Base case: when number is smaller than base.
    if number <base:
        # If number is equal to 1, it's a power (base**0).
        return False
    elif number==base:
        return True
    # Recursive case: keep dividing number by base.
    return is_power_of(number//base, base)


#Section 1-Variables

#Comments created with #,shortcut for comments is ctrl+/,
#if you do this shortcut again,then it will uncomment your code
#-Variables are dynamicly typed
n=0
print('n=',n) #comma automatically adds gap
n='89gh'
print('n=',n)


#-Get inputs from screen
name=input() # gets string from screen
num=int(input()) # gets integer from screen
names=input().split() # obtains strings from screen at the same line
n,m=map(int,input().split()) # obtains integers from screen at the same line


#-Multiple Assigment
n,m='0','900'
print(n+m) # cannot concatenate int and string
#for instance n=0 m='0' n+m throws error


#-Increment
n=n+1#available
n+=1#available
#n++ not permissible in python


#-None is null
n=0
n=None
print('n=',n)


#Section 2-Conditional Statements

#-If,Elif,Else
#in one line condition you don't need to have paranthesis
n=15
if n>0:
    print(1)
elif n<0:
    print(0)
else:
    print(-1)


#-Ternary operator python
n=int(input())
print("ODD" if n%2!=0 else "EVEN")


#-Logical Operators
#and-&& or-||
#in multi line condition you need paranthesis
m,k=9,0
if m>0 and k>0:
    print(1)
elif m<0 and k<0:
    print(0)
elif m==0 or k<0:
    print('y')
elif ((m>=9 or k==0)
        and m+k>0):
    print('n')


#Section 3-Loops

#-While loop
n=5
while n>0:
    print(n)
    n-=1


#-For Loop
#looping from i=0 to i=4
for i in range(5):
    print(i)
#looping from i=2 to i=5
for i in range(2,6):
    print(i)
#looping from i=5 to i=20 with specific increment number(5)
for i in range(5,21,5):
    print(i)


#Section 4-Math

#-Division
print(5/2) # decimal
print(5//2) # integer
print(-3//2) # round down
print(int(-3/2)) # obtained desired result with casting

#-Modulo
print(10%3) #gives anticipated vestige
print(-10%3) #gives wrong result,2
#in order to prevent this situation,we solve this problem like beneath:
import math
print(math.fmod(-10,3))


#-Math library helper methods,fmod have mentioned before
import math
print(math.floor(3/2)) #result is decimal
print(math.ceil(3/2))
print(round(2.3)) #traditional rounding comes built-in ,without any dependency to math library
print(math.pow(2,2)) #2**2 is also an operator and alternative for this pow function
print(math.sqrt(16))


#-Infinity
print(math.pow(2,500)<float('inf'))
# Float('inf') shows the infinity,but i reckon that it would not be used anywhere
#just know about it


#Section 5- Arrays (called lists in python)
#Can be used as a stack
#-Create and print array
#access and modify elements of array-the complexity would be O(1)
arr=[1,2,3]
print(arr[len(arr)-1]) #len(arr) gives us a length of array
arr[0]=19
print(arr) # prints like this [19,2,3]
print(*arr) # prints like this 19 2 3
n=5
arr1=[1]*n #one of the ways of array creation in python
print(arr1)
print(arr[-1]) #negative values get the latest value of array


#-Array Methods(append,pop,insert)
arr.append(4) #it adds at the end of array
arr.append(5)
arr.pop() #it removes the last element of array
print(arr.pop()) #it shows the removed item as a other c based languages
print(arr)
arr.insert(1,7) #it allows us to add element to a specific index
#The complexity for this function is O(N)
print(arr)


#-Array Slicing(creates the sublists)
arr=[1,2,3,4]
print(arr[0:-1])


#-Array contains with in operator
arr=[1,2,3,4]
print(1 in arr) #returns true


#-Unpacking
a,b,c=[1,2,3] #the length of array and the variables count must be same,otherwise we will obtain error
print(a)#it likes javascript array destruction
arr=[1,2,3]
[d,e,f]=arr
print(e)


#-Loop through one array
num=[1,2,3,4]
for i in range(len(num)):#if you want to have index, this way is unchangeable
    print(num[i])
for n in num:#if you want to have element, this way is unchangeable
    print(n)
for i,n in enumerate(num):#if you want both of index and element, this way is unchangeable
    print(i,n) #in python you can print something at the same line in this way,it creates gap automatically


#-Loop through multiple arrays
num=[1,2,3,4]
arr=[4,5,6,7]
for n1,n2 in zip(num,arr):
    print(n1,n2)


#-Array reverse and sort for numbers
num=[1,2,33,4]
num.reverse() #reversing array
num.sort() #sorting array
print(num)
num.sort(reverse=True) #helps us to sort in reverse order,simplifies the code which has been written above
print(num)


#-Array sorting for strings
names=['murad','comes','to','home','at','9pm']
names.sort() #sorts in alphabetical order
print(names)
names.sort(key=lambda x:len(x)) #sorting based on the length of array elements
print(names)


#-List Comprehension
arr=[i for i in range(5)] # iterates through loop and adds it's elements to array
#it is a shorthand and helps us so much
print(arr)
#another example
arr1=[i**i for i in range(5)]
print(arr1)


#-2D Arrays-i only show the syntax
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)
arr1=[[0 for i in range(5)] for j in range(5)]
print(arr1)
print(arr1[0][0]) #access to 2d array elements


#-Copy in Arrays
#it can not applied to  array which  don't contains at least one object inside it
#for instance,[1,2,3] you can't see corollary if you try to use copying
import copy
arr=[1,2,[3,5],4,5]
sarr=copy.copy(arr) # shallow copy,changes on parent array impacts the child
darr=copy.deepcopy(arr) # deep copy,changes on parent array don't impact the child
arr[2][0]=7
print(sarr)
print(darr)


#Section 6-Strings(virtually same with arrays)

#-String General
name='murad' #or "murad"
print(name.index('m'))->gives specific position of character
print(name[0:2])#string slicing
#strings is immutable,we can't do this:name[0]='hi'
name+='xy' # concatenates new word to existing string ,complexity would be O(N)
print(name)
print(int("123")+int("123")) # we obtain 246,it is possible in python
# also opposite is true,but it concatenates numbers
print(str(123)+str(123))
# it is just a little casting conjuring :)
print(ord('a'))  # gives us ascii table position of character
print(len(name)) # same with array
strings=['mu','r','ad']
myname=''.join(strings) #  all array items was congagrated by join function and created a new united string
#''.join->'' says that what is the connector you can use ',' like this
print(myname)
#you can look at on internet for useful string methods,
# this knowledge is enough to tackle with string problems
#string methods
print(name.upper())# lower
print(name.strip())#rstrip lstrip
print(name.split())
print(name.endswith('e')) #startswith
print(name.isnumeric()) #'12345' is true
print(name.isalpha())#checks if all text is contains only characters
print(name.count('e'))
print(name.replace('a','hello'))
print(name.rfind('a'))#->lastindexof


#Section 7-Queue

#-General Queue
from collections import deque
queue=deque()
queue.append(1) # adds to the end of queue
queue.append((2))
queue.appendleft(3) #adds to the start of the queue
queue.pop() #removes from end
queue.popleft()#removes from start
print(queue)
print(queue[0]) #access element
print(len(queue))



#Section 8-HashSet

#-General HashSet
myset=set()
mset={1,2,3,4} # Both writing type of set  is correct
myset.add(1)
myset.add(2)
myset.remove(2)
print(mset)
print(myset)
print(len(myset)) #length of set
print(1 in mset) # it is same with array.
# in looks like to includes in javascript or contains in c#
print(set([1,1,2,3,4])) # obtains list and returns a new set
nset={i for i in range(5)} # set comprehension
print(nset)


#Section 9-HashMap(aka dictionary)

#General HashMap
altmap={'x':1,'y':2}
print(altmap)
mymap={}
mymap['murad']=20
mymap['some']=25
mymap['haphazard']=30
mymap.pop('some')
print(mymap)
print(len(mymap))
print(mymap['murad'])
print('murad' in mymap)
compmap={f"{i}":i**i for i in range(3)} # Dictionary comprehension
print(compmap)
#f{} is looks like to c# string interpolation($"{}")
# or javascript template literals(`${}`)

#Looping through map
mymap={'1':1,'2':2,'3':3}
for key in mymap: # both key and values
    print(key,mymap[key])
for val in mymap.values(): # only values
    print(val)
for key,val in mymap.items(): # same with the first writing
    print(key,val)


#Section 10-Tuples(it is immutable array)

#-General Tuple
tup=(1,2,3)
print(tup[0])


#Section 11-Heap

#-General Heap
import heapq
minheap=[]
heapq.heappush(minheap,3) #adds to heap,but in a sensible way,always maintains the ascending order
heapq.heappush(minheap,1),
heapq.heappush(minheap,2) #1 2 3 is order
print(minheap[0]) # min value will be always at the first index
while len(minheap):
    print(heapq.heappop(minheap)) #removes from heap
#if you add negative numbers,you can find max element with the help of multiplying number to -1
#the minimum one will be the len-1
arr=[1,2,3,4,5]
heapq.heapify(arr) #gives us opportunity to approach array as a heap
while arr:
    print(heapq.heappop(arr))


#Section 12-Functions

#-General functions
def Add(x,y):
    #Simple Function
    print(x+y)
Add(4,5)
def outer(a,b):
    #Nested Function
    c=9
    def inner():
        return a+b+c
    return inner()
print(outer(1,2))
def double(arr,val):
    def helper():
        for i,n in enumerate(arr):
            arr[i]*=2
        nonlocal val # helps us to reach the parent function parameter
        val*=2
    helper()
    print(arr,val)
arr=[2,4]
val=3
double(arr,val)


#Section 13-Class
class MyClass:
     #constructor
     def __init__(self,nums): #self look like to this,we must provide it in each  functions
         #it is mandatory parameter,you can name it whatever you want
          self.nums=nums
          self.size=len(nums) #this syntax also loks like to javascript,practically same
     def getLength(self):
         return self.size
     def getPow(self):
         return self.getLength()**self.getLength()
ins=MyClass([1,2,3,4])
print(ins.getLength())
