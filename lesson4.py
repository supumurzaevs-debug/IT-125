flags = {
    'ru': {'red blue', 'white'},
    'kg': {"red yellow", 'red'},
    'ua': {"red blue", 'red', 'blue'},
    'uk': {"yellow", "blue"},
    'kz': {'blue yellow', 'blue'},
    'ger': {'black red' 'yellow'},
    'arm': {'red blue', 'yellow'}
}
while True:
   

    color=input('enter the color of the flag:')
    if color == 'exit': 
        print("end")
        break 
    if color in flags ['ru']:
        print ('ru')
    if color in flags ['kg']:
        print ('kg')
    if color in flags ['ua']:
        print ('ua')
    if color in flags ['uk']:
        print ('uk')
    if color in flags ['kz']:
        print ('kz')
    if color in flags ['ger']:
        print ('ger')
    if color in flags ['arm']:
        print ('arm')

    
    
