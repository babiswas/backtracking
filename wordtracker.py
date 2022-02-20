import copy
def word_tracker(word):
    mat=[['A','B','C','E'],['S','F','C','S'],['A','D','E','F']]
    path=list()
    l=[False]
    visited=[[False for i in range(len(mat[0]))] for i in range(len(mat))]
    find_word(mat,0,0,len(mat),len(mat[0]),path,'',l,visited,word)
    str2=''
    print(path)
    for x,y in path:
       str2+=mat[x][y]
    if str2==word:
      print("Word exist in the grid")


def issafe(mat,x,y,m,n,ch):
    if x>=m or x<0:
       return False
    if y>=n or y<0:
       return False
    if mat[x][y]!=ch:
       return False
    return True


def get_current_index(str1,str2):
   for i in str2:
     str1.pop(0)
   if str1:
      return str1[0]
   else:
      return ''


def find_word(mat,x,y,m,n,path,str1,l,visited,target):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited[x][y]=True
    str1=str1+mat[x][y]
    print(str1)
    path.append((x,y))
    if str1==target:
       print(str1)
       l[0]=True
       return
    else:
       ch=copy.deepcopy(target).replace(str1,'')[0]
       print(ch)
       for i in range(4):
          X=x+dx[i]
          Y=y+dy[i]
          if issafe(mat,X,Y,m,n,ch):
              if visited[X][Y]==False:
                find_word(mat,X,Y,m,n,path,str1,l,visited,target)
       if l[0]==False:
          path.pop()
          str1=str1[:-1]

if __name__=="__main__":
   word_tracker("ABCCED")
   
                
             
       
    
   
     