def find_all_subset(l):
    result=list()
    mylist=list()
    if l:
      dfs(0,result,mylist,l)
      print(result)
    else:
      return

def dfs(index,result,mylist,l):
    if index>=len(l):
       result.append(mylist.copy())
       return
    mylist.append(l[index])
    dfs(index+1,result,mylist,l)
    mylist.pop()
    dfs(index+1,result,mylist,l)

if __name__=="__main__":
   find_all_subset([1,2,3])
   


   