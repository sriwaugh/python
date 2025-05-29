def strongPasswordCheckerII(password):
        
        n = len(password)
        low = False
        high = False
        num = False
        spl_ans = False
        spl = "!@#$%^&*()-+"
        
        for i in range(n):
            if password[i].islower():
                low = True
            if password[i].isupper():
                high = True
            if password[i].isdigit():
                num = True
            if password[i] in spl:
                spl_ans = True
        for i in range(n-1):
            if password[i] == password[i+1]:
                return False
        if low and high and num and spl_ans and n >= 8:
            return True
        else:
            return False

password = "IloveLe3tcode!"
print(strongPasswordCheckerII(password))