##Lists
'''
new_list=[2,6.5,"aviram hanan",[]]
print(new_list)
#print(type(new_list))

new_list2=new_list+[77,"Hello World"]
print(new_list2)
new_list3=new_list+new_list2*2
print(new_list3)
'''

my_list=[1,2,28,5.6,"aviram hanan"]
print("My Age : " + str(my_list[2])) #הדפסת אחד מהתאים שאנחנו בוחרים

my_list2=list("1234567")
print(my_list2) #הדפסת list עם סוגריים עגולים

my_string= "A".join(my_list2) #join כלומר הכנסת תווים בתוך התאים לאחר כל אות או מספר
print(my_string)

my_string2="Hello aviram How Are You"
my_list3=my_string2.split() #מפצל את הכל למערך, ושם כל מילה בתא משלו
print(my_list3)

my_list4=["hello", 1, 55.5, "Aviram"]
print("\n" + str(my_list4))
print("The length is: " + str(len(my_list4))) #len כותב את מספר התאים שברשימה

my_str="\n12346548648978465"
print(my_str)
print("The length is: " +str(len(my_str))) #len כותב את מספר התאים שבסטרינג

#append הוספת מלים או מספרים לסוף הרשימה
my_list4.append("wow")
my_list4.append("aviram")
print("\n" + str(my_list4))
print("The length is: " + str(len(my_list4)))

my_list4.insert(5,"dudu") #מכניס לתא מספר 5 את השם dudu
print(my_list4)

my_list4.pop(4) # מציין איזה תא להוציא (למחוק) מהרשימה
print(my_list4)

my_list5=["google", "facebook", "ebay","apple"]
print("net4u" in my_list)


#my_list2=my_list
#print(my_list2*2) # list מכפיל פעמיים את