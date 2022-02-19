def find_all_permutation(l):
    if l:
       result=dfs(l)
       print(result)
    else:
      return

def dfs(l):
    result=list()
    if len(l)==1:
       return [l.copy()]
    for i in range(len(l)):
        item=l.pop(0)
        res=dfs(l)
        for r in res:
          r.append(item)
        result.extend(res)
        l.append(item)
    return result

if __name__=="__main__":
   find_all_permutation([1,2,3])

       

