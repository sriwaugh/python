def digitCount(num):

        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True 

num = "1210"
print(digitCount(num))