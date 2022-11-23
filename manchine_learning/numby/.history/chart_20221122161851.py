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
            if ((string[i-1] in '1234567890') == False or (i == 1)):
                string = string[0:i] +'1' + string[i:]
            string = string[:i] + "*" + string[i:]
            i += 2
        else:        
            i += 1
    return string
def calc(function):
    x = []
    y = []
    i = -10
    while i < 10:
        x.append(i)
        str_i = "(" + str(i) + ")" 
        new_function = function.replace("x", str_i)
        try:
            value = eval(new_function)
            y.append(value)
        except:
            break
        i += 1
    return x,y
    
def chart(x,y):
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.axis()
    plt.plot(x,y)
    plt.show()    
def main():
    data = "4x**4 -3x**3 +2x**2 -1-x**5"
    function = convert(data)
    x,y = calc(function)
    chart(x, y)
main()
# print(plt.style.available)