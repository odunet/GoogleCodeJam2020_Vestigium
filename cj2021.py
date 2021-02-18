import copy

#Swap function
def swap(array, index1, index2) :
	saveElement = array[index1]
	array[index1] = array[index2]
	array[index2] = saveElement
	return array

#Bubble sort
def bubbleSort(array) :
	n = len(array)
	for i in range(n) :
		count = 0
		for j in range(n-1) :
			if array[j + 1] < array[j] :
				count += 1
				swap(array, j, j + 1)
		if count == 0 :
			break
	return array
	

#Read number of iter
iter = int( input() )

for i in range(iter) :
	n = int( input() )
	matrix = []
	rowFail = 0
	for j in range(n) :
		matrixRow = [ int(unit) for unit in input().split(" ") ]
		matrix.append(matrixRow)
		tempMatrixRow = copy.deepcopy(matrixRow)
		sortMatrixRow = bubbleSort(tempMatrixRow)
		sequence = 1
		for k in sortMatrixRow :
			if sequence != k :
				rowFail += 1
				break
			sequence += 1
	columnMatrix = []
	colFail = 0
	trace = 0
	for j in range( len(matrix) ) :
		matrixCol = []
		for k in range( len(matrix[0]) ) :
			if (j == k) :
				trace += matrix[j][k]
			matrixCol.append(matrix[k][j])
		tempMatrixCol = copy.deepcopy(matrixCol)
		sortMatrixCol = bubbleSort(tempMatrixCol)
		sequence2 = 1
		for l in sortMatrixCol :
			if sequence2 != l :
				colFail += 1
				break
			sequence2 += 1
		columnMatrix.append(matrixCol)
	case = i + 1
	print("case #{}: {} {} {}".format(case, trace, rowFail, colFail) )
