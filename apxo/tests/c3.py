from apxo.tests.infrastructure import *
startfile(__file__, "speed brakes")

# Speed Brakes

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "1115", "N", 10, 2.5, "CL")
A2 = aircraft("A2", "AF", "F-80C", "1315", "N", 10, 3.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "1515", "N", 10, 3.5, "CL")
A4 = aircraft("A4", "AF", "F-80C", "1715", "N", 10, 4.0, "CL")
endtestsetup()

startturn()
A1.move("LVL",  "N", "HS,H"  )
A1._assert("1113       N    10",  2.5)
A2.move("LVL",  "N", "HS,H"  )
A2._assert("1313       N    10",  3.0)
A3.move("LVL",  "N", "HS,H,H")
A3._assert("1512       N    10",  3.5)
A4.move("LVL",  "N", "HS,H,H")
A4._assert("1712       N    10",  4.0)
endturn()

startturn()
A1.move("LVL",  "N", "HS,H"    )
A1._assert("1111       N    10",  2.0)
A2.move("LVL",  "N", "HS,H,H"  )
A2._assert("1310       N    10",  2.5)
A3.move("LVL",  "N", "HS,H,H"  )
A3._assert("1509       N    10",  3.0)
A4.move("LVL",  "N", "HS,H,H,H")
A4._assert("1708       N    10",  3.5)
endturn()

startturn()
A1.move("LVL",  "N", "HS"    )
A1._assert("1110       N    10",  2.0)
A2.move("LVL",  "N", "HS,H"  )
A2._assert("1308       N    10",  2.5)
A3.move("LVL",  "N", "HS,H"  )
A3._assert("1507       N    10",  3.0)
A4.move("LVL",  "N", "HS,H,H")
A4._assert("1705       N    10",  3.5)
endturn()

starttestsetup()
A1 = aircraft("A1", "AF", "Sea Fury FB.11", "2015", "N", 10, 2.0, "CL")
endtestsetup()

startturn()
A1.move("LVL",  "N", "HS,H")
asserterror("aircraft does not have speedbrakes.")
startturn()
A1.move("LVL",  "N", "H,H")
A1._assert("2013       N    10",  2.0)
endturn()

# Check APJ 53 rules for speed brakes.

starttestsetup(variants=["use APJ 53 rules"], verbose=True)
A1 = aircraft("A1", "AF", "F-80C", "1125", "N", 10, 2.5, "CL")
A2 = aircraft("A2", "AF", "F-80C", "1325", "N", 10, 3.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "1525", "N", 10, 3.5, "CL")
A4 = aircraft("A4", "AF", "F-80C", "1725", "N", 10, 4.0, "CL")
endtestsetup()

startturn()
A1.move("LVL",  "N", "HSS,H"  )
A1._assert("1123       N    10",  2.5)
A2.move("LVL",  "N", "HSS,H,H"  )
A2._assert("1322       N    10",  3.0)
A3.move("LVL",  "N", "HSS,H,H")
A3._assert("1522       N    10",  3.5)
A4.move("LVL",  "N", "HSS,H,H,H")
A4._assert("1721       N    10",  4.0)
endturn()

startturn()
A1.move("LVL",  "N", "HSS,H,H"    )
A1._assert("1120       N    10",  2.0)
A2.move("LVL",  "N", "HSS,H,H"  )
A2._assert("1319       N    10",  2.5)
A3.move("LVL",  "N", "HSS,H,H,H"  )
A3._assert("1518       N    10",  3.0)
A4.move("LVL",  "N", "HSS,H,H,H")
A4._assert("1717       N    10",  3.5)
endturn()

startturn()
A1.move("LVL",  "N", "HSS,H"  )
A1._assert("1118       N    10",  2.0)
A2.move("LVL",  "N", "HSS,H"  )
A2._assert("1317       N    10",  2.5)
A3.move("LVL",  "N", "HSS,H,H"  )
A3._assert("1515       N    10",  3.0)
A4.move("LVL",  "N", "HSS,H,H")
A4._assert("1714       N    10",  3.5)
endturn()

startturn()
A1.move("LVL",  "N", "HSS,H"  )
A1._assert("1116       N    10",  1.5)
A2.move("LVL",  "N", "HSS,H,H"  )
A2._assert("1314       N    10",  2.0)
A3.move("LVL",  "N", "HSS,H,H"  )
A3._assert("1512       N    10",  2.5)
A4.move("LVL",  "N", "HSS,H,H,H")
A4._assert("1710       N    10",  3.0)
endturn()

endfile(__file__)