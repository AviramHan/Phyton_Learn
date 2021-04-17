#Dictionary
'''
my_dict={"www.google.co.il":"8.8.8.8", "www.facebook.com":"10.10.2.2", "www.youtube.com":["5.5.5.5","4.4.4.4"]}
my_dict2={"www.net4uc.com":"12.12.12.12",}
print(my_dict)
print(my_dict2)
my_dict.update(my_dict2)
print(my_dict)

print("Number of Entries: " + str(len(my_dict)))
print(my_dict["www.google.co.il"])
print(my_dict.values()) #print all Values of my_dict
my_dict["www.google.co.il"]="8.8.4.4" #Change of Value
print(my_dict["www.google.co.il"])
print(my_dict)
'''

my_dict={"www.google.com":"8.8.8.8", "www.facebook.com":"10.10.2.2", "www.youtube.com":"www.google2.com"}
print("www.google.com" in my_dict) #Search of Key
print("www.google2.com" in my_dict.values()) #Search of Values













