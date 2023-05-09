# DataAlgoHub
personal reference repository for common algorithms and data structures implementation


- [Big-O Notation](#big-o)
- [Arrays](#arrays)
    - [Static Array](#static-array)
    - [Dynamic Array](#dynamic-array)
    - [Summary](#summary_0)
- [Linked List](#linked-list)
    - [Singly Linked List](#singly-linked-list)
    - [Doubly Linked List](#doubly-linked-list)
    - [Circular Linked List](#circular-linked-list)
    - [Summary](#summary_1)

<br/>
<br/>
<br/>

# Big-O

**what is ***Big-O Notation*** and what is ***Omega*** and ***Theta*** ?**

- **Big-O Notation**(worst case) is a mathematical Notation used to describe the limiting behavior of a function when the argument tends towards a particular value or infinity.<br/>
 It is commonly used in computer science to describe the time complexity of algorithms. 
  - **Big-O Notation Mathematical exepression**

    O(g(n)) = { f(n): there exist positive constants c and n0
            such that 0 ≤ f(n) ≤ cg(n) for all n ≥ n0 }

  - ***Big-O Notation Graph***
  <br/>
   <img src="https://cdn.programiz.com/sites/tutorial2program/files/big0.png" style = "width:70%" alt = "Figure for Big-Oh Notation">
    <br/><br/>
- **Omega Notation** (best case) , on the other hand, provides a lower bound on the running time of an algorithm. It is used to describe the best-case running time of an algorithm.

  - **Omega Notation Mathematical exepression**

    Ω(g(n)) = { f(n): there exist positive constants c and n0 
            such that 0 ≤ cg(n) ≤ f(n) for all n ≥ n0 }
    <br/><br/>
- **Theta Notation**(both O(g(n)) and Ω(g(n))) is used to describe the tight bound on the running time of an algorithm. It provides both an upper and a lower bound on the running time of an algorithm. In other words, if a function is Θ(g(n)), then it is both O(g(n)) and Ω(g(n)).
 
  - **Theta Notation Mathematical exepression**

    Θ(g(n)) = { f(n): there exist positive constants c1, c2 and n0
            such that 0 ≤ c1g(n) ≤ f(n) ≤ c2g(n) for all n ≥ n0 }

<br/><br/><br/>
- **Big-O Notation** measures the upper bound or worst-case scenario for the growth rate of a function. In the context of computer science and algorithm analysis, it is used to describe the maximum amount of time an algorithm takes to solve a problem as the input size grows.

- **Big-O Complexity Chart**

  <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg" style = "width:80%" alt = "Figure for Big-Oh Notation">

<br />




# Arrays

### Static Array 

- **Static Array**: Contiguous area of memory consisting of equal-size elements indexed by contiguous integers.

  - **Read / Write Time Complexity** 
    - **Access**: O(1)
    - **Add/Remove (start / middle)**: O(n)  
    - **Add/Remove (end)**: O(1)

### Dynamic Array

- **Dynamic Array**: A dynamic array is an array with a big improvement: automatic resizing.

- **Problem**: Static arrays are fixed in size, meaning they're not able to expand or contract once they're created. This is a problem for two reasons:
    - 1. We might insert items and then run out of capacity.
    - 2. We might delete items and end up with lots of empty space at the end of the array.

- **Solution**: dynamic arrays (also known as resizable arrays) 
 - **Idea**: store pointer to a dynamically allocated array and replace it with a newly-allocated array as needed.
 - [Dynamic Array Implementation](./Data_structures/array.py)

### Summary_0

- Unlike static arrays, dynamic arrays can be resized.
- Appending an item to a dynamic array is O(1) on average, but O(n) worst-case, because of the possibility of having to allocate a new array and copy over the old elements.
- Some space is wasted the capacity is always at least the length of the array, but usually, it's somewhere between length and length * 2.



# Linked List
  - is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
  - data structure for storing objects in a linear fashion. It is a collection of nodes where each node holds a node value and a link to the next node in the list.
  <br/><br/>
  - **Advantages**:
    - Dynamic size
    - Ease of insertion/deletion
  - **Disadvantages**:
    - Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation.
    - Extra memory space for a pointer is required with each element of the list.
    - Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.
  - **Use Cases**:
    - Linked lists are used to implement stacks, queues, graphs, etc.
    - dynamic memory allocation
<table>
  <thead>
    <tr>
      <th></th>
      <th>Array</th>
      <th>Linked List</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Order determined by</th>
      <td>indices</td>
      <td>pointers</td>
    </tr>
    <tr>
      <th>Search</th>
      <td>O(1)</td>
      <td>O(n)</td>
    </tr>
  </tbody>
</table>

    
  - The order of the elements in an array is determined by their indices. For example, if we have an array of integers {1, 2, 3, 4}, then the first element is at index 0, the second element is at index 1, and so on.

  - The order of the elements in a linked list is determined by the pointers that connect the nodes together. For example, if we have a linked list with three nodes containing the data values 1, 2, and 3, then the order of the elements is determined by the pointers connecting the nodes: node 1 points to node 2, which points to node 3.


## Types of Linked List

### Singly Linked List

- *Singly Linked Lists*: is a data structure that contains a sequence of nodes such that each node contains an object and a reference to the next node in the list.

  - *Singly Linked Lists*

    <img src="https://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist_insert_at_start.png" style = "width:80%" alt = "Figure for Singly Linked Lists">

- #### Singly Linked List Implementation

  - GOTO [Singly Linked Lists Implementation](./Data_structures/singly_linked_list.py)

### Doubly Linked List

- *Doubly Linked Lists*: is a data structure that contains a sequence of nodes such that each node contains an object and references to the previous and next nodes in the list.

  - *Doubly Linked List*

    <img src="https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/03/DLL1.png" style = "width:80%" alt = "Figure for Doubly Linked Lists">

### Circular Linked List
- *Circular Linked Lists*: is a variation of a linked list in which the last element is linked to the first element. This forms a circular loop.

  - *Circular Linked List*

    <img src="https://media.geeksforgeeks.org/wp-content/uploads/CircularLinkeList.png" style = "width:80%" alt = "Figure for Circular Linked Lists">

### Summary_1
  - Unlike arrays, linked list elements are not stored at contiguous locations; the elements are linked using pointers.
  - Accessing an element in a linked list is a linear operation because we have to sequentially traverse the list until we find the desired element.
  - Linked lists have dynamic size, unlike arrays which have fixed size. So, it is not required to pre-allocate memory for a linked list.
  - The drawbacks of using linked list are that they require extra memory for pointers and they are not cache friendly (elements are not stored in contiguous locations).
  