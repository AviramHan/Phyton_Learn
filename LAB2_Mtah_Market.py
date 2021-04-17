print("Now we will calculate your marketing: \nPrices:\n----------------\n"
      "Tomato= 3 NIS\nCucamber= 2 NIS\nCola= 5 NIS\nChicken= 20 NIS\n ")
tomatos=int(input("Enter how many tomatos?"))
cucambers=int(input("Enter how many Cucambers?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))

print("\nSummary of your order:\n--------------\ntomatos: " + str(tomatos) + "\ncucambers: " + str (cucambers) + "\ncolas: " + str(colas) + "\nchickens: " + str (chickens))

#sum1=tomatos*3
#sum2=cucambers*2
#sum3=colas*5
#sum4=chickens*20
summary=(tomatos*3)+(cucambers*2)+(colas*5)+(chickens*20)

print("\nYou have to pay: " + str(summary) + " NIS without tax")
#print("\nYou have to pay: " + str(summary*1.17) + " NIS with tax")
print("Sum with fee:" +str("%.2f" % (summary*1.17))+ " NIS with tax") #%.2f אומר שיוציא תוצאה עם 2 ספרות אחרי הנקודה