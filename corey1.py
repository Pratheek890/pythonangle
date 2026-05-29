
# print("Hello, world!")   
# # variable = value
# message  = "        hello to he world of python"

# print(message)
# print(len(message))
# message1 = message.replace("to he" , 'to the')
# print(message1)
# message2 = message1.title().strip()   
# message3 = message1.split()   #convert single text to list 
# print(message2)
# print(message3)
# print(message1.count('h'))   #count the number of h in the mesage 
# print(type(message1))   #check the type of the variable 

# if type(message1) is str:
#     print("Kehooo! ")


# # Lecture 3 - integer and float 
# # type() - returns the type of the value used
# num = 3
# print(type(num))

# numb = 3.25
# print(type(numb))

# numbe = 2+5j
# print(type(numbe))


# # type casting 
# a= int(22.56) #- convert to integer
# b = float(22) #- convert to float
# d = str(12) #- convert to string  
# print(a,b,d)


# lecture 4 - list tuple and set

# courses = ['History','Math','Physics','CSE','EE']
# print(courses)
# print(len(courses))
# print(courses[1])
# courses[1:3] = "Computer science",'Electrical' ,'Electronics'
# print(courses)
# print(courses[::-1])   #slicing the list 
# courses.extend(['Biology','Caed','Embedded system'])  # add the elemtns to the previous defined list
# courses.insert(1 , "DSA")   #insert dsa at 1st index
# courses.sort()   #sort the list based on alphebatic order
# courses.sort(reverse = True)   #reverse sorting the list based on alphebatic order 
# print(courses)
# print('DSA' in courses)
# for course in courses:
#     print(course)

# # if you dont want to alter the original list
# courses1 = ['History','Math','Physics','CSE','EE']
# sorted_course = sorted(courses1)
# print(sorted_course)

# #numeric list
# be = [1,22,14,5,566,42,889,33]
# be.sort()
# be.append(1555)
# print(be)
# a = min(be)
# b = sum(be)
# c = max(be)
# print(a,b,c)

# #to access the index and value in the list 
# #we used enumerate function

# for i ,courses1 in enumerate(courses1):
#     print(i,courses1)



# new_srt= ' * '.join(courses1)
# print(new_srt)


# # tuple
# tuple_1 = ('History','Math','Physics','CSE','EE')
# print(tuple_1)


# #sets are unordered collection with no duplicates
# set_1 = {'History','Math','Physics','CSE','EE','EE','CSE'}
# print(set_1)
# set_2 = {}
# set_2 ={'ARt','Designs','UX','EE'}

# print(set_1.union(set_2))   #union of two sets
# print(set_1.intersection(set_2))   #intersection of two sets 
# print(set_2.difference(set_1))   #difference of two sets


#Dictionary
student = {
    'student_no' : 1,
    'student_name' : "Alex",
    'student_perentage' : 92.78,
    'core_sub' : ['Math','English','Chemistry']
}
student['Phone'] = '89789789'
print(student)
student.update({'student_perentage' : 82.78})
del student['student_no']
print(student)
#get - to access the value of the key
print(student.get('student_name'))

for i ,key in enumerate(student):
    print(i,key)

for key,value in student.items():
    print(key,value,sep = " : ")   

    
     