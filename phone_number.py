def letter_comb(str1):
   nu_map={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv",9:"wxyz"}
   result=list()
   sample=list()
   if str1:
      find_text(0,str1,nu_map,result,sample)
      print(result)
   else:
     return

def find_text(index,str1,nu_map,result,sample):
   if len(sample)==len(str1):
      temp=''.join(sample)
      return result.append(temp)
   for ch in nu_map[str1[index]]:
      sample.append(ch)
      find_text(index+1,str1,nu_map,result,sample)
      sample.pop()

if __name__=="__main__":
   letter_comb("233")
   