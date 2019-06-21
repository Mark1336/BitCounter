#Bit Counter

#Setting Origin numbers and temporary number
originNum = 2
tempNum = 2

#ADD: input section for max bit amount

while originNum <= 256:
    print(originNum)

    originNum += tempNum
    tempNum = originNum

#Sample Output:
#2
#4
#8
#16
#32
#64
#128
#256
