x = ("samsung", "iphone", "tecno", "redmi")
favorite = "samsung"
   
if favorite in x:
    print("My favorite phone brand is:", favorite)
else:
    print("My favorite phone brand is not in the list.")

# This line must not be indented unnecessarily
print(x[-2])  # Will output: tecno
x[1] = ("itel")
print(x)