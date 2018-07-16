
def isSubstring(string1, string2):
   if(string1.find(string2) != -1):
      return True
   return False

if __name__=="__main__":
   string1="waterbottle"
   string2="erbottlew=t"
   if len(string1) == len(string2) and len(string1) is not 0: 
      boolean = isSubstring(string1+string1, string2)
      print(boolean)


