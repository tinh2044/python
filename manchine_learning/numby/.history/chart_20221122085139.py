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
    pass
main()
x = 1
data = """1+2*x+3*x**2"""
print(exec(data))

def exec_code():
    LOC = """
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(5))
"""
    exec(LOC)
     
# Driver Code
exec_code()