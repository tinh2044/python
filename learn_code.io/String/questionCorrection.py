def questionCorrection(s):
    
    s = s.replace("/(^[^a-zA-Z\d]+)|([^a-zA-Z\d]+$)/gm, ''").replace("/([^a-zA-Z\d\s,]+)/gm, ' '").replace("/(?!\b\s)\s+|\s+$/gm, ''").replace("/,+|\s,+/gm, ', '")
    return s
print(questionCorrection(" this  is not   a     relevant question , is it??? "))
# print(ord(","))