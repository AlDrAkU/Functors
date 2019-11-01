class Functor(object):

    
    def __init__(self, n=10):
        self.n = n
    def __call__(self, x):
        x_first = x[0]
        if type(x_first) is int:
            return self. __MergeSort(x)
        if type(x_first) is float:
            return self. __HeapSort(x)
        else:
            return self. __QuickSort(x)
    def __MergeSort(self,a):
        print("Data is Merge sorted:")
        def mSort(lst):
            if len(lst) >1: 
                mid = len(lst)//2 
                L = lst[:mid] 
                R = lst[mid:] 

                mSort(L) 
                mSort(R) 
                i = j = k = 0
                while i < len(L) and j < len(R): 
                    if L[i] < R[j]: 
                        lst[k] = L[i] 
                        i+=1
                    else: 
                        lst[k] = R[j] 
                        j+=1
                    k+=1

                while i < len(L): 
                    lst[k] = L[i] 
                    i+=1
                    k+=1

                while j < len(R): 
                    lst[k] = R[j] 
                    j+=1
                    k+=1
            return lst
        return mSort(a)
        
    def __HeapSort(self,b):
        print("Data is Heap sorted:")
        def heapify(lst,n,i):
            max = i  
            l = 2 * i + 1     
            r = 2 * i + 2     
            if l < n and lst[i] < lst[l]: 
                max = l 
            if r < n and lst[max] < lst[r]: 
                max = r 
            if max != i: 
                lst[i],lst[max] = lst[max],lst[i]
                heapify(lst, n, max) 
        
        def hSort(lst): 
            n = len(lst) 

            for i in range(n, -1, -1): 
                heapify(lst, n, i) 
            for i in range(n-1, 0, -1): 
                lst[i], lst[0] = lst[0], lst[i] 
                heapify(lst, i, 0) 
            return lst

        return hSort(b)
        
        
    def __QuickSort(self,c):
        print("Data is Quick sorted:")
        def part(lst,lo,hi): 
            i = ( lo-1 )         
            pivot = lst[hi]     
            for j in range(lo , hi): 
                if   lst[j] <= pivot: 
                    i = i+1 
                    lst[i],lst[j] = lst[j],lst[i] 
            lst[i+1],lst[hi] = lst[hi],lst[i+1] 
            return ( i+1 ) 

        def quickSort(lst,lo,hi): 
            if lo < hi: 
                pi = part(lst,lo,hi) 
                quickSort(lst, lo, pi-1) 
                quickSort(lst, pi+1, hi)
            return lst
        return quickSort(c,0,len(c)-1)
#         return c
    
    
class Caller(object):
    def __init__(self):
        self.sort=Functor()
        
    def SortingOut(self,x):
        return self.sort(x)

xs = [8, 4, 2, 2, 1, 7, 10, 5,55,18,3,6]
xf = [0.1, 10.5,55.2,7.4,3.8,22.1,144, 21.1,14.2]
xz = ['a','z','g','h','b','b','d','z','i']

Call = Caller()
print(Call.SortingOut(xs))
print(Call.SortingOut(xf))
print(Call.SortingOut(xz))