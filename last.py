sum = 0
choose = -1


def addMoney():
    global sum
    print('Please write an amount: ')
    n = int(input())
    sum += n
def getMoney():
    global sum
    print('Write an amount: ')
    check = int(input())
    if sum - check >= 0:
        sum -= check
    else:
        print('You have not such amount money')

def convert():
    global sum
    print('IN KZT: ', sum * 470)

while(choose != 0):
    print('Please choose one of the options: ')
    print('0: EXIT')
    print('1: Add Money')
    print('2: Get Money')
    print('3: Convert to KZT')
    print('4: Show my Money')
    print('Your choise: ')
    choose = int(input())
    if choose == 1:
        addMoney()
    elif choose == 2:
        getMoney()
    elif choose == 3:
        convert()
    elif choose == 4:
        print('MY MONEY: ', sum)
    elif choose != 0:
        print('please write an appropriate number')