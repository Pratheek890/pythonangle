# This is the notes of corey schefer python playlist tutorials 

# Lecture 1 is all about installing the python 
- print() - to print something as output
- input() - to get anyting as input

# Lecture2 -  Strings 
String is the basically text,character enclosed in "" or '' sometimes """ """

- len() = is a built in length command to count the length of string list etc etc 
- indexing [starting_value(n) : ending_index(n-1):skipping index] 
# String methods
- to get lower case .lower() 
- to get upper case .upper()
- to count .count()
- to get first letter capital = .capatalize()
- to finding character or text .find()
- to get first letter capital .title()
- .startswith() returns true if anything is starting with 
- .endswith() returns true if anything is ending with it
- .replace() - replaces the word with the other element
- strip() - removes the white spaces right an left 
- .split() - one long string and chops it up into smaller, individual strings.

# string concatenation and replication
- * is used as replication 
- + is used a string concatenation
# string formating
- format string f,'{}{}' is used to format string variable name inside {} 
- r', - raw string doesnt have filer 
- .format() - string formating  
# helping commands
dir() - shows all the method we can work with the particular datatype
help() - gives information and description of the method do 

# Lecture 3 - Integer and float
- no need to enclose with quotes to integer or floating value or else it will be string 
- Intger = whole number displayed by (int)
- float = whole number + decimal number diplayed by (float)
- complex = realnumber + apperent number (ex: 3+5j)

# arthematic operation 
- + -= addition
- - = substraction
- * = multiplication
- / = division
- // = floor division return the whole number of quotient
- % = modulo returns reminder
- ** = exponention or you can use pow()
- python used BODMAS way to calculate

# increment or decrement 
- += 1 increment by 1
- -= 1 decrement by 1 

# built in function 
- abs() = absolute - removes the negatice number
- round() - rounds the value to nearest integer

# Imp  question
= - assigemnt operator
== - comparison operator

# comparison operator
- == - equals to
- > - less than
- < - greater than 
-  != - not equal to 
- >= - greater than or equal to 
- =< - less than or equal to 
- object identity = is - check th value of same id  
# type casting 
int() - convert to integer
float() - convert to float
str() - convert to string  


# Lecture 4 - List tuple and sets 
- list, tuple are allowed to work for sequential data 
- set are unordered collection with no duplicates
# List 
- enclosed in []
- index start from 0 from start
- to access the last item -1 is used 
- list are mutable (we can alter the list)
# list methods
- reverse() - to reverse list
- sort() - sort based on aplhabetic order
-  index() - returns the index number
# - in operator checks whether the element is present or not - returns only true or not 
# to add
- .append('argument') - to add one items at once
- .insert(index_number  , "argument")-to add to specific index
- .extend() - to add multiple values to list 
# to remove
- .remove("argument") - remove the passed argument
- .pop()  - it removes the element present at last & it can return the element removes
# One trick to reverse using sort 
- .sort(reverse = True)
- if you dont want to alter the sorted list 
use this reference example 
- # if you dont want to alter the original list
example1 :
courses1 = ['History','Math','Physics','CSE','EE']
sorted_course = sorted(courses1)
print(sorted_course)

# min,max,sum
- this operation is performed primarly on numberic list
- min - returns the minimum number present in the list
- max - returns the maximun number present in the list
- sum - returns the sum of number present in the list 

# to access the index and value in the list 
 - we used enumerate function

# Tuples 
- enclosed in ()
- non-mutable (we cannot change once written)

# Set
- enclosed in {}
- no duplicates unordered 
- to create empty set  use set()
# Memebership operator 
- in 
- not in 

# union,intersection,differenciation
- set_1.union(set_2)   = #union of two sets
- set_1.intersection(set_2)  = #intersection of two sets 
- set_2.difference(set_1)  = #difference of two sets

# Lecture 5 : Dictionaries

- we use key-value pair enclodes in {'key' : value}
- key - unique identifier , value-data(defination of the word )
# Dictionary methods
- get(key, defaukt_values|this is optional ) method = to get the value of the key 
- update({}) = to update the dictionary
- del dictionary_name('Key that needs to be updates')
- to remove key we can use pop('key_name')
- to know the no of keys len()
- dictionary.key() - returns the keys
- dictionary.values() - returns the values
- to get key-value pair .items()
- some operation from lines 101 to 120 lines in corey1.py 

# Lecture 6: Conditional statement 
- if ,else,elif 
- if - executes when it meets the condition 
- else - alternate to it statemnt when its false
- elif - multiple if statements 
# example code : Corey2.py

# and , or , not  - Boolean operator 
- and = when both statemnts are True
- or = when any one statement is true
- not = switches from false to true and true to false

-  id() - keyword to get the identity number of element
-  
 # lecture 7 : Loops and iteration
- for and while loops 
- for loop - iterate to certain number of values 
- range()/range(n,n-1,skipping values)  - to go through loop fir certain number of times in a loop with numerical values  #5 in corey2.py
- break - breaks the loop 
- continue - continues to iterate in loop

- while loop - iternate until certain condition is met
- += increment
- -= decrement

