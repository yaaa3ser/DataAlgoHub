- ```left(..., 1)``` &&```right(..., 1)``` get the first and last char of a string
- ```... in ('a','e','i','o','u')``` check if a char is a vowel
- ```LIMIT 1``` only return the first row
    - ```sql
        (select city from station order by length(city) asc, city asc LIMIT 1)
        union
        (select city from station order by length(city) desc, city desc LIMIT 1)
        ``` 
        [★] **returns the two cities in STATION with the shortest and longest CITY names**
- ```LIMIT n, m``` return the mth row after the nth row
    - ```sql
        SET n = n - 1;
        SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT n, 1
        ```
        [★] **return the nth highest salary from the Employee table**
- ```LIMIT N, OFFSET M``` **(same as above)** return N rows after skipping M rows
    - ```sql
        SET n = n - 1;
        SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET n
        ```
        [★] **return the nth highest salary from the Employee table**
- ```sql
    case
        when ... then ...
        when ... then ...
        else ...
    end as ...
    ```
    [★] **return something based on conditions**



