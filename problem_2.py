# Write a program that prints the number from 1 to 100. But for multiples of three print “Fizz”
# instead of the number & for the multiples of five print “Buzz”. However, for numbers which are
# multiples of both three and five print “ FizzBuzz” instead.

for i in range(1,101):
    if i%5==0 and i%3==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)