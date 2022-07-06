#!/usr/bin/env python
# coding: utf-8

# ANSWER 1:

# In[3]:


###CREATING A FILE
f=open('example.txt','w')
f.write("This is a placement assignment")
f.close()


# ![image.png](attachment:image.png)

# In[4]:


def replaceString(file):
    f = open(file, 'r')
    content = f.read()
    f.close()
    content = content.replace('placement', 'screening')
    f = open(file, 'w')
    f.write(content)
    f.close


# In[5]:


replaceString('example.txt')


# ![image.png](attachment:image.png)

# In[ ]:





# ANSWER 2

# ABSTRACT CLASS

# In[1]:


class Person:
    def __init__(self, name, surname, salary):
        self.name = name 
        self._surname = surname         # _ single underscore means protected
        self.__salary = salary   # __ double underscore means private
    
    def getName(self, current_year):
        return self.name + ' ' + self._surname
    
    def __str__(self):
        return "%s %s and salary is %d."                 % (self.name, self._surname, self.__salary)
    
person1 = Person("Souradeep", "Bhattacharya", 713204)
print(person1)


# In[2]:


person1.__dict__


# In[3]:


print(person1.name, person1._surname, person1._Person__salary)


# MULTIPLE INHERITANCE

# In[4]:


class A:
    def method1(self):
        print("Class A inside method1")


# In[5]:


## Class B inheriting base class A
class B(A):
    def method1(self):
        print("Class B inside method1")
        
## Class C inheriting base class A
class C(A):
    def method1(self):
        print("Class C inside method1")
    def method2(self):
        print("Class C inside method2")


# In[6]:


## Class D inheriting base class B and C
class D(B,C):
    def method1(self):
        print("Class D inside method1")


# In[7]:


obj_d = D()


# In[8]:


obj_d.method1()
obj_d.method2()


# In[9]:


B.method1(obj_d)


# In[10]:


A.method1(obj_d)


# DECORATOR

# Decorators allows to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

# In[12]:


def decorator(func):
    def inner_function(*args, **kwargs):
        
        print("Before Execution")
        
        returned_value = func(*args, **kwargs)
        
        print("After Execution")
        
        # returning the value to the original frame
        return returned_value
    
    return inner_function


# adding decorator to the function
@decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

# getting the value through return of the function
print("Sum =", sum_two_numbers(a=10, b=20))


# In[ ]:




