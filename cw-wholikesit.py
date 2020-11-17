def likes(names):
    
    """Converts list of names into strings of likes

    Args:
        names (list): List of string names

    Returns:
        str

    Examples:
        >>> likes(['Pavel', 'Yury', 'Sveta'])
        'Pavel, Yury and Sveta like this'
        """
    
    if names == []:
        return "no one likes this"
    
    elif len(names) == 1:
        return names[0] + " likes this"
        
        
    elif len(names) == 2:
        return names[0] + " and " + names [1] + " like this"
        
        
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
        
    else:  
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
        


if __name__ == '__main__ ':
    import doctest
