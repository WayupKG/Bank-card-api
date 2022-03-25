import random

def sumNum(number):
    return number//10+number%10

def luna(cardNumber):
    evenNumbers = cardNumber[::2]
    oddNumbers = list(cardNumber[1::2])
    sumOddNumbers = 0
    for i in oddNumbers:
        sumOddNumbers+=int(i)
    k, summ = 0, 0
    for i in evenNumbers:
        k = int(i)*2
        summ+=sumNum(k)
    return(summ+sumOddNumbers)%10 

def generateCardNumber(series):
    bincards = {'ELCARD': 941718, 'VISA': 417749, 'MASTERCARD': 517851}
    result = str(bincards[series.upper()])
    for i in range(7,16):
        random.seed()
        result+=str(random.randint(1,9))
    for i in range(0,9):
        if(luna((result+str(i)).replace(" ",'')) == 0):
            result+=str(i)
            return result
