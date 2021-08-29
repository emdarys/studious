'''
A linear equation solver over the operations: addition, subtraction, multiplication, and division.
'''

def main():


   #using exception handling and while loop

    equation = input("Enter the equation or press 'q' to quit: ") 

    while equation != "q":
        try:
            ans = eqnSolver(equation)

            if ans == "123":
                print("Division by zero is not permissible!!")
            else:
                print("The value of the variable is ", ans)
        except:
            print("Please follow the format!! Format: Variable is always x and the equation is always linear. e.g 2/x=3 ") 

        equation = input("Enter the equation or press 'q' to quit: ") 

    print("Bye!")
    exit()

def eqnSolver(eqn):

    #finding indices of operations

    findEqual = eqn.find("=")
    variable = eqn.find("x") #the variable must be x
    findPlus = eqn.find("+")
    findSub = eqn.find("-")

    findMultiply = eqn.find("*")
    findDivide = eqn.find("/")

    na = "123"

#if x is on left side
    if findEqual > variable:
        
        #separating equations on the basis operations

        if "+" in eqn:
            if findPlus < findEqual and findPlus > variable:
                num1 = int(eqn[findPlus:findEqual])
                num2 = int(eqn[findEqual+1:])
                answer = num2 - num1
                #print("x =", num2 - num1)

            elif findPlus < findEqual and findplus < variable:
                num1 = int(eqn[0:findPlus])
                num2 = int(eqn[findEqual+1:])
                answer = num2 - num1
                #print("x =", num2 - num1)

            else:
                num1 = int(eqn[findEqual+1:findPlus])
                num2 = int(eqn[findPlus+1:])
                answer = num2 + num1
                #print("x =", num2 + num1)

            
        elif "-" in eqn:
            if findSub < findEqual and variable < findSub:
                num1 = int(eqn[findSub+1:findEqual])
                num2 = int(eqn[findEqual+1:])
                answer = num2 + num1
                #print("x =", num1 + num2)

            elif findSub < findEqual and variable > findSub:
                num1 = int(eqn[0:findSub])
                num2 = int(eqn[findEqual+1:])
                answer = num1 - num2
                #print("x =", num1 - num2)

            else:
                num1 = int(eqn[findEqual+1:findSub])
                num2 = int(eqn[findSub+1:])
                answer = num1 - num2
                #print("x =", num1 - num2)

        elif "*" in eqn:
            if findMultiply < findEqual and variable < findMultiply:
                num1 = int(eqn[findMultiply:findEqual])
                num2 = int(eqn[findEqual+1:])
                if num1 == 0:
                    return na
                answer = num2/num1
                #print("x =", num2/num1)

            elif findMultiply < findEqual and variable > findMultiply:
                num1 = int(eqn[0:findMultiply])
                num2 = int(eqn[findEqual+1:])
                if num1 == 0:
                    return na
                answer = num2/num1
                #print("x =", num2/num1)

            else:
                num1 = int(eqn[findEqual+1:findMultiply])
                num2 = int(eqn[findMultiply+1:])
                answer = num2*num1
                #print("x =", num1 * num2)

        elif "/" in eqn:
            if findDivide < findEqual and variable < findDivide:
                num1 = int(eqn[findDivide+1:findEqual])
                num2 = int(eqn[findEqual+1:])
                answer = num2*num1
                #print("x =", num1*num2)
            
            elif findDivide < findEqual and variable > findDivide:
                num1 = int(eqn[0:findDivide])
                num2 = int(eqn[findEqual+1:])
                if num2 == 0:
                    return na
                answer = num1/num2
                #print("x =", num1/num2)

            else:
                num1 = int(eqn[findEqual+1:findDivide])
                num2 = int(eqn[findDivide+1:])
                if num2 == 0:
                    return na
                answer = num1/num2
                #print("x =", num1/num2)

#if x is on  right side
    elif findEqual < variable:

        #separating equations on the basis operations

        if "-" in eqn:
            if findSub > findEqual and findSub > variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findSub+1:])
                answer = num1 + num2
                #print("x =", num1 + num2)

            elif findSub > findEqual and findSub < variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findEqual+1:variable])
                answer = num2 - num1
                #print("x =", num2 - num1)

            else: #because x is on the other side so in this case the numbers must be on left side
                num1 = int(eqn[0:findSub])
                num2 = int(eqn[findSub+1:findEqual])
                answer = num1 - num2
                #print("x =", num1 - num2)

            
        elif "+" in eqn:
            if findPlus > findEqual and findplus > variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findPlus+1:])
                answer = num1 - num2
                #print("x =", num1 - num2)

            elif findPlus > findEqual and findplus < variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findEqual+1:variable])
                answer = num1 - num2
                #print("x =", num1 - num2)

            else: #because x is on the other side so in this case the numbers must be on left side
                num1 = int(eqn[0:findPlus])
                num2 = int(eqn[findPlus+1:findEqual])
                answer = num1 + num2
                #print("x =", num1 + num2)


        elif "*" in eqn:
            if findMultiply > findEqual and findMultiply > variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findPlus+1:])
                if num2 == 0:
                    return na
                answer = num1/num2
                #print("x =", num1/num2)

            elif findMultiply > findEqual and findMultiply < variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findEqual+1:variable])
                if num2 == 0:
                    return na
                answer = num1/num2
                #print("x =", num1/num2)

            else: #because x is on the other side so in this case the numbers must be on left side
                num1 = int(eqn[0:findMultiply])
                num2 = int(eqn[findMultiply+1:findEqual])
                answer = num1 * num2
                #print("x =", num1 * num2)
    

        elif "/" in eqn:
            if findDivide > findEqual and findDivide > variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findDivide+1:])
                answer = num1*num2
                #print("x =", num1*num2)

            elif findDivide > findEqual and findDivide < variable:
                num1 = int(eqn[0:findEqual])
                num2 = int(eqn[findEqual+1:variable])
                if num1 == 0:
                    return na
                answer = num2/num1
                #print("x =", num2/num1)

            else: #because x is on the other side so in this case the numbers must be on left side
                num1 = int(eqn[0:findDivide])
                num2 = int(eqn[findDivide+1:findEqual])
                if num2 == 0:
                    return na
                answer = num1/num2
                #print("x =", num1/num2)

    return answer
            

main()
