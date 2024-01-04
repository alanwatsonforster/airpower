from apxo.tests.infrastructure import *
startfile(__file__, "dives")

# Dives

# Steep Dives

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N"  , 20, 3.0, "CL")
endtestsetup()

startturn()
A1.move("SD",  "N", "H,H,H")
asserterror("too few VFPs.")
startturn()
A1.move("SD",  "N", "H,D,H")
A1._assert("A1-1813       N    19",  3.0)
startturn()
A1.move("SD",  "N", "H,D,D")
A1._assert("A1-1814       N    18",  3.0)
startturn()
A1.move("SD",  "N", "H,D3,D3")
asserterror("attempt to dive 3 levels per VFP while the flight type is SC.")
startturn()
A1.move("SD",  "N", "H,D2,D2")
A1._assert("A1-1814       N    16",  3.5)
endturn()

startturn()
A1.move("SD",  "N", "D,D,D")
asserterror("too few HFPs.")
startturn()
A1.move("SD",  "N", "H,D2,H")
A1._assert("A1-1812       N    14",  4.0)
startturn()
A1.move("SD",  "N", "H,D2,D2")
A1._assert("A1-1813       N    12",  4.5)
endturn()

startturn()
A1.move("SD",  "M", "BTR/H,H,H,H,HR")
asserterror("too few VFPs.")
endturn()

# Unloaded Dives

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N"  , 20, 3.0, "CL")
endtestsetup()

startturn()
A1.move("UD",  "M", "HU,H,HU")
asserterror("unloaded HFPs must be continuous.")
startturn()
A1.move("UD",  "N", "H,H,H")
asserterror("too few unloaded HFPs.")
startturn()
A1.move("UD",  "N", "H,HU,H")
A1._assert("A1-1812       N    19",  3.0)
endturn()

startturn()
A1.move("UD",  "N", "HU,HU,HU")
A1._assert("A1-1809       N    16",  3.5)
endturn()

startturn()
A1.move("VD",  "N", "H,D2,D2")
A1._assert("A1-1808       N    12",  4.5)
endturn()

startturn()
A1.move("UD",  "N", "H,H,H,H,H")
asserterror("too few unloaded HFPs.")
startturn()
A1.move("UD",  "N", "HU,H,H,H,H")
asserterror("too few unloaded HFPs.")
startturn()
A1.move("UD",  "N", "TTR/HU,HUR,H,H,H")
asserterror("attempt to turn faster than the declared turn rate.")
startturn()
A1.move("UD",  "N", "TTR/H,HR,H,HU,HU")
A1._assert("A1-1903/2004  NNE  10",  5.0)
startturn()
A1.move("UD",  "N", "HU,HU,H,H,H")
A1._assert("A1-1803       N    10",  5.0)
endturn()

# Verify that attacks cannot happen on unloaded FPs.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-80C", "A1-2015", "N", 20, 4.0, "CL")
endtestsetup()

startturn()
A1.move("UD"    ,  "M", "HU,HU,HU,HU/AA(GN)()()" )
asserterror("attempt to use weapons while unloaded.")
startturn()
A1.move("UD"    ,  "M", "HU,HU,HU,HU"     )
A1._assert("A1-2011       N    16",  4.5)
endturn()

# Vertical Dives

starttestsetup(sheets=[["A1"],["A2"]])
A1 = aircraft("A1", "AF", "F-80C", "A2-1820", "N"  , 17, 5.0, "CL")
endtestsetup()

startturn()
A1.move("SD",  "N", "H,H,H,H,H")
asserterror("too few VFPs.")
startturn()
A1.move("SD",  "N", "H,H,H,H,D")
A1._assert("A1-1816       N    16",  5.0)
endturn()

startturn()
A1.move("VD",  "M", "H,D3,D3,D3,D3")
asserterror("too few HFPs.")
startturn()
A1.move("VD",  "M", "H,H,H,D3,D3")
asserterror("too many HFPs.")
startturn()
A1.move("VD",  "M", "H,H,D1,D3,D3")
asserterror("attempt to dive 1 level per VFP while the flight type is VD.")
startturn()
A1.move("VD",  "M", "H,H,D1,D3,D3")
asserterror("attempt to dive 1 level per VFP while the flight type is VD.")
startturn()
A1.move("VD",  "M", "H,H,D2,D2,D2")
A1._assert("A1-1814       N    10",  6.5)
endturn()

startturn()
A1.move("VC",  "M", "D2,D2,D2,D2,D2,D2")
asserterror("flight type immediately after VD cannot be VC.")
startturn()
A1.move("SC",  "M", "D2,D2,D2,D2,D2,D2")
asserterror("flight type immediately after VD cannot be SC.")
startturn()
A1.move("ZC",  "M", "D2,D2,D2,D2,D2,D2")
asserterror("flight type immediately after VD cannot be ZC.")
startturn()
A1.move("LVL",  "M", "D2,D2,D2,D2,D2,D2")
asserterror("flight type immediately after VD cannot be LVL.")
startturn()
A1.move("SD",  "M", "H,H,H,H,D,D")
asserterror("too few VFPs.")
startturn()
A1.move("SD",  "M", "H,H,H,D,D,D")
A1._assert("A1-1811       N     7",  6.5)
startturn()
A1.move("SD",  "M", "H,H,D,D,D,D")
A1._assert("A1-1812       N     6",  6.5)
startturn()
A1.move("SD",  "M", "H,D,D,D,D,D")
asserterror("too few HFPs.")
startturn()
A1.move("UD",  "M", "H,H,H,H,HU,HU")
asserterror("too few unloaded HFPs.")
startturn()
A1.move("UD",  "M", "H,H,H,HU,HU,HU")
A1._assert("A1-1808       N     7",  6.5)
startturn()
A1.move("UD",  "M", "HU,HU,HU,HU,HU,HU")
A1._assert("A1-1808       N     4",  6.5)
endturn()

starttestsetup(sheets=[["A1"],["A2"]])
A1 = aircraft("A1", "AF", "F-80C", "A2-1817", "N"  , 45, 2.5, "CL")
endtestsetup()

startturn()
A1.move("SD",  "N", "H,H")
asserterror("too few VFPs.")
startturn()
A1.move("SD",  "N", "H,D")
A1._assert("A1-1816       N    44",  2.5)
endturn()

startturn()
A1.move("VD",  "M", "H,D2,D2")
A1._assert("A1-1815       N    40",  3.5)
endturn()

startturn()
A1.move("VD",  "M", "D3,D3,D3")
A1._assert("A1-1815       N    31",  6.0)
endturn()

startturn()
A1.move("VD",  "M", "D3,D3,D3,D3,D3,D3")
A1._assert("A1-1815       N    13",  6.5)
endturn()

# Recoverty from Vertical Dives.

starttestsetup(sheets=[["A1"],["A2"]], variants=["use version 2.4 rules"])
A1 = aircraft("A1", "AF", "F-80C", "A2-1817", "N"  , 45, 3.5, "CL")
endtestsetup()

startturn()
A1.move("SD",  "M", "H,H,D2")
A1._assert("A1-1815       N    43",  4.0)
endturn()

startturn()
A1.move("VD",  "M", "H,D2,D2,D2")
A1._assert("A1-1814       N    37",  5.5)
endturn()

# The dive was crafted so that the aircraft has a speed of 5.5 but
# has 6 FP. Thus, it must dive for 3 VFPs on the next turn rather than 2.

startturn()
A1.move("SD",  "M", "D,D,H,H,H,H")
asserterror("too few VFPs.")

startturn()
A1.move("SD",  "M", "D,D,D,H,H")
A1._assert("A1-1812       N    34",  5.5)
endturn()

# Free Descent

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-1815", "N"  , 10, 4.0, "CL")
endtestsetup()

startturn()
A1.move("LVL",  "M", "HD2,H,H,H")
asserterror("'HD2' is not a valid element.")
startturn()
A1.move("LVL",  "M", "HD,H,H,HD")
asserterror("free descent cannot only be taken once per move.")
startturn()
A1.move("LVL",  "M", "H,H,H,HD")
A1._assert("A1-1811       N     9",  4.0)
endturn()

startturn()
A1.move("LVL",  "M", "HD,H,H,H")
A1._assert("A1-1807       N     8",  4.5)
endturn()

# In version 2.4, normal aircraft can go from VD to LVL if their speed is no
# more than 2.0.

starttestsetup(variants=["use version 2.4 rules"])
A1 = aircraft("A1", "AF", "F-80C"  , "A2-2025", "N", 20, 2.0, "CL")
A2 = aircraft("A2", "AF", "F-80C"  , "A2-2225", "N", 20, 2.5, "CL")
endtestsetup()

startturn()
A1.move("VD/HRD", "I", "S1/H,D2")
A1._assert("A2-2024       N    18", 2.0)
A2.move("VD/HRD", "I", "S1/H,D2")
A2._assert("A2-2224       N    18", 2.5)
endturn()

startturn()
A1.move("LVL", "I", "H,H")
A1._assert("A2-2022       N    18", 2.0)
A2.move("LVL", "I", "H,H,H")
asserterror("flight type immediately after VD cannot be LVL.")

startturn()
A1.move("LVL", "I", "H,H")
A1._assert("A2-2022       N    18", 2.0)
A2.move("SD", "I", "H,D,D")
A2._assert("A2-2223       N    16", 2.5)
endturn()

endfile(__file__)