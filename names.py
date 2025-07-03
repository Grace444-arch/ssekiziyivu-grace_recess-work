people = ["grace", "edrine", "winfred", "mugabe", "Melvin"] #list of five names
print(people[1]) #print the second name
people[0] = ("DENIS") #changing the first item 
print(people)
people.append("david")#add new sixth item 
print(people)#print new list
people.insert(3,"Bathel")#add item bathel at index 3
print(people)
del people[4]#delete 4th item from the list
print(people)
print(people[-1])# use negative indexing to print the last element 