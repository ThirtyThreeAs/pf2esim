import src.dice as dice

def dice_regression():
    # Test 1.a: Default values
    dice_test_1 = dice.Dice()
    assert(dice_test_1.sides==20)
    assert(dice_test_1.bonus==0)

    # Test 1.b: Test roll
    assert(dice_test_1.roll()>0)


    # Test 2.a: Non-default values
    dice_test_2 = dice.Dice(6,3)
    assert(dice_test_2.sides==6)
    assert(dice_test_2.bonus==3)

    # Test 2.b: Test roll
    # min(3d6+3) should be 3+3=6
    # max(3d6+3) should be 18+3=21
    for i in range(100):
        assert(dice_test_2.roll(3)>=6)
        assert(dice_test_2.roll(3)<=21)
