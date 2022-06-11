import time, linked_list, binary_search_tree

# LINKED LIST TEST STARTS HERE...

def linked_list_test(arr):
    print('Linked list - ' + str(len(arr)) + ' elements')

# Building
    starttime_building = time.time()
    linked_list_inst = linked_list.LinkedList(linked_list.Item(arr[0]))

    for i in range(1,len(arr)):
        linked_list_inst.insert(arr[i])

    lasttime_building = time.time()
    totaltime_building = int((lasttime_building - starttime_building) * 1000)

    print('-> building: ' + str(totaltime_building) + 'ms')

# Searching    
    starttime_searching = time.time()

    for i in range(len(arr)):
        linked_list_inst.search(arr[i])

    lasttime_searching = time.time()
    totaltime_searching = int((lasttime_searching - starttime_searching) * 1000)

    print('-> searching: ' + str(totaltime_searching) + 'ms')

# Deleting
    starttime_deleting = time.time()

    linked_list_inst.delete_all()

    lasttime_deleting = time.time()
    totaltime_deleting = int((lasttime_deleting - starttime_deleting) * 1000)

    print('-> deleting: ' + str(totaltime_deleting) + 'ms')


# BINARY SEARCH TREE TEST STARTS HERE...

def binary_search_tree_test(arr):
    print('Binary Search Tree - ' + str(len(arr)) + ' elements')

# Building
    starttime_building = time.time()
    bst_root = binary_search_tree.Node(arr[0])

    for i in range(1,len(arr)):
        binary_search_tree.insert(bst_root, arr[i])

    lasttime_building = time.time()
    totaltime_building = int((lasttime_building - starttime_building) * 1000)

    print('-> building: ' + str(totaltime_building) + 'ms')

# Searching    
    starttime_searching = time.time()

    for i in range(len(arr)):
        binary_search_tree.search(bst_root, arr[i])

    lasttime_searching = time.time()
    totaltime_searching = int((lasttime_searching - starttime_searching) * 1000)

    print('-> searching: ' + str(totaltime_searching) + 'ms')

# Deleting
    starttime_deleting = time.time()

    binary_search_tree.delete(bst_root)

    lasttime_deleting = time.time()
    totaltime_deleting = int((lasttime_deleting - starttime_deleting) * 1000)

    print('-> deleting: ' + str(totaltime_deleting) + 'ms')


# BST to AVL 

def bst_to_avl_test(arr):
    print('Binary Search Tree - ' + str(len(arr)) + ' elements')

    bst_root = binary_search_tree.Node(arr[0])

    for i in range(1,len(arr)):
        binary_search_tree.insert(bst_root, arr[i])

    print('-> height: ' + str(binary_search_tree.height(bst_root)))

    print('AVL Tree - ' + str(len(arr)) + ' elements')

    nodes=[]
    binary_search_tree.storeNodes(bst_root,nodes)
 
    n=len(nodes)
    binary_search_tree.buildTreeUtil(nodes,0,n-1)

    print('-> height: ' + str(binary_search_tree.height(binary_search_tree.buildTreeUtil(nodes,0,n-1))))

