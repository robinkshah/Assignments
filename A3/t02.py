posint = int(input("Enter a positive three digit integer: "))
#if i can divide the integer by 10, 100 , get the remainder isolate the digits e.g 123
d1 = posint % 10
#print(d1)
d2 = ( posint % 100 ) // 10
#print(d2)
d3 = posint // 100
#print(d3)
product = d1 * d2 * d3
print(f"The product of the three digits in the integer ({posint}) is: {product}")
