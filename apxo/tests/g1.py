from apxo.tests.infrastructure import *

startfile(__file__, "displacement rolls")

# Displacement Rolls

# Check the position after a displacement roll.

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "E", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "E", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-2008       E    10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2609       E    10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "ENE", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "ENE", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1906       ENE  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2608       ENE  10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "NNE", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "NNE", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1806       NNE  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2506       NNE  10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "N", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "N", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1606       N    10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2406       N    10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "NNW", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "NNW", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1506       NNW  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2206       NNW  10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "WNW", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "WNW", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1408       WNW  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2106       WNW  10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "W", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "W", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1409       W    10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2008       W    10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "WSW", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "WSW", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1510       WSW  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2009       WSW  10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "SSW", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "SSW", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1611       SSW  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2110       SSW  10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "S", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "S", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1811       S    10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2211       S    10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "SSE", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "SSE", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-1910       SSE  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2411       SSE  10", 3.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "AF", "F-80C", "A1-1708", "ESE", 10, 3.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2308", "ESE", 10, 3.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "M", "H,DRL/H,HL")
A1._assert("A1-2009       ESE  10", 3.0)
A2.move("LVL", "M", "H,DRR/H,HR")
A2._assert("A1-2510       ESE  10", 3.0)
endturn()

# Check we can carry preparatory HFPs from one turn to the next.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 10, 7.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", 0.5, "H,H,H,H,H,H,DRL/H")
A1._assert("A1-1708       N    10", 7.0)
endturn()

startturn()
A1.move("LVL", 0.5, "HL,H,H,H,H,H,H")
A1._assert("A1-1602       N    10", 7.0)
endturn()

# Check VFPs and unloaded HFPs are not counted as preparatory HFPs.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 10, 7.0, "CL")
endtestsetup()
startturn()
A1.move("UD", "AB", "H,DRL/HU,HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("UD", "AB", "H,DRL/HU,HUL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("UD", "AB", "H,DRL/H,HL,HU,HU,HU,HU")
A1._assert("A1-1609       N     6", 8.0)
startturn()
A1.move("SD", "AB", "H,DRL/D,D,HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("SD", "AB", "H,DRL/H,DL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("SD", "AB", "H,DRL/H,HL,D,D,D,D")
A1._assert("A1-1613       N     6", 8.0)
startturn()
A1.move("ZC", "AB", "H,DRL/C,HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("ZC", "AB", "H,DRL/H,CL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("ZC", "AB", "H,DRL/H,HL,C,C,C,C")
A1._assert("A1-1613       N    14", 6.5)
endturn()

startturn()
A1.move("ZC", "AB", "H,DRL/C,HL,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("LVL", "M", "H,H,H,H,H,H")
A1._assert("A1-1607       N    14", 7.0)
endturn()

# Check the required preparatory HFPs, both at subsonic and supersonic speeds.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 7, 7.0, "CL")
A2 = aircraft("A2", "AF", "F-104A", "A1-1915", "N", 7, 7.5, "CL")
A3 = aircraft("A3", "AF", "F-104A", "A1-2115", "N", 20, 6.5, "CL")
A4 = aircraft("A4", "AF", "F-104A", "A1-2315", "N", 20, 7.0, "CL")
endtestsetup()
startturn()
A1.move("LVL", "AB", "H,DRL/HL,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A2.move("LVL", "AB", "H,DRL/H,HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A3.move("LVL", "AB", "H,DRL/HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A4.move("LVL", "AB", "H,DRL/H,HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("LVL", "AB", "H,DRL/H,HL,H,H,H,H")
A1._assert("A1-1609       N     7", 7.5)
A2.move("LVL", "AB", "H,DRL/H,H,HL,H,H,H")
A2._assert("A1-1809       N     7", 7.5)
A3.move("LVL", "AB", "H,DRL/H,HL,H,H,H")
A3._assert("A1-2010       N    20", 7.0)
A4.move("LVL", "AB", "H,DRL/H,H,HL,H,H,H")
A4._assert("A1-2209       N    20", 7.0)
endturn()

# Check additional preparatory HFPs required at altitude.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1515", "N", 20, 12.0, "CL")
A2 = aircraft("A2", "AF", "F-104A", "A1-1715", "N", 30, 12.0, "CL")
A3 = aircraft("A3", "AF", "F-104A", "A1-1915", "N", 40, 12.0, "CL")
A4 = aircraft("A4", "AF", "F-104A", "A1-2115", "N", 50, 12.0, "CL")
A5 = aircraft("A5", "AF", "F-104A", "A1-2315", "N", 61, 12.0, "CL")
endtestsetup()

startturn()
A1.move("LVL", "AB", "H,DRL/H,HL,H,H,H,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A2.move("LVL", "AB", "H,DRL/H,H,HL,H,H,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A3.move("LVL", "AB", "H,DRL/H,H,H,HL,H,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A4.move("LVL", "AB", "H,DRL/H,H,H,H,HL,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A5.move("LVL", "AB", "H,DRL/H,H,H,H,H,HL,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
startturn()
A1.move("LVL", "AB", "H,DRL/H,H,HL,H,H,H,H,H,H,H,H")
A1._assert("A1-1404       N    20", 12.0)
startturn()
A2.move("LVL", "AB", "H,DRL/H,H,H,HL,H,H,H,H,H,H,H")
A2._assert("A1-1604       N    30", 12.0)
startturn()
A3.move("LVL", "AB", "H,DRL/H,H,H,H,HL,H,H,H,H,H,H")
A3._assert("A1-1804       N    40", 12.0)
startturn()
A4.move("LVL", "AB", "H,DRL/H,H,H,H,H,HL,H,H,H,H,H")
A4._assert("A1-2004       N    50", 12.0)
startturn()
A5.move("LVL", "AB", "H,DRL/H,H,H,H,H,H,HL,H,H,H,H")
A5._assert("A1-2204       N    61", 12.0)
endturn()

# Check allowed flight types.

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1415", "N", 20, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-1615", "N", 20, 4.0, "CL")
endtestsetup()

startturn()
A1.move("SC", "M", "DRL/H,H,H,C")
asserterror("attempt to declare a displacement roll while flight type is SC.")
startturn()
A2.move("SC", "M", "DRR/H,H,H,C")
asserterror("attempt to declare a displacement roll while flight type is SC.")
startturn()
A1.move("SC", "M", "H,H,H,C")
A2.move("SC", "M", "H,H,H,C")
endturn()

startturn()
A1.move("VC", "M", "DRL/H,C2,C2,C2")
asserterror("attempt to declare a displacement roll while flight type is VC.")
startturn()
A2.move("VC", "M", "DRR/H,C2,C2,C2")
asserterror("attempt to declare a displacement roll while flight type is VC.")
startturn()
A1.move("SD", "M", "H,H,H,D")
A2.move("SD", "M", "H,H,H,D")
endturn()

startturn()
A1.move("VD", "M", "DRL/H,H,D2,D2,D2")
asserterror("attempt to declare a displacement roll while flight type is VD.")
startturn()
A2.move("VD", "M", "DRR/H,H,D2,D2,D2")
asserterror("attempt to declare a displacement roll while flight type is VD.")
startturn()
A1.move("SD", "M", "H,H,H,D")
A2.move("SD", "M", "H,H,H,D")
endturn()


# TODO: Check multiple rolls in one turn. The issue is the F-104 is GSSM.

# checkstarttestsetup(verbose=False)
# A1 = aircraft("A1", "AF", "F-104A", "A1-1715", "N", 20, 12.0, "CL")

# checkendtestsetup()
# checkstartturn()
# A1.move("LVL",  "AB", "DRL/H,H,HL,DRR/H,H,HR,DRL/H,H,HL,DRR/H,H,HR")
# A1._assert("A1-1705       N    20",  11.5)
# A1.move("LVL",  "AB", "DRL/H,H,HL,H,H,H,H,H,H,DRR/H,H,HR"          )
# A1._assert("A1-1704       N    20",  12.0)
# A1.move("ZC" ,  "AB", "DRL/H,H,HL,H,C,C,C,C,H,DRR/H,H,HR"          )
# A1._assert(""1708"       N    24",  11.5)
# A1.move("SD" ,  "AB", "DRL/H,H,HL,H,D,D,D,D,H,DRR/H,H,HR"          )
# A1._assert(""1708"       N    16",  10.5)
# checkendturn()

# Check we can select the bank after a DR.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-80C", "A1-1715", "N", 20, 4.0, "CL")

endtestsetup()
startturn()
A1.move("LVL", "M", "DRL/H,HL/BL,EZR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
startturn()
A1.move("LVL", "M", "DRL/H,HL/WL,EZR/H,H")
A1._assert("A1-1612       N    20", 4.0)
startturn()
A1.move("LVL", "M", "DRL/H,HL/BR,EZR/H,H")
A1._assert("A1-1612       N    20", 4.0)
startturn()
A1.move("LVL", "M", "DRR/H,HR/BL,EZR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
startturn()
A1.move("LVL", "M", "DRR/H,HR/WL,EZR/H,H")
A1._assert("A1-1812       N    20", 4.0)
startturn()
A1.move("LVL", "M", "DRR/H,HR/BR,EZR/H,H")
A1._assert("A1-1812       N    20", 4.0)
startturn()
A1.move("LVL", "M", "DRL/H,HL/BR,EZL/H,H")
asserterror("attempt to declare a turn to L while banked to R.")
startturn()
A1.move("LVL", "M", "DRL/H,HL/WL,EZL/H,H")
A1._assert("A1-1612       N    20", 4.0)
startturn()
A1.move("LVL", "M", "DRL/H,HL/BL,EZL/H,H")
A1._assert("A1-1612       N    20", 4.0)
startturn()
A1.move("LVL", "M", "DRR/H,HR/BR,EZL/H,H")
asserterror("attempt to declare a turn to L while banked to R.")
startturn()
A1.move("LVL", "M", "DRR/H,HR/WL,EZL/H,H")
A1._assert("A1-1812       N    20", 4.0)
startturn()
A1.move("LVL", "M", "DRR/H,HR/BL,EZL/H,H")
A1._assert("A1-1812       N    20", 4.0)
endturn()

# Rolls and GSSM/PSSM aircraft

# F-104A is GSSM, F-102A is PSSM, and F-100A is neither.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A1-1215", "N", 20, 7.5, "CL")  # GSSM
A2 = aircraft("A2", "AF", "F-100A", "A1-1415", "N", 20, 7.5, "CL")
A3 = aircraft("A3", "AF", "F-102A", "A1-1615", "N", 20, 7.5, "CL")  # PSSM
endtestsetup()

startturn()

A1.move("LVL", "AB", "H,H,H,H,H,H,H")
A1._assert("A1-1208       N    20", 8.0)
A2.move("LVL", "AB", "H,H,H,H,H,H,H")
A2._assert("A1-1408       N    20", 7.5)
A3.move("LVL", "AB", "H,H,H,H,H,H,H")
A3._assert("A1-1608       N    20", 7.5)

startturn()

A1.move("LVL", "AB", "DRR/H,H,HR,DRL/H,H,HL,H")
A1._assert("A1-1209       N    20", 7.5)
A2.move("LVL", "AB", "DRR/H,H,HR,DRL/H,H,HL,H")
A2._assert("A1-1409       N    20", 7.0)
A3.move("LVL", "AB", "DRR/H,H,HR,DRL/H,H,HL,H")
A3._assert("A1-1609       N    20", 6.5)

endturn()

# Additional prepatory FPs in version 2.4.

starttestsetup(variants=["use version 2.4 rules"], verbose=False)
A1 = aircraft("A1", "AF", "F-104A", "A2-2025", "N", 20, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-104A", "A2-2225", "N", 20, 5.0, "CL")
A3 = aircraft("A3", "AF", "F-104A", "A2-2425", "N", 20, 6.0, "CL")
endtestsetup()

startturn()
A1.move("LVL", "M", "DRR/H/R,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
A2.move("LVL", "M", "DRR/H/R,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")
A3.move("LVL", "M", "DRR/H,H/R,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory FPs.")

startturn()
A1.move("LVL", "M", "DRR/H,H/R,H,H")
A1._assert("A2-2121       N    20", 4.0)
A2.move("LVL", "M", "DRR/H,H/R,H,H,H")
A2._assert("A2-2320       N    20", 5.0)
A3.move("LVL", "M", "DRR/H,H,H/R,H,H,H")
A3._assert("A2-2519       N    20", 6.0)
endturn()

# In version 2.4, the preparatory FPs can be HFPs or VFPs, but the roll must
# be executed on an HFP.

starttestsetup(variants=["use version 2.4 rules"])
A1 = aircraft("A1", "AF", "F-104A", "A2-2025", "N", 20, 6.0, "CL")
endtestsetup()

startturn()
A1.move("ZC", "M", "H,H,H,H,H,C")
endturn()

startturn()
A1.move("ZC", "M", "DRR/C,C,C/R")
asserterror("attempt to roll on a VFP.")

startturn()
A1.move("ZC", "M", "DRR/C,C,H/R,H,H,H")
A1._assert("A2-2116       N    23", 6.0)
endturn()

endfile(__file__)
