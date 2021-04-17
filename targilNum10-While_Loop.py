#while loops
from time import sleep

while(True):
    choice=input("Menu:\n-----\n1.Insert Number and ** it by 3\n2.Insert 4 IPS to a list and print it\n"
                 "3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if string Polindrom\n")
    if(choice=="1"):
        print("The new number is: " + str((int(input("Enter a number: ")))**3))
    elif(choice=="2"):
        list_ip=[]
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        print("The new list: \n----------\n" +str(list_ip))
    elif(choice=="3"):
        dns_dict={}
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
        print("The new Dictionary DNS:\n-----------\n" + str(dns_dict))
        break
    elif(choice=="4"):
        word=input("Enter a Word: ")
        if (word == word[::-1]):
            print("This is polindrom! ")
        else:
            print("This isn't polindrom!")
    else:
        print("Enter 1-4 only!!...\n")
    exit=input("Do you want to exit? y/n\n")
    if(exit=="y" or exit=="yes"):
        break
    else:
            print("Welcome back!\n")

print("Thank You and bye bye")

'''
while(true):
    name=input("Enter a name: ")
    if(name=="idan"):
        print("Hello Idan")
        break
    elif(name=="ben")
        continue
    else:
        print("Where is Idan?")
        
    number=int(input("Enter is number: "))
    print(number*4)
    
print("Bye Bye...")    
'''

'''
num=int(input("Enter a number: "))
while(!=7):
    print(nunm*100)
    num = int(input("Enter a number: "))
'''
'''
counter=10
while(counter>0):
    print(counter*100)
    print("Idan Hakimi")
    counter=counter-1
'''