def isPlaindrome(s,i,j):
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    return isPlaindrome(s,i+1,j-1)

s="nitin"
print(isPlaindrome(s,0,len(s)-1))
    

