myInput = input("Enter the bills sequence : ")
bills = myInput.split(",")
myBills = []
print(feasible(bills,myBills))

def feasible (bills,myBills):
    result = "YES"
    billsR = bills
    for bill in bills:
        if (bill == "$5"):
            myBills.append("$5")
            billsR.remove(bill)
        elif (bill == "$10"):
            if(myBills.count("$5")>= 1):
                myBills.remove("$5")
                myBills.append("$10")
                billsR.remove(bill)
            else:
                result = "NO"
                break
        elif (bill == "$15"):
            if(myBills.count("$10")>= 1):
                myBills.remove("$10")
                myBills.append("$15")
                billsR.remove(bill)
            elif(myBills.count("$5")>= 2):
                myBills.remove("$5")
                myBills.remove("$5")
                myBills.append("$15")
                billsR.remove(bill)
            else:
                result = "NO"
                break
        elif (bill == "$20"):
            billsR.remove(bill)
            myBills.append("$20")
            if(myBills.count("$15")>= 1):
                temp = myBills
                temp.remove("$15")
                a = feasible(billsR,temp)
            if(myBills.count("$10")>= 1 & myBills.count("$5")>= 1):
                temp = myBills
                temp.remove("$10")
                temp.remove("$5")
                b = feasible(billsR,temp)
            if(myBills.count("$5")>= 3):
                temp = myBills
                temp.remove("$5")
                temp.remove("$5")
                temp.remove("$5")
                c = feasible(billsR,temp)
            if(a == "NO"& b == "NO" & c == "NO"):
                result = "NO"
                break
        else:
            billsR.remove(bill)
            myBills.append("$25")
            if(myBills.count("$15")>= 1 & myBills.count("$5")>=1):
                temp = myBills
                temp.remove("$15")
                temp.remove("$5")
                a = feasible(billsR,temp)
            if(myBills.count("$10")>= 1 & myBills.count("$5")>= 2):
                temp = myBills
                temp.remove("$10")
                temp.remove("$5")
                temp.remove("$5")
                b = feasible(billsR,temp)
            if(myBills.count("$5")>= 4):
                temp = myBills
                temp.remove("$5")
                temp.remove("$5")
                temp.remove("$5")
                temp.remove("$5")
                c = feasible(billsR,temp)
            if(myBills.count("$10")>= 2):
                temp = myBills
                temp.remove("$10")
                temp.remove("$10")
                d = feasible(billsR,temp)
            if(a == "NO"& b == "NO" & c == "NO" & d == "NO"):
                result = "NO"
                break
            else:
                break
            
    return result
    