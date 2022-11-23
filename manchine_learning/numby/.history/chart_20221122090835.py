def enter_function():
    print('mũ = **, nhập số trước biến')
    string = input('nhap ham so : ')
    return string
    
    
def convert(string):
    list_1 = []
    i = 0
    new_str = ""
    while i < len(string):
        if string[i] == "x":
            string = string.replace("x", "*x", 1)
            i += 2
        else:        
            i += 1
def calc(function):
    x, y = []
    for i in range(-10, 10, 1):
        x.append(i)
        str_i = str(i)
        new_function = function.replace("x", str_i)
        value = exec(new_function)
        y.append(value)
    print(y)
def main():
    data = """1+2x+3x**2"""
    function = convert(data)
    print(function)
    # calc(function)
main()