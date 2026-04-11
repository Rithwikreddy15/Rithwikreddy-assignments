#checking even or odd

num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#largest of three numbers
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a > b and a > c:
    print("Largest is", a)
elif b > c:
    print("Largest is", b)
else:
    print("Largest is", c)  

# print 1 to 50
for i in range(1, 51):
    print(i)

num = int(input("Enter number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i += 1
print("Factorial:", fact)


# check prime number
num = int(input("Enter number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime")
else:
    print("Not Prime")


#  sum of digits
num = int(input("Enter number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Sum of digits:", sum)


# reverse a number
num = int(input("Enter number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed number:", rev)


# even numbers 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)


#  break and continue
for i in range(1, 11):
    if i == 5:
        continue
    if i == 9:
        break
    print(i)


# largest element in list
lst = [10, 20, 5, 40, 25]
print("Largest:", max(lst))


# remove duplicates
lst = [1, 2, 2, 3, 4, 4, 5]
lst = list(set(lst))
print(lst)


#sort list
lst = [5, 2, 8, 1]
lst.sort()
print("Ascending:", lst)

lst.sort(reverse=True)
print("Descending:", lst)



# count occurrences
lst = [1, 2, 2, 3, 2, 4]
x = int(input("Enter element: "))
print("Count:", lst.count(x))



#merge two lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


#create and access tuple
t = (10, 20, 30)
print(t[0], t[1], t[2])


# length of tuple
t = (1, 2, 3, 4)
print(len(t))


# tuple to list
t = (1, 2, 3)
lst = list(t)
print(lst)


#  max and min
t = (5, 2, 9, 1)
print("Max:", max(t))
print("Min:", min(t))


#  tuple unpacking
t = (1, 2, 3)
a, b, c = t
print(a, b, c)


# create set and add elements
s = {1, 2, 3}
s.add(4)
print(s)


# union, intersection, difference
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)


# remove duplicates using set
lst = [1, 2, 2, 3, 4]
print(list(set(lst)))


# check element in set
s = {1, 2, 3}
x = int(input("Enter element: "))

if x in s:
    print("Exists")
else:
    print("Not Exists")


# common elements
a = [1, 2, 3]
b = [2, 3, 4]

print(list(set(a) & set(b)))


# create dictionary
d = {"name": "Ram", "age": 25}
print(d["name"], d["age"])


#frequency of characters
s = input("Enter string: ")
d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)


# merge dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)


# key with max value
d = {"a": 10, "b": 25, "c": 15}
print(max(d, key=d.get))


#iterate dictionary
d = {"a": 1, "b": 2, "c": 3}

for k, v in d.items():
    print(k, v)

 
