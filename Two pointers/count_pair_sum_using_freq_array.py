A = [2,3,3,10,10,10]
k = 13
freq_arr = [0] * (max(A)+1)
for i in A:
  freq_arr[i] += 1

n = len(freq_arr)
i = 0
j = n-1
cnt = 0
while i < j:
  if i + j == k:
    cnt += (freq_arr[i] * freq_arr[j])
    i += 1
    j -= 1
  elif i+j < k:
    i += 1
  else:
    j -= 1

print(cnt)