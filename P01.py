import math as m
def computeAreaAndPerimeter(side1,side2,side3):
    assert (side1<side2+side3) and (side2<side1+side3) and (side3<side1+side2),'''Error :
    Sum of two sides should be greater than third side'''
    # gives assertion error if sum of two side is less than third side
    perimeter = side1+side2+side3
    s = perimeter/2
    area = m.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    result = (perimeter,area)
    return result

if __name__ == '__main__':
    side1 = float(input("Enter the value of side 1 :"))
    side2 = float(input("Enter the value of side 2 :"))
    side3 = float(input("Enter the value of side 3 :"))

    perimeter ,area = computeAreaAndPerimeter(side1,side2,side3)

    print(f"The area of triangle is : {area:.2f}")
    print(f"The perimeter of triangle is : {perimeter}")
