def decodeMessage(key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alpa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]
        letters = []
        s = ""
        for ch in key:
            if ch != ' ' and ch not in letters:
                letters.append(ch)
        
        for i in message:
            if i == ' ':
                s += ' '
            else:
                ind =  letters.index(i)
                s += alpa[ind]
        return s


key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"

print(decodeMessage(key,message))