names_money={"idan":20000, "ben":10000, "dudu":15000, "aviram":26000, "yuval":15000}
print(names_money)
summary=names_money["ben"]+names_money["yuval"]
print("The summary is: " + str(summary))
#names_money["yoel"]=summary
#print(names_money)
names_money.update({"yoel":summary})
print(names_money)
print("Number of entries: " + str(len(names_money)))
print("idan" in names_money)









#names_money["dudu2"]=40000 #אופציה להוסיף עוד שם לדיקשן