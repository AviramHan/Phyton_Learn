#Middle_Exericises
import datetime #targilNum2
from collections import defaultdict, Counter #targilNum10
import collections #targilNum13

#targilNum1
#1. Write a Python program to print the following string in a specific format
#(see the output).
#Sample String : "Net4U, is the best place…in the world" Output :
#"Net4U, is the best place
#…in the world"
print("Net4U, is the best place\n ...in the world")

#targilNum2
#2. Write a Python program to display the current date and time.
#Sample Output :
#Current date and time :
#2014-07-05 14:34:14
x = datetime.datetime.now()
print(x)

#targilNum3
#3. Write a Python program which accepts the user's first and last name
#and print them in reverse order with a space between them.
'''
a=input("Enter Full name: ")
print(a)
print((a[::-1]))
print(' '.join(a[::-1])) '''

#targilNum4
'''
filename = input("Input the Filename: ")
res = filename.split(".")
print ("The extension of the file is : " + repr(res[-1])) '''

#targilNum5
#5. Write a Python program that accepts an integer (n) and computes the
#value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615
'''
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)      '''

#targilNum6
#6. Write a Python program to find whether a given number (accept from
#the user) is even or odd, print out an appropriate message to the user.
'''
num=int(input("Enter a number: "))
print("Results: " + str(num%2))
if(num%2 == 0):
    print("The Number Is Odd")
else:
    print("The Number Is Even") '''

#targilNum7
#7. Write a Python program to convert height (in feet and inches) to 7
#centimeters.
'''
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print("Your height is : %d cm." % h_cm) '''

#targilNum8
#Write a Python program to empty a variable without destroying it.
#Sample data: n=20
#d = {"x":200}
#Expected Output : 0
#{}
'''
n = 20
d = (1,10,"hello")
l = {"abc":123,"www.google.com":12345}

print(type(n)())
print(type(d)())
print(type(l)()) '''

#targilNum9
# Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

#targilNum10
#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'Net4U'
#Expected output: {'N': 1, 'e': 1, 't': 2, '4': 1, 'U': 1}
str1 = 'Net4U'
'''
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
my_dict.update({"t":2})
print(my_dict)
'''

#targilNum11
#11. Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

#targilNum12
#12. Write a Python program to count repeated characters in a string.
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))

#targilNum13
#13. Write a Python program to sum all the items in a list.
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))

#targilNum14

list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list.pop(5)
list.pop(4)
list.pop(0)
print(list)