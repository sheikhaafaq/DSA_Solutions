# Approach :
# if we have only one element [1] in list , we can select it [1] or not select it [].
# Now if we have 2 elements [1,2] in list, we can select it [2] or not [], append it [1,2] or not [1].
# Using same logic and do it recusively.


def powerset(lst , index , currentlst):
    
    if index == len(lst):   # If index of element is greater than length of list
        
        x.append(currentlst)    # Appending current list to the external list
        return 
    
    # add the element to current lsit and increment in index 
    powerset(lst, index + 1, currentlst + [lst[index]])

    # Don't add the to the current list and increament
    powerset(lst, index + 1, currentlst) 


x= list()  # create external list to store all sets

# Calling of powerset function with list[1,2,3], initial index is 0 and empty current lpist 
powerset([1,2,3] , 0, [])

print(x)   #print external list
