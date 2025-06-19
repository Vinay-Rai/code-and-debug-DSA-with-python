def maxDepth( root):
    if root == None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

#if root node ko exclude karna ho to return -1 kar dena root none hone par
