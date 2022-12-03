def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile):
        return True

    elif (a_smile and not b_smile):
        return False

    elif (not a_smile and not b_smile):
        return True

    elif (not a_smile and b_smile):
        return False

    else:
        return False


monkey_trouble(True, True)
monkey_trouble(False, False)
monkey_trouble(True, False)
monkey_trouble(False, False)
