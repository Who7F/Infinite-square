def NumvValidation(message):
    userInput = ''
    while isinstance(userInput, int) == False:
        try:
            userInput = int(input(message))
        except ValueError:
            print('Error: user input is not an integer')
    return userInput

def main():
    number = NumvValidation('Number:')
    
    SqNum = 0
    for i in range(int(number)):
        SqNum = SqNum + i + i + 1
        print(SqNum)

if __name__ == "__main__":
    main()
