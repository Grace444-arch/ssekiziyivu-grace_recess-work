

def factorial(num):
    if num==1:
        return 1
    elif num==0:
      return 0
    else:
     return factorial(num-1)*num

print(factorial(5))