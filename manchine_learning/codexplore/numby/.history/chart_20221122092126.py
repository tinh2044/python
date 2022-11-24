import matplotlib.pyplot as plt

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
            string = string[:i] + "*" + string[i:]
            i += 2
        else:        
            i += 1
    return string
def calc(function):
    x = []
    y = []
    for i in range(-10, 10, 1):
        x.append(i)
        str_i = "(" + str(i) + ")" 
        new_function = function.replace("x", str_i)
        value = eval(new_function)
        y.append(value)
    print(x)
    # chart(x, y)
    return x,y
    
def chart(x,y):
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.plot(x,y)
    plt.show()    
def main():
    data = """1+2x+3x**2"""
    function = convert(data)
    calc(function)
main()
# print(plt.style.available)