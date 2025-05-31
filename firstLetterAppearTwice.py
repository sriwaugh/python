def repeatedCharacter(s):
        
        res = []
        for i in s:
            if i not in res:
                res.append(i)
            else:
                return i
            

s = "abccbaacz"
print(repeatedCharacter(s))