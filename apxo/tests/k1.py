from apxo.tests.infrastructure import *
startfile(__file__, "damage effects")

# Turn rate.

starttestsetup()
A1 = aircraft("A1", "AF", "F-100C"  , "A2-2025", "N", 5, 5.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "HBR,ETR/H,H,H,H")
A1._assert("A2-2020       N     5", 4.5)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-100C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("L")
endtestsetup()
startturn()
A1.move("LVL", "M", "HBR,ETR/H,H,H,H")
asserterror("attempt to declare a turn rate tighter than allowed by the damage, speed, or flight type.")
startturn()
A1.move("LVL", "M", "HBR,BTR/H,H,H,H")
A1._assert("A2-2020       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-100C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("2L")
endtestsetup()
startturn()
A1.move("LVL", "M", "HBR,BTR/H,H,H,H")
asserterror("attempt to declare a turn rate tighter than allowed by the damage, speed, or flight type.")
startturn()
A1.move("LVL", "M", "HBR,HTR/H,H,H,H")
A1._assert("A2-2020       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-100C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("H")
endtestsetup()
startturn()
A1.move("LVL", "M", "HBR,BTR/H,H,H,H")
asserterror("attempt to declare a turn rate tighter than allowed by the damage, speed, or flight type.")
startturn()
A1.move("LVL", "M", "HBR,HTR/H,H,H,H")
A1._assert("A2-2020       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-100C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("C")
endtestsetup()
startturn()
A1.move("LVL", "M", "HBR,HTR/H,H,H,H")
asserterror("attempt to declare a turn rate tighter than allowed by the damage, speed, or flight type.")
startturn()
A1.move("LVL", "M", "HBR,TTR/H,H,H,H")
A1._assert("A2-2020       N     5", 5.0)
endturn()

# HPR

import apxo.capabilities as apcapabilities

starttestsetup()
A1 = aircraft("A1", "AF", "F7U-3"  , "A2-2025", "N", 5, 5.0, "CL")
assert apcapabilities.hasproperty(A1, "HPR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F7U-3"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("L")
assert not apcapabilities.hasproperty(A1, "HPR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F7U-3"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("2L")
assert not apcapabilities.hasproperty(A1, "HPR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F7U-3"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("H")
assert not apcapabilities.hasproperty(A1, "HPR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F7U-3"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("C")
assert not apcapabilities.hasproperty(A1, "HPR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F7U-3"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("K")
assert not apcapabilities.hasproperty(A1, "HPR")
endtestsetup()

# HRR and LRR

starttestsetup()
A1 = aircraft("A1", "AF", "F-5A"  , "A2-2025", "N", 5, 5.0, "CL")
assert apcapabilities.hasproperty(A1, "HRR")
assert not apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-5A"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("L")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-5A"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("2L")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-5A"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("H")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-5A"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("C")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-5A"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("K")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
assert not apcapabilities.hasproperty(A1, "HRR")
assert not apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("L")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("2L")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("H")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("C")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("K")
assert not apcapabilities.hasproperty(A1, "HRR")
assert apcapabilities.hasproperty(A1, "LRR")
endtestsetup()

# NRM

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
assert not apcapabilities.hasproperty(A1, "NRM")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("L")
assert not apcapabilities.hasproperty(A1, "NRM")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("2L")
assert not apcapabilities.hasproperty(A1, "NRM")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("H")
assert apcapabilities.hasproperty(A1, "NRM")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("C")
assert apcapabilities.hasproperty(A1, "NRM")
endtestsetup()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("K")
assert apcapabilities.hasproperty(A1, "NRM")
endtestsetup()

# Preparatory FPs.

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "SLL/H,HL,H,H,H")
asserterror("attempt to slide without sufficient preparatory HFPs.")
startturn()
A1.move("LVL", "M", "SLL/H,H,HL,H,H")
A1._assert("A2-1920       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("L")
endtestsetup()
startturn()
A1.move("LVL", "M", "SLL/H,HL,H,H,H")
asserterror("attempt to slide without sufficient preparatory HFPs.")
startturn()
A1.move("LVL", "M", "SLL/H,H,HL,H,H")
A1._assert("A2-1920       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("2L")
endtestsetup()
startturn()
A1.move("LVL", "M", "SLL/H,H,HL,H,H")
asserterror("attempt to slide without sufficient preparatory HFPs.")
startturn()
A1.move("LVL", "M", "SLL/H,H,H,HL,H")
A1._assert("A2-1920       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("H")
endtestsetup()
startturn()
A1.move("LVL", "M", "SLL/H,H,HL,H,H")
asserterror("attempt to slide without sufficient preparatory HFPs.")
startturn()
A1.move("LVL", "M", "SLL/H,H,H,HL,H")
A1._assert("A2-1920       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A1.takedamage("C")
endtestsetup()
startturn()
A1.move("LVL", "M", "SLL/H,H,HL,H,H")
asserterror("attempt to slide without sufficient preparatory HFPs.")
startturn()
A1.move("LVL", "M", "SLL/H,H,H,HL,H")
A1._assert("A2-1920       N     5", 5.0)
endturn()

# Power

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A"  , "A2-2030", "N", 5, 5.0, "CL")
endtestsetup()
startturn()
A1.move("UD", "AB", "H,H,H,H,HU")
A1._assert("A2-2025       N     4", 6.0)
startturn()
A1.move("LVL", "M", "H,H,H,H,H")
A1._assert("A2-2025       N     5", 5.5)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A"  , "A2-2030", "N", 5, 5.0, "CL")
A1.takedamage("L")
endtestsetup()
startturn()
A1.move("UD", "AB", "H,H,H,H,HU")
A1._assert("A2-2025       N     4", 6.0)
startturn()
A1.move("LVL", "M", "H,H,H,H,H")
A1._assert("A2-2025       N     5", 5.5)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A"  , "A2-2030", "N", 5, 5.0, "CL")
A1.takedamage("2L")
endtestsetup()
startturn()
A1.move("UD", "AB", "H,H,H,H,HU")
A1._assert("A2-2025       N     4", 6.0)
startturn()
A1.move("LVL", "M", "H,H,H,H,H")
A1._assert("A2-2025       N     5", 5.5)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A"  , "A2-2030", "N", 5, 5.0, "CL")
A1.takedamage("H")
endtestsetup()
startturn()
A1.move("UD", "AB", "H,H,H,H,HU")
A1._assert("A2-2025       N     4", 5.5)
startturn()
A1.move("LVL", "M", "H,H,H,H,H")
A1._assert("A2-2025       N     5", 5.0)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A"  , "A2-2030", "N", 5, 5.0, "CL")
A1.takedamage("C")
endtestsetup()
startturn()
A1.move("UD", "AB", "H,H,H,H,HU")
asserterror("aircraft does not have an AB power setting.")
startturn()
A1.move("LVL", "M", "H,H,H,H,H")
A1._assert("A2-2025       N     5", 5.0)
endturn()

# Speed

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A", "A2-2030", "N", 5, 9.0, "CL")
A2 = aircraft("A2", "AF", "F-104A", "A2-2030", "N", 5, 9.0, "CL")
endtestsetup()

startturn()
A1.move("LVL", "AB", "H,H,H,H,H,H,H,H,H")
A1._assert("A2-2021       N     5", 9.0)
A2.takedamage("H")
A2.move("LVL", "AB", "H,H,H,H,H,H,H,H,H")
A2._assert("A2-2021       N     5", 8.0)
endturn()

# Climb capability

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 5, 5.0, "CL")
A2 = aircraft("A2", "AF", "F-80C"  , "A2-2225", "N", 5, 5.0, "CL")
endtestsetup()

startturn()
A1.takedamage("H")
A1.move("SC","M","H,H,C,H,H")
A1._assert("A2-2021       N     5", 5.0)
A2.takedamage("2L")
A2.move("SC","M","H,H,C,H,H")
A2._assert("A2-2221       N     6", 5.0)
endturn()

startturn()
A1.move("SC","M","H,H,C,H,H")
A1._assert("A2-2017       N     6", 5.0)
A2.move("SC","M","H,H,C,H,H")
A2._assert("A2-2217       N     7", 5.0)
endturn()


endfile(__file__)