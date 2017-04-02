#-------------------------------------------------------------------------------
# Name:        Bubble sort
# Purpose:
#
# Author:      Devanshi
#
# Created:     02-04-2017
# Copyright:   (c) Devanshi 2017
# Licence:
#-------------------------------------------------------------------------------

def Bubblesort(elements):
    for i in range(len(elements)):
        #loop below will bring the heaviest element to the last
        for j in range(len(elements)-i-1):
            #swap elements if element in lower index is greater than higher index
                if elements[j]>elements[j+1]:
                    elements[j],elements[j+1]=elements[j+1],elements[j]
    return elements

elements=list(int(i) for i in input("Enter the elements to be sorted").split(" "))
result=Bubblesort(elements)
print("Sorted array is " ,result)
