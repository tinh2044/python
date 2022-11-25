def enter_function():
    print('mũ = **, nhập số trước biến')
    string = input('nhap ham so : ')
    return string
    
    
def convert(string):
    list_1 = []
    i = 0
    while i < len(string):
        if string[i] in "+-":
            list_1.append(string[0:i])
            string = string[i:]
        i += 1
    list_1.append(string[0:i])
    return list_1            
    
    
def main():
    data = '1+2x+3x**2'
    print(eval(data))
    # print(convert(data))
    dict1 = {'one':1, 'two':2, 'three': {'three.1': 3.1, 'three.2': 3.2 }}
    str1 = str(dict1)
    
    dict2 = eval(str1)
    
    print( data)
main()