def formatString(input):
    input += "1"
    return "".join([input[i] for i in range(len(input) -1) if input[i+1] != " " or input[i]  != " "]).strip()

print(formatString("    a a  a     "))