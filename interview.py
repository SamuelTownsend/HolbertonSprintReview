python
def find_nail_day(n):
    # Loop over each day of the road trip
    for i in range(n):
        # Check if the nail was present on the i-th day
        if not nailIn(i):
            # If the nail was not present, return the day
            return i
    # If the nail was present on every day, return -1
    return -1
