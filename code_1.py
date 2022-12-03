def sleep_in(weekday, vacation):
    if (weekday and vacation):
        return True

    elif (weekday and not vacation):
        return False

    elif (not weekday and not vacation):
        return True

    elif (not weekday and vacation):
        return True

    else:
        return False


sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)
