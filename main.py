# python oop

# class myClass:
#     x = 10

# c1 = myClass() 
# print(c1.x)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


# p1 = Person('Rahim',20)
# print(p1.name)
# print(p1.age)


#inheritance


# parent class
# class Person:
#     def __init__(self,firstname,lastname):
#         self.firsname = firstname
#         self.lastname = lastname

#     def fullname(self):
#         print(self.firsname,self.lastname)  


# p1 = Person("Karim","Islam")
# p1.fullname()




# child class

# first method= how child class inherite the parent class->  by using "pass" keyword


# class Student(Person):
#     pass

# s1 = Student("John","Doe")
# s1.fullname()



# second method= how child class inherite the parent class->  by using "__init__" function
# class Student(Person):
#     def __init__(self,firstname,lastname):
#         Person.__init__(self,firstname,lastname)
    
       


# s1 = Student("Rahim","Islam")
# s1.fullname()


# third method= how child class inherite the parent class->  by using "super" function

# class Student(Person):
#     def __init__(self,firstname,lastname):
#         super().__init__(firstname,lastname)



# s1 = Student("Karim","Islam")
# s1.fullname()


# final of inheritance

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def fullname(self):
#         print(self.firstname,self.lastname)    



# class Student(Person):
#     def __init__(self,firstname,lastname,graduationyear):
#         super().__init__(firstname,lastname)
#         self.graduationyear = graduationyear
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 

# s1 = Student("Rahim","Islam",2018)
# s1.fullname()
# s1.welcome()
# print(s1.graduationyear)


# module
# import mymodule
# mymodule.greeting("John")
# person = mymodule.person1
# print(person)


# Naming a Module
# import mymodule as mx
# mx.greeting("John")
# print(mx.person1)


# Import From Module
# from mymodule import person1
# from mymodule import greeting

# print(person1)
# greeting("John")

# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# print(y)


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y) 

# user_list = [
#     {
#         "user_id":1,
#         "name":"rahim"
#     },
#     {
#         "user_id":2,
#         "name":"karim"
#     }
# ]


# user_ids = []

# for user_dict in user_list:
#     if "user_id" in user_dict:
#         user_ids.append(user_dict["user_id"])
# print(user_ids)  


# text = "Hello, World!"
# result = text.split()  # By default, split at spaces
# print(result)

# def caluculate (a:int,b:int):
#     return a*b

# value = caluculate(2,10)
# print(value)




# final example of inheritance

# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#     def FullName(self):
#         print(self.fname, self.lname)    
   

# p1 = Person("Habib","Islam")
# print(p1.fname)
# print(p1.lname)
# p1.FullName()

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)


# class Teacher(Person):
#     def __init__(self, fname, lname,year):
#         super().__init__(fname, lname)
#         self.year = year
#     def graduationYear(self):
#         print(f"graduatoin year is {self.year}")


# s1 = Student("Karim","Islam")
# print(s1.fname)
# print(s1.lname)
# s1.FullName()
# t1 = Teacher("Karim","Islam",2018)
# print(t1.fname)
# print(t1.lname)
# print(t1.year)
# t1.FullName()
# t1.graduationYear() 

# module
# from greeting import greetingHello
# hello = greetingHello('John')
# print(hello)

# split method
# text = "apple,orange,banana"
# result = text.split(",")
# print(result)

# join method
# delimiter = "-"
# word = ["orange","banana","apple"]
# result = delimiter.join(word)
# print(result)

# delimiter = " "
# word = ["orange","banana","apple"]
# result = delimiter.join(word)
# print(result)