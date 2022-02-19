def find_all_subset(l):
    result=list()
    mylist=list()
    if l:
       find_subset(l,0,len(l),mylist,result)
       print(result)
    else:
      return

def find_subset(l,start,end,mylist,result):
    if mylist not in result:
       result.append(mylist.copy())
    if start<end:
       mylist.append(l[start])
       find_subset(l,start+1,end,mylist,result)
       mylist.pop()
       find_subset(l,start+1,end,mylist,result)

if __name__=="__main__":
   find_all_subset([1,2,3])
