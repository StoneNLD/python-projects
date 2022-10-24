
import operator

allowed_operators={
      "+": operator.add,
      "-": operator.sub,
      "*": operator.mul,
      "/": operator.truediv}

def calculate(int1, operator, int2):
    if type(int1) != int: 
        #and  and type(int2) != int:
        print("input error")
    elif type(int2) != int:
         print("input error")
    elif operator not in allowed_operators:
        print("input error")
    else:
        print(int((allowed_operators[operator](int1,int2))))


calculate(14,"*",7)