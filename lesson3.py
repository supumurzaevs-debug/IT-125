data_tuple=("h", 6.13, "C", "e", "T", True, "k", "e", 3, "e", 1, "g")
data_tuple = list(data_tuple)
letters=[]
numbers=[]


for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
    

numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1, 2 )
numbers.sort()
letters.reverse()


letters[1] = "V"
letters[2] = "o"
letters[3] = "l"
letters[4] = "l"
letters[5] = "e"
letters[6] = "y"
letters[7] = "B"
letters[8] = "a"


word = ["l", "l"]
letters.extend(word)
      

letters=tuple(letters)
numbers=tuple(numbers)

print (letters)
print (numbers)