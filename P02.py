def computeCommission(totalsales):
    if totalsales<=50000:
        return 0
    else:
        return 0.05*totalsales

def remark(totalsales):
    if totalsales>=80000:
        return "Excellent"
    elif totalsales>=60000 and totalsales<80000:
        return "Good"
    elif totalsales>=40000 and totalsales<60000:
        return "Average"
    else:
        return "Work Hard"

if __name__ == '__main__':
    totalSales = []

    week1 = int(input("Sales in first week : "))
    totalSales.append(week1)
    week2 = int(input("Sales in second week : "))
    totalSales.append(week2)
    week3 = int(input("Sales in third week : "))
    totalSales.append(week3)
    week4 = int(input("Sales in fourth week : "))
    totalSales.append(week4)

    salesManData= (sum(totalSales), computeCommission(sum(totalSales)), remark(sum(totalSales)))

    print()
    print("Total Sales :", salesManData[0])
    print("Commission  :", salesManData[1])
    print("Remarks     :", salesManData[2])
    
