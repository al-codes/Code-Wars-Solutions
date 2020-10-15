def repeat_str(repeat_amt, string):
    """Returns given string a repeated amount of times as defined by user"""
    
    return repeat_amt * string

test1 = print(repeat_str(6, "I"))
# should print "IIIIII"
test2 = print(repeat_str(5, "Hello"))
# should print "HelloHelloHelloHelloHello"