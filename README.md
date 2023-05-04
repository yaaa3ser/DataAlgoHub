# DataAlgoHub
personal reference repository for common algorithms and data structures implementation


- [Big-O Notation](#big-o)
- [Arrays](#arrays)
    - [Static Array](#static-array)
    - [Dynamic Array](#dynamic-array)
    - [Summary](#summary)

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


<div style="text-align:center"
>ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ</div>

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

### Summary

- Unlike static arrays, dynamic arrays can be resized.
- Appending an item to a dynamic array is O(1) on average, but O(n) worst-case, because of the possibility of having to allocate a new array and copy over the old elements.
- Some space is wasted the capacity is always at least the length of the array, but usually, it's somewhere between length and length * 2.
<div style="text-align:center"
>ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ</div>
