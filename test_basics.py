# Section A: Dictionary (5 Marks)

# (1 mark) How do you add a new key-value pair to a dictionary named student with key "name" and value "Amit"?
Answer no 01
student = {
    
}

student.update({"name": "Amit"})
print(student)

# (1 mark) What will be the output of this code?
Answer no 02:
    The output of this code is 2

# (1 mark) Write a code snippet to update the value of key "age" in dictionary person from 25 to 30.
Answer no 03
person = {
    "age": 25
}

person.update({"age": 30})
print(person)


# (1 mark) Can a dictionary have duplicate keys? (Yes/No)
Answer no 04:
    No


# (1 mark) What does dict.keys() return?
Answer no 05:
    It return all keys in Dictionary

#  Section B: Set (5 Marks)

# (1 mark) How do you create an empty set?
# (a) s = {}
# (b) s = set()
# (c) s = []

Answer no 06:
    (b) s = set()

# (1 mark) Write code to add "apple" to a set named fruits.
Answer no 07
fruits = set()
fruits.add("apple")
print(fruits)

# (1 mark) What will be the output of:
# s = {1, 2, 3, 2, 1}
Answer no 08:
    The output of these code is: {1,2,3}

(1 mark) Are sets ordered collections? (Yes/No)
Answer no 09:
    NO

(1 mark) Can sets contain duplicate values? (Yes/No)
Answer no 10:
    No


# Section A: Lists (5 Marks)
# (1 mark) How do you create a list named colors with values "red", "green", and "blue"?
Answer no 01:
colors = ["red", "green", "blue"]
print(colors)


# (1 mark) Write Python code to change the second item in a list nums = [10, 20, 30] to 25.
Answer no 02:
nums = [10, 20, 30]
nums[1] = 25
print(nums)


# (1 mark) What is the output of this code?
# a = [1, 2, 3]
# a.append(4)
# print(a)
Answer no 03:
The output of this code is [1,2,3,4]


# (1 mark) How do you remove the last element from a list in Python?
Answer no 04:
a = [1, 2, 3]
a.pop()
print(a)

# another method
a = [1, 2, 3]
del a[2]
print(a)

# another method
a = [1, 2, 3]
a.remove(3)
print(a)


# 1 mark) Can lists contain elements of different data types? (Yes/No)
Answer no 05:
    Yes ists contain elements of different data types.


#  Section B: Tuples (5 Marks)
# (1 mark) How do you create a tuple named fruits with "apple", "banana", and "cherry"?
Answer no 06:
fruits = ("apple", "banana", "cherry")


# (1 mark) What will be the output of this code?

# t = (5, 10, 15)
# print(t[1])
Answer no 07:
The output of this code si 10


# (1 mark) Can you change the value of an element in a tuple? (Yes/No)
Answer no 08:
No we can't change the value of an element in a tuple because tuple is a immutable


# (1 mark) What method can be used to count how many times an item appears in a tuple?
Answer no 09:
The count() method can be used to count how many times an item appears in a tuple


# (1 mark) What is the difference between a list and a tuple in one sentence?
Answer no 10:
The difference between a list and a tuple is a List is mutable which means changeable time by time while tuple is Immutable which means cannot change when it created