def enter_function():
    print('mũ = **')
    string = input('nhap ham so : ')
    return string
    
    
def convert(string):
    list_1 = []
    i = 0
    while i < len(string):
        if string[i] in "+-":
            list_1.append(string[0:i+1])
            string = string[i+1:]
        i += 1
    list_1.append(string[0:i])
    return list_1            
    
    
def main():
    data = '1+2x+3x**2'
    print(convert(data))
main()