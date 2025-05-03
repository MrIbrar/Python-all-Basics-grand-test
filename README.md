# 🐍 Python Basics – Dictionary, Set, List, and Tuple (20 Marks)

This document contains practice questions and answers covering four fundamental Python data structures: **Dictionaries**, **Sets**, **Lists**, and **Tuples**. Each section includes both **conceptual questions** and **code examples**, useful for students learning Python fundamentals.

---

## 📚 Section A: Dictionary (5 Marks)

### ✅ Q1. Add a key-value pair `"name": "Amit"` to a dictionary named `student`

```python
student = {}
student.update({"name": "Amit"})
print(student)  # Output: {'name': 'Amit'}
```

### ✅ Q2. Output of `len({"a": 1, "b": 2})`

**Answer:** `2`

### ✅ Q3. Update the value of key `"age"` in dictionary `person` from `25` to `30`

```python
person = {"age": 25}
person.update({"age": 30})
print(person)  # Output: {'age': 30}
```

### ✅ Q4. Can a dictionary have duplicate keys?

**Answer:** No

### ✅ Q5. What does `dict.keys()` return?

**Answer:** It returns all keys in the dictionary

---

## 🧮 Section B: Set (5 Marks)

### ✅ Q6. How do you create an empty set?

**Answer:** `(b) s = set()`

### ✅ Q7. Add `"apple"` to a set named `fruits`

```python
fruits = set()
fruits.add("apple")
print(fruits)  # Output: {'apple'}
```

### ✅ Q8. Output of `s = {1, 2, 3, 2, 1}`

**Answer:** `{1, 2, 3}`

### ✅ Q9. Are sets ordered collections?

**Answer:** No

### ✅ Q10. Can sets contain duplicate values?

**Answer:** No

---

## 📋 Section A: Lists (5 Marks)

### ✅ Q1. Create a list named `colors` with `"red"`, `"green"`, `"blue"`

```python
colors = ["red", "green", "blue"]
print(colors)
```

### ✅ Q2. Change the second item in `nums = [10, 20, 30]` to `25`

```python
nums = [10, 20, 30]
nums[1] = 25
print(nums)  # Output: [10, 25, 30]
```

### ✅ Q3. Output of:

```python
a = [1, 2, 3]
a.append(4)
print(a)  # Output: [1, 2, 3, 4]
```

### ✅ Q4. Remove the last element from a list

```python
a = [1, 2, 3]
a.pop()       # OR
del a[2]      # OR
a.remove(3)
```

### ✅ Q5. Can lists contain different data types?

**Answer:** Yes

---

## 📦 Section B: Tuples (5 Marks)

### ✅ Q6. Create a tuple `fruits` with `"apple"`, `"banana"`, and `"cherry"`

```python
fruits = ("apple", "banana", "cherry")
```

### ✅ Q7. Output of:

```python
t = (5, 10, 15)
print(t[1])  # Output: 10
```

### ✅ Q8. Can you change the value of an element in a tuple?

**Answer:** No, tuples are immutable

### ✅ Q9. Method to count occurrences in a tuple

**Answer:** `.count()`

### ✅ Q10. Difference between list and tuple (1 sentence)

**Answer:** Lists are mutable (changeable), while tuples are immutable (unchangeable after creation).

---

## 🧠 Summary

This practice file is helpful for understanding:

* When to use **dictionary** for key-value mappings
* Why **sets** are useful for unique collections
* How **lists** allow dynamic, ordered storage
* What makes **tuples** fixed and reliable
