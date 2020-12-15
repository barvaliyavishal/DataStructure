class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = -1;
        arr = [];
        for i in arr2:
            j = index + 1;
            while j < len(arr1):
                if arr1[j] == i:
                    index += 1;
                    temp = arr1[index];
                    arr1[index] = arr1[j];
                    arr1[j] = temp;
                j += 1;
        arr = arr1[index + 1:]
        arr.sort();
        for i in arr:
            index += 1;
            arr1[index] = i;

        return arr1;