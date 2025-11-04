command=""
command=input('>').lower()
is_started=False
while True:
    if command=='help':
        guideline="""
        
start - to start the car
stop - to stop the car
exit - to exit
        """
        print(guideline)
        
    elif command=='start':
        if is_started:
            print("Car is already started")
        else:
            print('Car started...ready to go')
            is_started=True
        
    elif command=='stop':
        if not is_started:
            print("Car is already stopped")
        else:
             print('Car stopped')
             is_started=False
       
        
    elif command=='quit':
        print('Quitting...')
        break
    else:
        print('This command is not supported')
    command=input('>').lower()
    