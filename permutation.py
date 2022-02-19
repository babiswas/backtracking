def find_permutation(l):
   result=list()
   mylist=list()
   if l:
      find_all_permutation(l,0,len(l),result,mylist)
      print(result)
   else:
     return

def find_all_permutation(l,start,end,result,mylist):
       if start>=end:
          result.append(l.copy())
          return

       for i in range(start,end):
          l[start],l[i]=l[i],l[start]
          find_all_permutation(l,start+1,end,result,mylist)
          l[start],l[i]=l[i],l[start]

if __name__=="__main__":
   find_permutation([1,2,3])
   
          
       