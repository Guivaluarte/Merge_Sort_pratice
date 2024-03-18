#This program will take an random array with n elements and sort this array using merge sort 

import random

array = random.sample(range(0,100),10)


def sort (arr):
  if len(arr) > 1:

     half = len(arr)//2

     left_arr = arr[:half]
     right_arr = arr[half:]

     sort(left_arr)
     sort(right_arr)

     i = j = k = 0

     while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
             arr[k] = left_arr[i]
        
             i += 1
        else:
           arr[k] = right_arr[j]
           j += 1
        k += 1

     while i < len(left_arr):
         arr[k] = left_arr[i]
         i += 1
         k += 1

     while j < len(right_arr):
         arr[k] = right_arr[j]
         j += 1
         k += 1
  


print('given array')

print(array)
sort(array)

print('sorted array')

print(array)

   

    
    

    

  




  

   





