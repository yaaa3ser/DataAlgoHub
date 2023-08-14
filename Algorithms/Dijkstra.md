
**Dijkstra's shortest path algorithm operates <u>based on the following steps:</u>**

0. Initialize two lists: one to keep track of visited vertices and another to store unvisited vertices.
1. Start with the given starting vertex (let's say vertex A).
2. Set the distance from A to itself as 0, and assign a very high value (such as infinity) to the distances from A to all other vertices.
3. Add this information to the table.
4. Visit the unvisited vertex with the smallest known distance from the starting vertex. Initially, this is the starting vertex itself (A).
5. For the current vertex, examine its unvisited neighbors and Calculate the distance of each neighbor from the starting vertex.
6. If the calculated distance of a vertex is less than the known distance, update the shortest distance in the table.
7. Update the previous vertex column for each updated distance.
8. Add the current vertex to the list of visited vertices and remove it from the unvisited list.
* **Repeat steps 4-8 until all vertices are visited and the table is complete.**
----------------------
----------------------
***better to understand***
```
Let distance of start vertex from start vertex = 0
Let distance of all other vertices from start = ∞ (infinity)

WHILE vertices remain unvisited
    Visit unvisited vertex with smallest known distance from start vertex (call this 'current vertex')
    FOR each unvisited neighbour of the current vertex
        Calculate the distance from start vertex
        If the calculated distance of this vertex is less than the known distance
            Update shortest distance to this vertex
            Update the previous vertex with the current vertex
        end if
    NEXT unvisited neighbour
    Add the current vertex o the list of visited vertices
END WHILE
```

**useful link: https://www.youtube.com/watch?v=pVfj6mxhdMw**