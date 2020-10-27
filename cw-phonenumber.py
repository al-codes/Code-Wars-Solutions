def create_phone_number(str_list):
    """Returns a string of numbers in phone number format (XXX) XXX-XXXX"""

  
    str_list = [str(i) for i in str_list]

    str_list.insert(0,'(')
    str_list.insert(4,') ')
    str_list.insert(8,'-')
    str1 = ''

    return str1.join(str_list)

test = print(create_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# prints (012) 345-6789