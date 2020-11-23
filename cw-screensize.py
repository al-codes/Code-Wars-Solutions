def find_screen_height(width, ratio): 
    """Returns screen height given a width and w:h ratio"""

    dimensions = ratio.split(":")

    # Calculates height value
    height = ((width * int(dimensions[1]) // (int(dimensions[0]))))

    #Returns screen dimensions as a string
    return str(width) + "x" + str(height)


test1 = print(find_screen_height(1024, "4:3"))
#returns "1024x768"

test2 = print(find_screen_height(1280, "16:9"))
#returns "1280x720"





