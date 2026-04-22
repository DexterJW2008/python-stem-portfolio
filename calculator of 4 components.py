
        

def main():
    menu = """
1. Volume of a cube
2. PED calculation
3. Percentage change
4. Quit"""
    while True:
        print(menu)
        while True:
            try:
                menuChoice = int(input('Enter a menu choice:'))
                break
            except:
                print("Please enter a number from the menu:")
        if menuChoice ==4:
            break
        elif menuChoice ==1:
            volumeCube()
        elif menuChoice ==2:
            ped()
        elif menuChoice ==3:
            percentageChange()
            

def volumeCube():
    while True:
        try:
            length = float(input('length: '))
            width = float(input('width: '))
            height = float(input('height: '))
            
            volume = length*height*width
            print(f'Volume is {volume} cubic units')
            break
        except ValueError:
            print('only numbers may be entered')
            

def ped():

    num1 = float(input("Enter origional value for quantity demanded"))
    num2 = float(input("Enter second value for quantity demanded"))
    num3 = float(input("Enter origional value for quantity demanded"))
    num4 = float(input("Enter original value for price"))
    num5 = float(input("Enter second value for price"))
    num6 = float(input("Enter origional value for price"))

    difference = num1 - num2
    percentagedif = difference/num3

    difference = num4 - num5
    percentagediff = difference/num6

    print(f"PED: {(percentagedif/percentagediff)}")
    
def percentageChange():
  
     num1 = float(input("Enter original value"))
     num2 = float(input("Enter second value"))
     num3 = float(input("Enter original value"))
     
     difference = num1 - num2
     percentagedif = difference/num3
     
     print(f"Percentage change: {(percentagedif*100)}")

            
            
    

