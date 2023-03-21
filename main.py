import random, time
import tabulate

def ssort(L):     
	for i in range(len(L)):         
		#print(L)         
		m = L.index(min(L[i:]))         
		L[i], L[m] = L[m], L[i]     
	return L

def qsort(a, pivot_fn):
    ## TO DO
	left= []
	right = []
	pivot = []
	if len(a) <= 1:
		return a
	else:
		pivot.append(a[pivot_fn(a)])
		#print("pivot: {}".format(pivot))
		for num in a:
			if num < pivot[0]:
				left.append(num)
			elif num > pivot[0]:
				right.append(num)
		#print("left: {}".format(left))
		#print("right: {}".format(right))
		return qsort(left,pivot_fn)+pivot+qsort(right,pivot_fn)

def random_index(mylist):
	return (random.randint(0,len(mylist)-1))
# b = list(range(100))
# random.shuffle(b)
# print(qsort(b,random_index))
# print(ssort(b))

def fixed_pivot(mylist):
		return 0

def qsort_random_pivot(mylist):
	return qsort(mylist,random_index)

def qsort_fixed_pivot(mylist):
	return qsort(mylist,fixed_pivot)
	
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 3000, 5000, 10000, 15000, 20000]):
    """
    Compare the running time of different sorting algorithms.
    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        #shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(ssort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-random-pivot', 'Selection Sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()