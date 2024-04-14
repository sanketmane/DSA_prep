# Count sorting technique
# uses frequency array for storing frequency of array values(can use hashmap as well)

A = [-2,3,8,3,-2,3]

# count sort for positive nums
freq_arr = [0] * (max(A)+1)
for i in A:
  freq_arr[i] += 1

k = 0
for i in range(len(freq_arr)): # loop over the freq_arr indices
  for j in range(freq_arr[i]): # loop over the index frequency
    A[k] = i # update original array based on index frequency
    k += 1 # this will move the index in the original array.


# count sort for negative nums
# range of freq arr will be from smallest num to largest
# largest num = largest num in A + abs(smallest num) + 1
# adjust indices of freq_arr to include -ve nums.
min_num = min(A)
max_num = max(A) + abs(min_num)
freq_arr = [0] * (max_num+1)

# adjust for -ve nums
for i in A:
  freq_arr[i-min_num] += 1

k = 0
for i in range(len(freq_arr)):
  for j in range(freq_arr[i]):
    A[k] = i+min_num # add min_num 
    k += 1

print(A)
