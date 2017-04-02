#-------------------------------------------------------------------------------
# Name:        Insertion sort
# Purpose:
#
# Author:      Devanshi
#
# Created:     02-04-2017
# Copyright:   (c) Devanshi 2017
# Licence:
#-------------------------------------------------------------------------------

def insertion_sort(elements):
    size=len(elements)
    for i in range(size-1):
        ele=elements[i+1]

        #implement insertion sort

        for j in range(i+1):
            if ele<elements[j]:
                elements.remove(ele)
                elements.insert(j,ele)
                break
    return elements

#take elements from user

elements=list(int(i) for i in input("Enter the elements to be sorted").split(" "))

#sort elements

result=insertion_sort(elements)

# print the result

print(" Sorted Array: ",result)