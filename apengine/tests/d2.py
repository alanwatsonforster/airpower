from apengine.tests.infrastructure import *
startfile(__file__, "banking")


# Turns and banking with normal RR aircraft

startsetup()
A1 = aircraft("A1", "F-80C" , 2015, "N"  , 10, 4.0, "CL")
endsetup()
startturn()
A1.move("LVL",  "M", "H/WL,EZL/H,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/WL,EZR/H,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKL,EZR/H,H,H")
asserterror("attempt to declare a turn to R while banked to L.")
A1.move("LVL",  "M", "H/BKR,EZL/H,H,H")
asserterror("attempt to declare a turn to L while banked to R.")
A1.move("LVL",  "M", "H/BKL,H/BKR,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,H/BKL,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,H/WL,H/BKL,H/WL")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,EZR/H,H,HR")
A1._assert("2011       NNE  10",  4.0)
A1.move("LVL",  "M", "H/BKL,EZL/H,H,HL")
A1._assert("2011       NNW  10",  4.0)
endturn()

# Turns and banking with LRR aircraft

startsetup()
A1 = aircraft("A1", "Meteor F.8" , 2015, "N"  , 10, 4.0, "CL")
endsetup()
startturn()
A1.move("LVL",  "M", "H/WL,EZL/H,H,H")
asserterror("attempt to declare a turn to L while not banked to L in a LRR aircraft.")
A1.move("LVL",  "M", "H/WL,EZR/H,H,H")
asserterror("attempt to declare a turn to R while not banked to R in a LRR aircraft.")
A1.move("LVL",  "M", "H/BKL,EZR/H,H,H")
asserterror("attempt to declare a turn to R while not banked to R in a LRR aircraft.")
A1.move("LVL",  "M", "H/BKR,EZL/H,H,H")
asserterror("attempt to declare a turn to L while not banked to L in a LRR aircraft.")
A1.move("LVL",  "M", "H/BKL,H/BKR,H,H")
asserterror("attempt to bank to R while banked to L in a LRR aircraft.")
A1.move("LVL",  "M", "H/BKR,H/BKL,H,H")
asserterror("attempt to bank to L while banked to R in a LRR aircraft.")
A1.move("LVL",  "M", "H/BKR,H/WL,H/BKL,H/WL")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,EZR/H,H,HR")
A1._assert("2011       NNE  10",  4.0)
A1.move("LVL",  "M", "H/BKL,EZL/H,H,HL")
A1._assert("2011       NNW  10",  4.0)
endturn()

# Turns and banking with HRR aircraft

startsetup()
A1 = aircraft("A1", "F-5A" , 2015, "N"  , 10, 4.0, "CL")
endsetup()
startturn()
A1.move("LVL",  "M", "H/WL,EZL/H,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/WL,EZR/H,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKL,EZR/H,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,EZL/H,H,H")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKL,H/BKR,H,H" )
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,H/BKL,H,H" )
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,H/WL,H/BKL,H/WL")
A1._assert("2011       N    10",  4.0)
A1.move("LVL",  "M", "H/BKR,EZR/H,H,HR")
A1._assert("2011       NNE  10",  4.0)
A1.move("LVL",  "M", "H/BKL,EZL/H,H,HL")
A1._assert("2011       NNW  10",  4.0)
endturn()

# Turns and banking with HRRCL aircraft

startsetup(verbose=False)
A1 = aircraft("A1", "Yak-9D" , 2010, "N"  , 10, 3.5, "CL")
A2 = aircraft("A2", "Yak-9D" , 2210, "N"  , 10, 3.5, "1/2")
A3 = aircraft("A3", "Yak-9D" , 2410, "N"  , 10, 3.0, "DT")
endsetup()

startturn()
A1.move("LVL",  "HT", "BTL/H,BTR/H,H")
A1._assert("2007       N    10",  3.5)
A2.move("LVL",  "HT", "BTL/H,BTR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
A2.move("LVL",  "HT", "BTL/H,WL/H,BTR/H")
A2._assert("2207       N    10",  3.5)
A3.move("LVL",  "HT", "HTL/H,HTR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
A3.move("LVL",  "HT", "HTL/H,WL/H,HTR/H")
A3._assert("2407       N    10",  3.0)
endturn()

endfile(__file__)