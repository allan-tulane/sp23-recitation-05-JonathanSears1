# CMPS 2200 Recitation 5

In this recitation, we'll look at randomness in computation.

**To make grading easier, please place all written solutions directly in `answers.md`, rather than scanning in handwritten work or editing this file.**

All coding portions should go in `main.py` as usual.


## Determinism versus Randomization in Quicksort

In lecture we saw that adding a random choice of pivot reduced the
probability of worst-case behavior for any given input in
selection. Let's look at how pivot choices affect Quicksort. For this
question, refer to the code in `main.py` 

**1a)**

Complete the implementations of `qsort` and `compare_sort` stubs. Feel
free to take from code given in the lectures to  help you perform list
partitioning. Note that the pivot choice function is input to `qsort`,
so you will have to curry `qsort` to test different methods of
choosing pivots. Implement variants of `qsort` that correspond to
selecting the first element of the input list as the pivot, and to
selecting a random pivot.
|        |        n |   qsort-fixed-pivot |   qsort-random-pivot |
|--------|----------|---------------------|----------------------|
|    100 |    0.242 |               0.332 |                0.011 |
|    200 |    0.923 |               0.785 |                0.021 |
|    500 |    1.364 |               2.076 |                0.057 |
|   1000 |    3.402 |               4.176 |                0.118 |
|   2000 |    6.800 |              52.606 |                0.350 |
|   5000 |   21.520 |              75.900 |                3.025 |
|  10000 |  115.827 |             140.886 |                1.876 |
|  20000 |  185.997 |             239.603 |                3.034 |
|  50000 |  504.764 |             604.565 |               11.308 |
| 100000 | 1155.451 |            1390.875 |               70.747 |


**1b)**

Compare running times using `compare-qsort` between variants of
Quicksort and the
provided implementation of selection sort (`ssort`). Perform two
different comparisons: a comparison between sorting methods using
random permutations of the specified sizes, and a comparison using
already sorted permutations. How do the running times compare to the
asymptotic bounds? How does changing the type of input list change the
relative performance of these algorithms? Note that you may have to
modify the list sizes based on your system memory; compare at least 10
different list sizes. The `print_results` function in `main.py` gives
a table of results, but feel free to use code from Lab 1 to plot
the results as well. 

|     n |   qsort-random-pivot |   Selection Sort |
|-------|----------------------|------------------|
|   100 |                0.378 |            0.401 |
|   200 |               13.256 |            3.932 |
|   500 |                7.465 |           35.156 |
|  1000 |                9.527 |           40.461 |
|  2000 |               45.377 |          240.571 |
|  3000 |               68.709 |          611.431 |
|  5000 |               68.152 |         1604.055 |
| 10000 |              112.107 |         7067.119 |
| 15000 |              188.170 |        16126.666 |
| 20000 |              254.990 |        29912.787 |

The running times check out with the asymptotic bounds, with qsort hitting around where it is expected too (not worst wase). I am surprised at how slow selection sort is though, even though it is O(n^2) these times still seem a little slow. 
**1c)**

Python uses a sorting algorithm called [*Timsort*](https://en.wikipedia.org/wiki/Timsort), designed by Tim Peters. Compare the fastest of your sorting implementations to the Python
sorting function `sorted`, conducting the tests in 3b above. 

|      n |   qsort-random-pivot |   Tim-Sort |
|--------|----------------------|------------|
|    100 |                0.419 |      0.011 |
|    200 |                0.818 |      0.022 |
|    500 |                2.214 |      0.057 |
|   1000 |                5.103 |      0.122 |
|   2000 |               10.760 |      0.299 |
|   5000 |               95.617 |      0.938 |
|  10000 |              100.458 |      1.839 |
|  20000 |              216.062 |      3.938 |
|  50000 |              691.183 |     58.285 |
| 100000 |             1663.159 |     94.479 |
