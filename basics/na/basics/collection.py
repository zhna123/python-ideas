# atomic data types
print(2**10)
print(7//3)
print(7%3)
print(3//7)
print(3%7)
print(7/3)

# collections

# list
myList = [0] * 6
print(myList)

myList = [1, 2, 3, 4] * 3
print(myList)

print(list(range(10)))
print(list(range(5, 10, 2)))
print(list(range(10, 5, -1)))

# strings -- immutable
myName = "NatAlie"
print(myName * 3)
print(myName.center(10))
print(myName.split("a"))

# tuple -- immutable
myTuple = (2, True, 4.5)
print(myTuple[0:2])

# set -- unordered
mySet = {"cat", True, 3}
print(mySet)
print("cat" in mySet)

# dictionary
scores = {"Jon" : 100, "Lily" : 98, "Naomi" : 97}
# print(scores)
# print(scores["Naomi"])
# scores["Micheal"] = 96
# print(scores)

# i is the key
for i in scores:
    print(scores[i], " is the score of ", i)
    print("the score of %s is %d" % (i, scores[i]))

print(scores.keys())
print(list(scores.values()))
print(list(scores.items()))
print(scores.get("sushi", "NO ENTRY"))
print(scores.get("Lily"))
# print out unique letters
# list comprehension
wordlist = ["cat", "dog", "rabbit"];
letterlist = [word[i] for word in wordlist for i in range(len(word))]
print(list(set(letterlist)))
