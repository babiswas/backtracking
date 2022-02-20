def palindrome_partition(str1):
    result=list()
    mylist=list()
    if str1:
       find_palindrome(str1,0,len(str1),result,mylist)
       print(result)
    else:
       return

def ispalindrome(str1):
    return str1[::-1]==str1

def find_palindrome(str1,start,end,result,mylist):
    if start==end:
       result.append(mylist.copy())
       return
    for i in range(start,len(str1)):
        if ispalindrome(str1[start:i+1]):
           mylist.append(str1[start:i+1])
           find_palindrome(str1,i+1,end,result,mylist)
           mylist.pop()

if __name__=="__main__":
   palindrome_partition("aab")
   
           
           
           
           
   