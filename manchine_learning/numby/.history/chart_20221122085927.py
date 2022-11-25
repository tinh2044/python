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
    
    
def main():
    data = """1+2*x+3*x**2"""
    
main()