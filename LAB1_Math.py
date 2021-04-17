num=int(input("Enter a number 4 digits: "))
'''
Alafim=4
Meot=5
Asarot=6
Ahadot=7
'''
#This is Alafim
#print("Alafim:" + str(num//1000))

#This is Meot
#print("Meot:" + str((num%1000)//100))

#This is Asarot
#print("Asarot:" + str((num%100)//10))

#This is Ahadot
#print("Ahadot is:" + str(num%10))

print("Alafim is:" + str(num//1000) + "\nMeot is:"  + str((num%1000)//100)
      + "\nAsarot is:"  + str((num%100)//10) + "\nAhadot is:"  + str(num%10))