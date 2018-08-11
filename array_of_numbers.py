# Given an array of numbers, find the top K
# largest numbers in the array. [5,1,2,9,1], K = 3,
# return [5,9,2]

'''
Solution: This is assuming integers are positive 
1. Create array to hold results or modify array to only keep Kth biggest integers 
2. Loop throup array and check if size of results array is kth - 1 size & 
make sure done looping through sample array
3. Edge cases: 
	a. empty array
	b. sample array size == k 
'''

def solutionOne(sample_array, k):
	result = []	
	if len(sample_array) == 0 or len(sample_array) - 1 <= k: 
		return sample_array
	else: 
		sample_array.sort(); 	
		last_index = len(sample_array) - 1 	
		length_of_array = len(sample_array)
		ending_index = k + 1
		cursor_direction = -1
		for i in range(last_index, length_of_array - ending_index, cursor_direction):
			result.append(sample_array[i]);
		return result

# def solutionTwo(sample_array, k):
# 	result = []
# 	if len(sample_array) == 0 and len(sample_array) == (k - 1): 
# 		return sample_array
# 	else:



array = [5,1,2] 
K = 3
print(solutionOne(array, K)); 
# print(solutionTwo(array, K)); 


