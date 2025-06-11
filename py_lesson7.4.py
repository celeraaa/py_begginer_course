def common_elements():
    thirds = set(range( 0, 100, 3))
    fifths = set(range( 0, 100, 5))
    commons = thirds.intersection(fifths)
    print(commons)
    pass
common_elements()