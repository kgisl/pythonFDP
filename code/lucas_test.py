from lucas import sequence_gen

def test_for_three_elements():
    assert sequence_gen(3) == [0, 0, 1]

def test_for_five_elements():
    assert sequence_gen(5) == [0, 0, 1, 1, 2] 
    
def test_for_big_numbers():
    assert sequence_gen(20) == \
          [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513]
          