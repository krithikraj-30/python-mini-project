print("MENU")
print("1.idly-2pcs- ₹19")
print("2.dosa-1- ₹35")
print("3.chapathi-2pcs- ₹25")
print("4.poori-2pcs- ₹39")
print("5.vada-1- ₹5")
print("6.chicken biriyani- ₹129")
print("7.chickenfried rice- ₹149")
print("8.parotta-2pcs- ₹39")
print("9.kothu parotta- ₹99")
print("10.mutton biriyani- ₹159")
print("0.exit")
    
total=0

while True:
    choice=int(input("enter your choice:"))
    
    if choice==0:
        break
    elif choice==1:
        item="idly"
        price=19
    elif choice==2:
        item="dosa"
        price=35
    elif choice==3:
        item="chapathi"
        price=25
    elif choice==4:
        item="poori"
        price=39
    elif choice==5:
        item="vada"
        price=5
    elif choice==6:
        item="chicken biriyani"
        price=129
    elif choice==7:
        item="chickenfried rice"
        price=149
    elif choice==8:
        item="parotta"
        price=39
    elif choice==9:
        item="kothu parotta"
        price=99
    elif choice==10:
        item="mutton biriyani"
        price=159
    else:
        print("not available")
        continue

    quantity=int(input("enter the quantity"))
    cost=quantity*price
    total=total+cost

    print(item,"=",cost)

discount=0

if total>1000:
    discount=100

print("\nBILL")
print("Total=",total)
print("Discount=",discount)
print("final amount=",total-discount)
print("THANK YOU,COME AGAIN")

        
