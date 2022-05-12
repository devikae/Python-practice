for i in range(5):
    print('')
    for j in range(i+1):
      print("*", end='')


for i in range(5):
    print('')
    for j in range(5-i):
        print("*", end='')   


for i in range(5):
    print('')
    
    for k in range(i):
        print(" ", end='')      
    
    for j in range(5-i):
        print("*", end='') 



for i in range(6):
    print('')
    
    for k in range(6-i):
        print(" ", end='')      
    
    for j in range(i):
        print("*", end='') 


for i in range(1,6):
    print('')
    
    for k in range(5-i):
        print(" ", end='')      
    
    for j in range(1,i*2):
        print("*", end='') 