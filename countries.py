countries =["england", "uruguay", "france", "uganda", "germany","spain"]
country2 = countries.copy()#creating a copy from the original list
print(countries)
print(country2)
for country in countries:#loop through the items
    print(country)

countries.sort()#sorting in ascending order 
print(countries)
countries.sort(reverse=True)#sorting in descending order
print(countries)