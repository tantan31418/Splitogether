# Python3 program to fin maximum 
# cash flow among a set of persons 

# A utility function that returns 
# index of minimum value in arr[] 
def getMin(arr): 
	
	minVal = list(arr.values())[0]
	minKey = list(arr.keys())[0]
	for i in arr: 
		if (arr[i] < minVal): 
			minVal = arr[i]
			minKey = i 
	return minKey 

# A utility function that returns 
# index of maximum value in arr[] 
def getMax(arr): 

	maxVal = list(arr.values())[0]
	maxKey = list(arr.keys())[0]
	for i in arr: 
		if (arr[i] > maxVal): 
			maxVal = arr[i]
			maxKey = i 
	return maxKey 

# A utility function to 
# return minimum of 2 values 
def minOf2(x, y): 

	return x if x < y else y 

# amount[p] indicates the net amount to 
# be credited/debited to/from person 'p' 
# If amount[p] is positive, then i'th 
# person will amount[i] 
# If amount[p] is negative, then i'th 
# person will give -amount[i] 
def minCashFlowRec(amount,payment): 

	# Find the indexes of minimum 
	# and maximum values in amount[] 
	# amount[mxCredit] indicates the maximum 
	# amount to be given(or credited) to any person. 
	# And amount[mxDebit] indicates the maximum amount 
	# to be taken (or debited) from any person. 
	# So if there is a positive value in amount[], 
	# then there must be a negative value 
	mxCredit = getMax(amount) 
	mxDebit = getMin(amount) 

	# If both amounts are 0, 
	# then all amounts are settled 
	if (amount[mxCredit] == 0 or amount[mxDebit] == 0): 
		return payment

	# Find the minimum of two amounts 
	min = minOf2(-amount[mxDebit], amount[mxCredit])
	payment.append([mxDebit, min, mxCredit])

	amount[mxCredit] -= min
	amount[mxDebit] += min	

	# Recur for the amount array. Note that 
	# it is guaranteed that the recursion 
	# would terminate as either amount[mxCredit] 
	# or amount[mxDebit] becomes 0 
	return minCashFlowRec(amount,payment) 


amount = {
	"userID1": 5000,
	"userID2": 3000,
	"userID3": -4000,
	"userID4": -4000
}
for i in amount: 
	print(amount[i])


payment = minCashFlowRec(amount, []) 
print(payment)

TextArray = ""
for i in payment:
	TextArray = ' '.join( [TextArray, "Person", str(i[0]), "pays ", str(i[1]),"to" ,"Person" ,str(i[2]), '\n' ] )

print (TextArray)