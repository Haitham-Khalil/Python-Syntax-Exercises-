command=""
command=input('>').lower()
while True:
    if command=='help':
        guideline="""
        
start - to start the car
stop - to stop the car
exit - to exit
        """
        print(guideline)
        
    elif command=='start':
        print('Car started...ready to go')
        
    elif command=='stop':
        print('Car stopped')
        
    elif command=='quit':
        print('Quitting...')
        break
    else:
        print('This command is not supported')
    command=input('>').lower()
