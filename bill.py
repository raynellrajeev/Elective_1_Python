stock={'Pen':5,'Book':3,'Scale':7,'Eraser':10}
price={'Pen':10,'Book':50,'Scale':5,'Eraser':12}
print("Items Available are: ")
itemno=1
bill={}
for i in stock:
    print(itemno,".",i)
    itemno+=1
choice=True
while choice!=False:
    ino=int(input("Enter the item number you want to purchase: "))
    qty=int(input("Enter the quantity you want to purchase: "))
    if ino==1:
        if stock['Pen'] >qty:
            stock['Pen']=stock['Pen']-qty
            bill['Pen']=qty*price['Pen']
        else:
            print("Not Available")
    elif ino==2:
        if stock['Book'] >qty:
            stock['Book']=stock['Book']-qty
            bill['Book']=qty*price['Book']
        else:
            print("Not Available")    
    elif ino==3:
        if stock['Scale'] >qty:
            stock['Scale']=stock['Scale']-qty
            bill['Scale']=qty*price['Scale']
        else:
            print("Not Available")
    elif ino==4:
        if stock['Eraser'] >qty:
            stock['Eraser']=stock['Eraser']-qty
            bill['Eraser']=qty*price['Eraser']
        else:
            print("Not Available")
    else:
        print("Invalid choice")
    choice=eval(input("Do you want to continue (True/False): "))

print("Bill: ")
sum=0
for i in bill:
    print(i,": $",bill[i])
    sum+=bill[i]
print("Total: $",sum)


