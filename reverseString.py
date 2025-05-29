def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l , h = 0 , len(s)-1
        while l <= h:
            s[h],s[l] = s[l],s[h]
            h -= 1
            l += 1
    
s = ["h","e","l","l","o"]
print(reverseString(s))