# Union-find

- Union-find is a logic and a data type to effectively determine whether two points are connected.
- The basic idea is that we put all the connected nodes in the same group. When we want to check if some nodes are connected, we can quickly check whether they belong to the same group.

![Union-find](https://miro.medium.com/v2/resize:fit:528/1*m3b5nj9h3XVYs8z_3Ow5xg.jpeg)

- **union(3,4)**
  ![Union Example](https://miro.medium.com/v2/resize:fit:559/1*JNgu4VfNm2zV6aYCiGbqGw.jpeg)

- **connected(1,2)** will return True

- `def find(self, p)`: This will return the component identifier for p (0 to N — 1).

# How do we apply this algorithm?

## 1. Quick-Find
![Quick-Find](https://miro.medium.com/v2/resize:fit:700/1*IYOCMWete5INfvjQrRVGYA.png)

- Quick-Find uses an array to implement this algorithm.
- The array `id[]` is indexed by the site number, and the array value is the site number of the component identifier.
- **Connected:** Check if the `id` of nodes are the same. Returns True if they're the same, else returns False.
- **Union:** To merge two nodes, `p` and `q` (or components), we need to change all entries whose `id[p]` equals `id[q]`.

**union(2,3)**
  ![Union Example](https://miro.medium.com/v2/resize:fit:700/1*HvIXmPLYiyBpAVAB5iJNrw.png)

### Problem of Quick-Find: Union is too expensive
- Initialize: N (Create an array of length N)
- Union: N (We need to go through every component to check their `id`) ***too expensive***
- Find: 1
- Quadratic complexity: Every “union” requires visiting all array components, leading to N*N operations.

## 2. Quick-Union
![Quick-Union](https://miro.medium.com/v2/resize:fit:700/1*qZNyUeWAal_XIVppfUcupA.png)

- **Connected:** Check if the roots of two nodes are the same.
- **Union:** To merge two components `p` and `q`, set the root of `p`’s root to the root of `q`’s root.

    ```python
    class QuickUnionUF():

    def __init__(self,N):
        if(type(N)!=int):
            print("Size must be integer")
        else:
            self.id_array=list(range(0,N))
            self.size=N

    def root(self,i):
        if(type(i)!=int):
            print("Input must be integer")
        else: 
            while(i!=self.id_array[i]):  # iteratively track up to find root
                i=self.id_array[i]
            return i

    def connected(self,p,q):
        if(type(p)!=int or type(q)!=int):
            print("Input must be integer")
        else:
            return self.root(p)==self.root(q)     # check whether two nodes have the same root

    def union(self,p,q):
        if(type(p)!=int or type(q)!=int):
            print("Input must be integer")
        else:
            i = self.root(p)
            j = self.root(q)
            self.id_array[i]=j # union roots

    def count(self):   #show size
        return(self.size)
    
    def printarray(self): #show array
        print(self.id_array)
    ```
## Problem of Quick-Union: Tree-like structure might get too tall

- Initialize: N (We need to create a N length array)

- Union: N> (In the worst case, if the tree is too tall)

- Find: N (In the worst case, if the tree is too tall)

- If the tree structure gets too tall, we have to go through every node when we try to find the root.

# Compare with Quick-Find
- <img alt="" class="bg oc od c" width="700" height="135" loading="lazy" role="presentation" src="https://miro.medium.com/v2/resize:fit:700/1*v8vH1ZdcXF_DgRhtR23ulg.png">