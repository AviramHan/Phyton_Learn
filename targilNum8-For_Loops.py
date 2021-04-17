from time import sleep
#For loops

#for x in range(1,10): #אם כותבים את (10) בצורה כזאת הוא יתחיל מ-0
#    print(x)
#    print("wow\n")

'''
list_aviram=["banana","apple","mango"]
for x in range (len(list_aviram)):
    print(list_aviram[x]) '''

#for x in range(1,10,3): # אם כותבים את (1,10,3) הוא יספור בקפיצות של 3
#    print(x)
#    print("wow\n")

print("Now we will get all the details about your class: \n")
for i in range(2):
    name=input("Enter a name: ")
    age=input("Enter an age: ")
    phone=input("Enter a phone: ")
    print("Printing student number " +str(i+1) + " Details...\n")
    sleep(3)
    print("Full name: " + name + "\nAge: " +str(age) + "\nPhone: " + phone + "\n-------------\n")

print("\nBye Bye")