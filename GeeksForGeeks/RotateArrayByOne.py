'''Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far'''

def contiguousMaxSubArray(arr):
    maxs=0;
    maxe=0;

    for i in arr:
        maxe+=i;
        if maxs<maxe:
            maxs=maxe;
        if maxe<0:
            maxe=0;
    return maxs;

print(contiguousMaxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))