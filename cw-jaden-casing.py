def to_jaden_case(string):
    """Returns a string in title case"""
    
    return ' '.join(w[:1].upper() + w[1:] for w in string.split(' '))

test = print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
# prints How Can Mirrors Be Real If Our Eyes Aren't Real

