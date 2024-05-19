# Given three numbers X, Y & Z. write a function/method that finds the greatest 
# among the numbers.

def find_max(x,y,z):
    if x>y and x>z:
        return x
    elif y>z:
        return y
    else:
        return z


a,b,c = map(int, input("Enter 3 numbers to calculate max value separated by space: ").split())
print(find_max(a,b,c))








#alternative approach : using python built-in max function