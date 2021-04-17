# LAB 4
details_list=["Aviram Hanan", 28, "Aviram@gmail.com", "0525123456"]
print("Full Name: " + details_list[0] + "\nAge: " + str(details_list[1]) +
      "\nEmail: " + details_list[2] + "\nMy Phone: " + str(details_list[3]))

ip_list=["192.168.1.1", "192.168.1.2"]
print(ip_list)
ip_list.append("192.168.1.3")
ip_list.append("192.168.1.4")
ip_list.append("192.168.1.5")
print(ip_list)
ip_list.pop(2)
print("IP List Length Is: " + str(len(ip_list)) + "\nAnd the IP List: " + str (ip_list))