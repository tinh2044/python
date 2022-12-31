def checkStrongPassword(password):
    if len(password) <6 : return False
    
    check_num = lambda x : ord(x) >= 47 and ord(x) <= 57
    check_upper_case = lambda x : ord(x) >= 65  and ord(x) <= 90
    check_lower_case = lambda x : ord(x) >= 97 and ord(x) <= 122
    check_len = lambda x : len(x) > 0
    list_char = " ".join(password).split(" ")
    
    # return list_char
    list_num = list(filter(check_num, list_char))
    list_upper_case = list(filter(check_upper_case, list_char)) or []
    list_lower_case = list(filter(check_lower_case, list_char)) or []
    list_special_character = list(filter(lambda x : not(check_num(x)) and not(check_upper_case(x)) and not(check_lower_case(x)), list_char)) or []
    
    
    if  (check_len(list_num) and check_len(list_lower_case) and check_len(list_upper_case) and check_len(list_special_character)):
        return True
    
    return False
print(checkStrongPassword("12Sa@qqqq"))
    
        