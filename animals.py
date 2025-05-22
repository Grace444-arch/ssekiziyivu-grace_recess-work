animals =["cow", "goat", "lion" , "elephant","tiger", "leopard"]
animals.sort()#ascending order
print(animals)
animals.sort(reverse= True)#descending order
print(animals)
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
for animal in animals_with_a:
    print(animal)