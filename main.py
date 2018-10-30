import SpectralIndex
import random
import math
import copy

def expandIndex(index,index2,isLeft):

    if index.left == None and index.right == None:

        if isLeft:
            index.parent.left = index2
            index2.parent = index
        else:
            index.parent.right = index2
            index2.parent = index

        # return index

    else:

        if random.random() < 0.5:
            expandIndex(index.left,index2,True)
        else:
            expandIndex(index.right,index2,False)

def evaluate(root,values):

    # empty SpectralIndexNode
    if root is None:
        return 0

    # leaf node
    if root.left is None and root.right is None:

        # multiply value with coefficient

        temp = float(values[root.value]) * root.coefficient
        # evaluate unary operation

        if root.unary_op == "sqrt":
            return math.sqrt(abs(temp))
        elif root.unary_op == "log":
            if temp == 0:
                return 0
            else:
                return math.log(temp,10)
        elif root.unary_op == "-":
            return temp*-1

        return temp


    left_sum = evaluate(root.left,values)
    right_sum = evaluate(root.right,values)

    if root.value == '+':
        return left_sum + right_sum

    elif root.value == '-':
        return left_sum - right_sum

    elif root.value == '*':
        return left_sum * right_sum

    else:
        if right_sum == 0:
            return 0
        else:
            return left_sum / right_sum

def basicCrossover(tree1, tree2):

    tree3 = copy.deepcopy(tree1)
    tree4 = copy.deepcopy(tree2)

    temp = tree3.index.left

    tree3.index.left = tree4.index.left
    tree3.index.left.parent = tree3.index    


    tree4.index.left = temp
    tree4.index.left.parent = tree4.index




    return tree3,tree4

bands = ["B1","B2","B3","B4","B5","B6","B7"]

values = {}
values['B1'] = 1.0
values['B2'] = 2.0
values['B3'] = 3.0
values['B4'] = 4.0
values['B5'] = 5.0
values['B6'] = 6.0
values['B7'] = 7.0

index = SpectralIndex.SpectralIndex(bands)
# index.pretty(index.index,0)
indexAppend = SpectralIndex.SpectralIndex(bands)
# indexAppend.pretty(indexAppend.index,0)

expandIndex(index.index,indexAppend.index,True)

indexAppendAgain = SpectralIndex.SpectralIndex(bands)

expandIndex(index.index,indexAppendAgain.index,True)


index.pretty(index.index,0)



print("---------------------------------")
index2 = SpectralIndex.SpectralIndex(bands)
# index2.pretty(index2.index,0)
index2Append = SpectralIndex.SpectralIndex(bands)
# index2Append.pretty(index2Append.index,0)

expandIndex(index2.index,index2Append.index,True)
index2.pretty(index2.index,0)



print("---------------------------------")
print("")
print("Crossover!")


index3,index4 = basicCrossover(index,index2)

index3.pretty(index3.index,0)
# print("---------------------------------")

index4.pretty(index4.index,0)



