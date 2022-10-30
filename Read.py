from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
from operator import or_
from xml.dom import minidom
file = minidom.parse('ord.xml')
# print('hello world')
AddOrder = file.getElementsByTagName('AddOrder')
DeleteOrder = file.getElementsByTagName('DeleteOrder')
# print(AddOrder[0].attributes['book'].value)
# for elem in DeleteOrder:
#     print(elem.attributes['orderId'].value)

books = dict()
for ele in AddOrder:
    # print(ele.attributes['book'])
    if ele.attributes['book'].value not in books.keys():
        if ele.attributes['operation'].value=="SELL":
            books[ele.attributes['book'].value]=([],[(ele.attributes['volume'].value,ele.attributes['price'].value)])
        else :
            books[ele.attributes['book'].value]=([(ele.attributes['volume'].value,ele.attributes['price'].value)],[])
    else:
        if ele.attributes['operation'].value=="SELL":
            books[ele.attributes['book'].value][1].append((ele.attributes['volume'].value,ele.attributes['price'].value))
        else :
            books[ele.attributes['book'].value][0].append((ele.attributes['volume'].value,ele.attributes['price'].value))



# output:
# print(books)
for key in books.keys():
    print("book: "+key)
    print("BUY--SELL")
    print("=="*20)
    buy=books[key][0]
    sell=books[key][1]
    i=0
    while i<len(buy) or i<len(sell):
        if i<len(buy):
            print(buy[i][0]+"@"+buy[i][1],end="")
        print("--",end="")
        if i<len(sell):
            print(sell[i][0]+"@"+sell[i][1],end="")
        print('')
        i+=1



now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)