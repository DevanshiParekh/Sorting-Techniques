#-------------------------------------------------------------------------------
# Name:        Selection sort
# Purpose:
#
# Author:      Devanshi
#
# Created:     02-04-2017
# Copyright:   (c) Devanshi 2017
# Licence:
#-------------------------------------------------------------------------------

def selection_sort(elements):
    size=len(elements)
    for i in range(size):
        for j in range(i,size-1):
            #select the shortest element and then swap it with position of i
            if elements[j]>elements[j+1]:
                elements[j+1],elements[i]=elements[i],elements[j+1]
                break
    return elements
elements = list(int(i) for i in input("Enter the elements to be sorted").split(" "))
result=selection_sort(elements)
print(" Sorted Array: ",result)