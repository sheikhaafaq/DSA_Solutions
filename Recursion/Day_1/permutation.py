#----------------- PERMUTATION ---------------------------
def permutation(lst):

	# If list is empty
	if len(lst) == 0:
		return []

	# If element in list is only 1, one permutation is possible
	if len(lst) == 1:
		return [lst]

	# find permutation if more than 1 elements are in list

	l = [] #list that will store current permutation

	#
	for i in range(len(lst)):
	    x = lst[i]

	    # remaining list
	    remLst = lst[:i] + lst[i+1:]

	    # Generating all permutations where m is first
	    # element
	    for p in permutation(remLst):
		    l.append([x] + p)
	return l


# Driver program to test above function
data = list('123')

print(permutation(data))