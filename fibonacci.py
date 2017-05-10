#############
#J Plumitallo
#project Eueler problem #2
#############

#
#recursive function to yield the fibonacci number associated with the position in the fibonacci sequence  entered as an argument
def fib( x ):
    
    if( x == 0 ):
        
        return 0
    
    elif( x == 1):
        
        return 1

    else:

        return fib(x-1)+fib(x-2)


#
#summation of all fibonacci numbers afore the 33rd fibonacci number
s = 0

for i in range(34):
    
    if( fib(i)%2 == 0 ):

        s += fib(i)

print s

