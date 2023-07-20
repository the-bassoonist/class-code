#Berkiel Molinard
#21 April 2021
#CS 10
#Prof. Locke
#Program to test functions a to j. 
# 
#Define constant variables. 
#ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #this is test run 1 
ONE_TEN =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103] #this is test run 2,  
#ONE_TEN = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]   #this is test run 3, 
#run test run 1 first, then 
#comment out test run 1 and 
#uncomment to run test run 2 
#and so forth for test run 3  
 
def main() : 
    print("The original data for all functions is: ", ONE_TEN) 
 
    #a. Demonstrate swapping the first and last element. 
    data = list(ONE_TEN) 
    swapFirstLast(data)         #call this function       
    print("After swapping first and last: ", data) 
 
    #b. Demonstrate shifting to the right. 
    data = list(ONE_TEN) 
    shiftRight(data)            #call this function 
    print("After shifting right: ", data) 
 
    #c. Demonstrate replacing even elements with zero. 
    data = list(ONE_TEN) 
    replaceEven(data)           #call this function 
    print("After replacing even elements: ", data) 
 
    #d. Demonstrate replacing values with the larger of their neighbors. 
    data = list(ONE_TEN) 
    replaceNeighbors(data)      #call this function 
    print("After replacing with neighbors: ", data) 
 
    #e. Demonstrate removing the middle element. 
    data = list(ONE_TEN) 
    removeMiddle(data)          #call this function 
    print("After removing the middle element(s): ", data) 
 
    #f. Demonstrate moving even elements to the front of the list. 
    data = list(ONE_TEN) 
    evenToFront(data)           #call this function 
    print("After moving even elements: ", data) 
 
    #g. Demonstrate finding the second largest value. 
    print("The second largest value is: ", secondLargest(ONE_TEN)) 
 
    #h. Demonstrate testing if the list is in increasing order. 
    print("The list is in increasing order: ", isIncreasing(ONE_TEN)) 
 
    #i. Demonstrate testing if the list contains adjacent duplicates. 
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN)) 
 
    #j. Demonstrate testing if the list contains duplicates. 
    print("The list has duplicates: ", hasDuplicate(ONE_TEN)) 
 
 
#here are 2 sample functions for item a and b 
 
def swapFirstLast(data:list):  ##????you decide what is being returned 
    temp=data[0]
    data[0]=data[len(data)-1]
    data[len(data)-1]=temp
   
    return data
 
# grabbing the last element and slapping it up front but not before redefining the list. 
def shiftRight(data:list):  ##????you decide what is being returned 
    '''Shift the elements of list to the right.'''
    lastelement = data[9]
    data[1:] = data[:len(data)-1]
    data[0] = lastelement


# define the following functions
#the following are replace function
#replaceEven, all evens go to zero. if i value does not have a remainder when devided to 0, then replace with 0
def replaceEven(data:list):
    for i in range(len(data)):
        if i %2 == 0:
            data[i] = 0
    

#replaceNeighbors, for values ijk, compare value j to i and k, if i or k > j then replace with either i or k,whatever is bigger
# i is really j-1 and k is really j+1, so really compare the values and do if else
def replaceNeighbors(data:list):
    for i in range(1, len(data)-1):
        if data[i-1] > data[i+1]:
            data[i] = data[i-1]
        else:
            data[i] = data[i+1]

#removeMiddle, for any given list remove the middle element
def removeMiddle(data:list):
    list_length = len(data)
    middle = int(list_length/2)
    if list_length %2 ==0:
        left = data[middle-1]
        right = data[middle]
        data.remove(left)
        data.remove(right)
    else:
        mid = data[middle]
        data.remover[mid]

#eventoFront, if i is of form 2n, then move to front
def evenToFront(data:list):
    dataindex = 0
    for i in range(0, len(data)):
        if data[i] %2 == 0 :
            data.remove(i)
            data.insert(dataindex, i)
            dataindex += 1
            

#these are identify functions
#secondLargest, sort from big to small, take the second largest value in case there is a tie, a condition is added to return second largest
def secondLargest(data:list):
    large_no = max(data)
    top = data[0]
    for i in range(0, len(data)):
        if i > top and i < large_no:
            top = i
    

#isIncreasing, use second largest sort, set it == to the actual list
def isIncreasing(data:list):
    list_new = data
    list_sort = data.sort()
    if list_new == list_sort :
        return True
    else: False
#hasAdjacentDuplicate, for i j k in list, compare  i and j and then compare j and k. return true if either is true
#again considerint i = j+1 and k = j-1
def hasAdjacentDuplicate (data:list):
    for i in range(1, len(data)):
        if data[i-1] == data[i]:
            return True
    return False

#hasDuplicate, compare two numbers in the list, if they are equal to eachother then true, if not false
def hasDuplicate(data:list):
    for i in range(len(data)-1):
        current = data[i]
        for j in range(i+1, len(data)):
            if current == data[j]:
                return True
    return False
 
##Complete the rest of the functions from items c to j 
 
if __name__ == "__main__": 
    main()

#The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
#After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#After replacing even elements:  [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
#After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
#After removing the middle element(s):  [1, 2, 3, 4, 7, 8, 9, 10]
#After moving even elements:  [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
#The second largest value is:  None
#The list is in increasing order:  None
#The list has adjacent duplicates:  False
#The list has duplicates:  False

#The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
#After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
#After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
#After replacing even elements:  [0, 20, 0, 14, 0, 16, 0, 38, 0, 103]
#After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
#After removing the middle element(s):  [12, 20, 10, 14, 75, 38, 79, 103]

    
