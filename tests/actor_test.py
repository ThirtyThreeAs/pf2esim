import src.actor as actor

def actor_regression():
    # Test 1: Initialization
    fighter_name = "Fighter"
    fighter_hp = 20
    fighter_ac = 18
    fighter_strat = None
    actor_test_1 = actor.SimpleActor(fighter_name, fighter_hp, fighter_ac, fighter_strat)
    assert(actor_test_1.name==fighter_name)
    assert(actor_test_1.maxhp==fighter_hp)
    assert(actor_test_1.ac==fighter_ac)
    assert(actor_test_1.strat==None)

    # Test 2: reset
    actor_test_1.hp = 0
    actor_test_1.block = True
    actor_test_1.reset()
    assert(actor_test_1.hp==actor_test_1.maxhp)
    assert(actor_test_1.block==False)

    # Test 3: roundreset
    actor_test_1.block = True
    actor_test_1.roundreset()
    assert(actor_test_1.block==False)

    # Test 4: raiseshield
    actor_test_1.reset()
    actor_test_1.raiseshield()
    assert(actor_test_1.block==True)

    # Test 5.a getac
    actor_test_1.reset()
    assert(actor_test_1.getac()==fighter_ac)
    actor_test_1.raiseshield()
    assert(actor_test_1.getac()==(fighter_ac+2))