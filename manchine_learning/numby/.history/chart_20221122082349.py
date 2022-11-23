def enter_function():
    print('mũ = **')
    string = input('nhap ham so : ')
    return string
    
    
def convert(string):
    list_1 = []
    i = 0
    while i < len(string):
        if string[i] in "+-*/":
            list_1.append(string[0:i])
            string = string[i+1:]
    return list_1            
    
    
def main():
    data = enter_function()
    print(convert(data))
main()