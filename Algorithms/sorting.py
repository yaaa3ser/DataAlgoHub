class Sort:
    def __init__(self, A):
        self.A = A
    
    def insertion_sort(self):
        for i in range(1, len(self.A)): # in range mean it became a list [.., .., ..] even if i changed inside the loop
            while i > 0 and self.A[i-1] > self.A[i]:
                self.A[i-1], self.A[i] = self.A[i], self.A[i-1]
                i -= 1
        return self.A
    
    def selection_sort(self):
        for i in range(len(self.A)):
            min_index = i
            for j in range(i+1, len(self.A)):
                if self.A[min_index] > self.A[j]:
                    min_index = j
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]
        return self.A
    
    def merge_sort(self):
        def merge(A, B):
            C = []
            while A and B:
                if A[0] < B[0]:
                    C.append(A.pop(0))
                else:
                    C.append(B.pop(0))
            C.extend(A)
            C.extend(B)
            return C
        
        if len(self.A) <= 1:  # Base case: return if array length is 1 or less
            return self.A
        
        mid = len(self.A) // 2
        left = self.A[:mid]
        right = self.A[mid:]

        sorted_left = Sort(left).merge_sort()
        sorted_right = Sort(right).merge_sort()
        
        return merge(sorted_left, sorted_right)
    
    def quick_sort(self):
        def partition(nums, low, high):
            pivot = nums[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1
                    
                j -= 1
                while nums[j] > pivot:
                    j -= 1

                if i >= j:
                    return j

                nums[i], nums[j] = nums[j], nums[i]
                
        def _quick_sort(low, high):
            if low < high:
                split_index = partition(self.A, low, high)
                _quick_sort(low, split_index)
                _quick_sort(split_index + 1, high)

        _quick_sort(0, len(self.A) - 1)
        return self.A



A = [5,4,3,2,1,0,9,8,7,6,5,4,3]
B = [10,20,20,30,10]

a = Sort(A)
b = Sort(B)
# print(a.insertion_sort())
# print(b.selection_sort())
# print(a.merge_sort())
# print(b.merge_sort())
print(a.quick_sort())
print(b.quick_sort())

