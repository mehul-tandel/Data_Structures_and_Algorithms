'''
Problem Statement: Lumberjack Mirko needs to chop down M metres of wood. It is an easy job for him since he has a nifty new woodcutting machine that can take down forests like wildfire. However, Mirko is only allowed to cut a single row of trees.

Mirko‟s machine works as follows: Mirko sets a height parameter H (in metres), and the machine raises a giant sawblade to that height and cuts off all tree parts higher than H (of course, trees not higher than H meters remain intact). Mirko then takes the parts that were cut off. For example, if the tree row contains trees with heights of 20, 15, 10, and 17 metres, and Mirko raises his sawblade to 15 metres, the remaining tree heights after cutting will be 15, 15, 10, and 15 metres, respectively, while Mirko will take 5 metres off the first tree and 2 metres off the fourth tree (7 metres of wood in total).

Mirko is ecologically minded, so he doesn‟t want to cut off more wood than necessary. That‟s why he wants to set his sawblade as high as possible. Help Mirko find the maximum integer height of the sawblade that still allows him to cut off at least M metres of wood.
'''

def cutsMinRequireWood(tree_heights,min_wood_required,saw_height):

    total_wood_cut = 0

    for i in range(len(tree_heights)):
        
        # if current_tree's height is greater than saw's height, extra height of tree is cut and added to pile of total_wood_cut.
        if tree_heights[i] > saw_height :
            total_wood_cut += (tree_heights[i]-saw_height)

            # check if pile of total_wood_cut has accumulated minimum_wood_required.
            if total_wood_cut >= min_wood_required :
                return True
            
    return False


def search_optimal_saw_height(n,m,tree_heights): # n = no. of trees, m = minimum wood required.

    tree_heights.sort()
    start = 0
    end = 10**6  #max height of a tree possible(given in constraints)
    saw_height = 0 #initialize the saw height to worst case(0) where all trees needs to be cut fully

    while start <= end :
        mid = start + (end-start)//2

        if cutsMinRequireWood(tree_heights,m,mid):
            saw_height = mid
            start = mid + 1
        else:
            end = mid - 1

    return saw_height


# input
n,m = input().split()
n = int(n)
m = int(m)
arr = input().split()
arr = list(map(int,arr))

# test code
print(search_optimal_saw_height(n,m,arr))