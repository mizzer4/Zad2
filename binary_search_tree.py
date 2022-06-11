class Node:
    # Constructor definition
    def __init__(self, value):
        # Initialize pointers to child nodes with no target
        self.left = None
        self.right = None
        # Set node value to value given as parameter
        self.value = value

# Insert method to create nodes
def insert(node, value):
    # Check if current node has value
    if node.value is not None:
        # If value to be inserted is smaller than current node value
        # then go left and if bigger then go right. When empty pointer 
        # encountered create new node with new value
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                insert(node.right, value)
        else:
            node.value = value

# Search through the BST for given value
def search(node, value):
    # If element not found in BST
    if node is None:
        return 
    # If element is found
    if node.value == value:
        return
    # Element to be searched is less than the current node
    elif node.value > value:
        search(node.left, value)
        return
    # Element to be searched is greater than the current node
    else:
        search(node.right, value)
        return

def delete(node):
    # If left child node exists
    if node.left is not None:   
        delete(node.left)
    # If right child node exists 
    if node.right is not None:
        delete(node.right)
    del(node)

# This function returns the binary tree height
def height(node):
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))

# This function traverses the binary tree and
# stores nodes in a list
def storeNodes(root,nodes):
     
    # Base case
    if not root:
        return
     
    # Store nodes traversing Inorder 
    storeNodes(root.left,nodes)
    nodes.append(root)
    storeNodes(root.right,nodes)

# Recursive function to construct binary tree
def buildTreeUtil(nodes,start,end):
     
    # base case
    if start>end:
        return None
 
    # Get the middle element and make it root
    mid=(start+end)//2
    node=nodes[mid]
 
    # Using index in Inorder traversal, construct
    # left and right subtrees
    node.left=buildTreeUtil(nodes,start,mid-1)
    node.right=buildTreeUtil(nodes,mid+1,end)
    return node
 