#Write a program to implement binary search algorithm using python2.7
#NOTE: important in interview screening
#Function is binary search
"""
INPUT: arr=[1,2,3,4,5,6,7]
Want to find number 3:
OUPUT: 2(number 3 is at index 2)
"""
def BinarySearch(arr,l,r,user):
    if r>=l:
        mid=(l+(r-1))/2 #Divide the list to find middle value
        if arr[mid]==user:
            return mid
        elif arr[mid]<user:
            l=mid+1
            return BinarySearch(arr,l,mid-1,user) #Recursive call to function
        else:
            r=mid-1
            return BinarySearch(arr,mid+1,r,user) #Recursive call to function
    else:
        return -1
#Main program
arr=[1,2,3,4,5,6,7]
user=raw_input("enter number you want to search:")
result=BinarySearch(arr,0,len(arr)-1,user) #Function call

if result!=-1:
    print "element at index",result
else:
    print "element is not present"
