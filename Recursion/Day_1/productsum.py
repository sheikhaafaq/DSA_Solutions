
# Here we created a funtion 'prodSum' with arguments array and depth
# depth parameter keep the track of nesting of array 
def prodSum(array,depth = 1 ):
    # Initialize variable sum , store sum of elements
    sum = 0

    for i in array:
        # If element inside array is integer, then element is added to sum variable
        if type(i) is int:
            sum += i

        elif type(i) is list:
            # if element inside array is array/list, then again recusrion occur on that element
            # Also depth is incremented
            sum += prodSum(i, depth + 1)
    #final sum is return in multiplication with depth
    return sum * depth

# Funtion call
array =  [ 5, 2, [7, -1], 3, [6 ,[-13 ,8], 4] ]
print(prodSum(array))