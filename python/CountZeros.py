def countZeros(num):
    """
    This function calculates number of zeros in given factoial
    Example: Zeros in 10! is 2 
    """
    count = 0
    div = 5
    while(div <= num):
        count = count + (num / div)
        div = div * 5
    return count

print 'Zeros in 10! = ', countZeros(10)
print 'Zeros in 100! = ', countZeros(100)    
