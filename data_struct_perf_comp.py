import list_generator, sys, tests

sys.setrecursionlimit(10**6)

def main():
    #zad1()
    zad2()

def zad1():
    for i in range(1,16):
        arr = list_generator.generate_random_list(5000*i)

        tests.linked_list_test(arr)
        tests.binary_search_tree_test(arr)

def zad2():
    for i in range(1,16):
        arr = list_generator.generate_random_list(10000*i)

        tests.bst_to_avl_test(arr)

if __name__=="__main__":
    main()