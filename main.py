import math

def getinputs():
    inputs = []
    # n = int(input("What is the highest order term?\t"))
    # for i in range(n, 0, -1):
    #     inp = int(input(f"What is the constant of the x^{i} term?\t"))
    #     inputs.append([inp, i])
    ended = False
    while not ended:
        power = int(input("What is the power of the term?\t"))
        constant = int(input(f"What is the constant of the x^{power} term?\t"))
        inputs.append([constant, power])
        l = input("Do you want to add another term? (y/n)\t")
        if l == "n":
            ended = True
    return inputs

def differentiatestring(constant, power):
    # differentiate with the power rule into a string in terms of x
    if constant == 0:
      return ""
    if power == 1:
      return f"{constant}"
    if power == 2:
      return f"{constant*power}x"
    return f"{constant*power}x^{power-1}"

def differentiate(constant, power, point):
    # differentiate with the power rule into a number at a given x
    return constant*power * math.pow(point,power-1)

def main():
    print("This is the Differentiation Calculator for Polynomials using the Power Rule and Constant Rule")
    inputs = getinputs()

    c = int(input("Do you want to find the derivative at a value (1) or find the derivative in terms of x (2)?\t"))
    if c == 1:
        point = int(input("What is the value of x?\t"))
        ans = 0
        for i in inputs:
            res = differentiate(i[0], i[1], point)
            ans = ans + res
        print(ans)
    elif c == 2:
        out = ""
        for i in inputs:
            res = differentiatestring(i[0], i[1])
            if len(res) == 0:
                continue
            if res[0] == "-":
                out = out + res
            else:
                out = out + "+" + res
        
        print(out)

main()
