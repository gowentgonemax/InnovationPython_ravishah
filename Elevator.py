from random import randint
currentElevatorPosition = 0

def RequestElevator (userCurrentFloor):
    pass

def upDirection(userCurrentFloor):
    isValid = False
    floorCount =0
    floorChoice = {1: '1st Floor', 2: '2nd Floor', 3: '3rd Floor', 4: '4rth Floor',5:'5th Floor',6:'6th Floor',7:'7th Floor'}
    while not isValid:
        for key, value in floorChoice.items():
            print(key, ' : ', value)
        userFloorChoice: int = int(input('Which floor would you like to go? :'))
        if userFloorChoice > 0 and userFloorChoice < 8:
            isValid = True
            if userFloorChoice == userCurrentFloor:
                print('You are on the same floor')
            else:

                global currentElevatorPosition
                print(currentElevatorPosition, userFloorChoice)
                if currentElevatorPosition < userFloorChoice:

                    while currentElevatorPosition != userFloorChoice:
                        currentElevatorPosition += 1
                        print('Current elevator at ',currentElevatorPosition,' position')
                else:
                    print('You need to go down direction')

        else:
            print('We don\'t have that floor in our building')
            isValid = False
    print('Elevator position',currentElevatorPosition)



if __name__ == "__main__":
    currentElevatorPosition = randint(1,7)
    print('Current Elevator Position',currentElevatorPosition)
    liftDirection = ['UP', 'DOWN']
    for i in liftDirection:
        print(i)
    upDownOption = int(input('Please, Select the option 1 for UP or 2 for Down: '))
    userCurrentFloor = int(input('Enter you Current floor from(1-7): '))

    if upDownOption == 1:
        print('You have selected UP direction')
        upDirection(userCurrentFloor)
    elif upDownOption == 2:
        print('You have selected DOWN direction')
    else:
        print('Wrong Choice')
    print('Elevator door is opening')
