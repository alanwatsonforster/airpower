from apassistant._tests.infrastructure import *
startfile(__file__, "lag rolls")


# Lag Rolls

# Check the position after lag rolls.

starttestsetup(sheets=[["A1"]], verbose=False)
A1 = aircraft("A1", "F-80C", "1708", "E", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "E", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1808       ESE  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2409       ENE  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "ENE", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "ENE", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1807       E    10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2508       NNE  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "NNE", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "NNE", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1707       ENE  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2408       N    10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "N", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "N", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1607       NNE  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2407       NNW  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "NNW", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "NNW", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1608       N    10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2307       WNW  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "WNW", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "WNW", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1508       NNW  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2207       W    10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "W", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "W", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1609       WNW  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2208       WSW  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "WSW", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "WSW", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1610       W    10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2108       SSW  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "SSW", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "SSW", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1709       WSW  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2209       S    10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "S", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "S", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1810       SSW  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2210       SSE  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "SSE", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "SSE", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1809       S    10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2309       ESE  10",  2.0)
endturn()

starttestsetup(sheets=[["A1"]])
A1 = aircraft("A1", "F-80C", "1708", "ESE", 10, 2.0, "CL")
A2 = aircraft("A2", "F-80C", "2308", "ESE", 10, 2.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL")
A1._assert("1908       SSE  10",  2.0)
A2.move("LVL",  "M", "LRR/H,HR")
A2._assert("2410       E    10",  2.0)
endturn()

# Check we can carry preparatory HFPs from one turn to the next.

starttestsetup(verbose=False)
A1 = aircraft("A1", "F-104A", "1715", "N", 10, 7.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  0.5, "H,H,H,H,H,H,LRL/H")
A1._assert("1708       N    10",  7.0)
endturn()

startturn()
A1.move("LVL",  0.5 , "HL,H,H,H,H,H,H"  )
A1._assert("1903       NNE  10",  7.0)
endturn()

# Check VFPs and unloaded HFPs are not counted as preparatory HFPs.

starttestsetup(verbose=False)
A1 = aircraft("A1", "F-104A", "1715", "N", 10, 7.0, "CL")
endtestsetup()
startturn()
A1.move("UD" ,  "AB", "H,LRL/HD,HL,H,H,H,H"   )
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("UD" ,  "AB", "H,LRL/HD,HDL,H,H,H,H"  )
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("UD" ,  "AB", "H,LRL/H,HL,HD,HD,HD,HD")
A1._assert("1810       NNE   6",  8.0)
startturn()
A1.move("SD" ,  "AB", "H,LRL/D,D,HL,H,H,H,H"  )
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("SD" ,  "AB", "H,LRL/H,DL,H,H,H,H"    )
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("SD" ,  "AB", "H,LRL/H,HL,D,D,D,D"    )
A1._assert("1613       NNE   6",  8.0)
startturn()
A1.move("ZC" ,  "AB", "H,LRL/C,HL,H,H,H,H"    )
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("ZC" ,  "AB", "H,LRL/H,CL,H,H,H,H"    )
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("ZC" ,  "AB", "H,LRL/H,HL,C,C,C,C"    )
A1._assert("1613       NNE  14",  6.5)
endturn()

startturn()
A1.move("ZC" ,  "AB", "H,LRL/C,HL,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("LVL",  "M" , "H,H,H,H,H,H"     )
A1._assert("1908       NNE  14",  7.0)
endturn()

# Check the required preparatory HFPs, both at subsonic and supersonic speeds.

starttestsetup(verbose=False)
A1 = aircraft("A1", "F-104A", "1715", "N",  7, 7.0, "CL")
A2 = aircraft("A2", "F-104A", "1915", "N",  7, 7.5, "CL")
A3 = aircraft("A3", "F-104A", "2115", "N", 20, 6.5, "CL")
A4 = aircraft("A4", "F-104A", "2315", "N", 20, 7.0, "CL")
endtestsetup()
startturn()
A1.move("LVL",  "AB", "H,LRL/HL,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A2.move("LVL",  "AB", "H,LRL/H,HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A3.move("LVL",  "AB", "H,LRL/HL,H,H,H,H"  )
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A4.move("LVL",  "AB", "H,LRL/H,HL,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("LVL",  "AB", "H,LRL/H,HL,H,H,H,H")
A1._assert("1810       NNE   7",  7.5)
startturn()
A2.move("LVL",  "AB", "H,LRL/H,H,HL,H,H,H")
A2._assert("1909/2010  NNE   7",  7.5)
startturn()
A3.move("LVL",  "AB", "H,LRL/H,HL,H,H,H"  )
A3._assert("2110/2211  NNE  20",  7.0)
startturn()
A4.move("LVL",  "AB", "H,LRL/H,H,HL,H,H,H")
A4._assert("2309/2410  NNE  20",  7.0)
endturn()

# Check additional preparatory HFPs required at altitude.

starttestsetup(verbose=False)
A1 = aircraft("A1", "F-104A", "1515", "N", 20, 12.0, "CL")
A2 = aircraft("A2", "F-104A", "1715", "N", 30, 12.0, "CL")
A3 = aircraft("A3", "F-104A", "1915", "N", 40, 12.0, "CL")
A4 = aircraft("A4", "F-104A", "2115", "N", 50, 12.0, "CL")
A5 = aircraft("A5", "F-104A", "2315", "N", 61, 12.0, "CL")

endtestsetup()
startturn()
A1.move("LVL",  "AB", "H,LRL/H,HL,H,H,H,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A1.move("LVL",  "AB", "H,LRL/H,H,HL,H,H,H,H,H,H,H,H")
A1._assert("1806       NNE  20",  12.0)
startturn()
A2.move("LVL",  "AB", "H,LRL/H,H,HL,H,H,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A2.move("LVL",  "AB", "H,LRL/H,H,H,HL,H,H,H,H,H,H,H")
A2._assert("1905/2006  NNE  30",  12.0)
startturn()
A3.move("LVL",  "AB", "H,LRL/H,H,H,HL,H,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A3.move("LVL",  "AB", "H,LRL/H,H,H,H,HL,H,H,H,H,H,H")
A3._assert("2105       NNE  40",  12.0)
startturn()
A4.move("LVL",  "AB", "H,LRL/H,H,H,H,HL,H,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A4.move("LVL",  "AB", "H,LRL/H,H,H,H,H,HL,H,H,H,H,H")
A4._assert("2205/2305  NNE  50",  12.0)
startturn()
A5.move("LVL",  "AB", "H,LRL/H,H,H,H,H,HL,H,H,H,H,H")
asserterror("attempt to roll without sufficient preparatory HFPs.")
startturn()
A5.move("LVL",  "AB", "H,LRL/H,H,H,H,H,H,HL,H,H,H,H")
A5._assert("2405       NNE  61",  12.0)
endturn()


# Check allowed flight types.

starttestsetup()
A1 = aircraft("A1", "F-80C", "1415", "N", 20, 4.0, "CL")
A2 = aircraft("A2", "F-80C", "1615", "N", 20, 4.0, "CL")
endtestsetup()

startturn()
A1.move("SC", "M", "LRL/H,H,H,H")
asserterror("attempt to declare a lag roll while flight type is SC.")
startturn()
A2.move("SC", "M", "LRR/H,H,H,H")
asserterror("attempt to declare a lag roll while flight type is SC.")
startturn()
A1.move("SC", "M", "H,H,H,C")
A2.move("SC", "M", "H,H,H,C")
endturn()

startturn()
A1.move("VC", "M", "LRL/H,C2,C2,C2")
asserterror("attempt to declare a lag roll while flight type is VC.")
startturn()
A2.move("VC", "M", "LRR/H,C2,C2,C2")
asserterror("attempt to declare a lag roll while flight type is VC.")
startturn()
A1.move("SD", "M", "H,H,H,D")
A2.move("SD", "M", "H,H,H,D")
endturn()

startturn()
A1.move("VD", "M", "LRL/H,H,D2,D2,D2")
asserterror("attempt to declare a lag roll while flight type is VD.")
startturn()
A2.move("VD", "M", "LRR/H,H,D2,D2,D2")
asserterror("attempt to declare a lag roll while flight type is VD.")
startturn()
A1.move("SD", "M", "H,H,H,H")
A2.move("SD", "M", "H,H,H,H")
endturn()


# TODO: Check multiple rolls in one turn.

# The issue is the F-104A is GSSM.

#checkstarttestsetup(verbose=True)
#A1 = aircraft("A1", "F-104A", "1715", "N", 20, 12.0, "CL")
#checkendtestsetup()
#checkstartturn()
#A1.move("LVL",  "AB", "LRL/H,H,HL,LRR/H,H,HR,LRL/H,H,HL,LRR/H,H,HR")
#A1._assert("1906       N    20",  11.5)
#A1.move("LVL",  "AB", "LRL/H,H,HL,H,H,H,H,H,H,LRR/H,H,HR"          )
#A1._assert("2106       N    20",  12.0)
#A1.move("ZC" ,  "AB", "LRL/H,H,HL,H,C,C,C,C,H,LRR/H,H,HR"          )
#A1._assert("1909       N    24",  11.5)
#A1.move("SD" ,  "AB", "LRL/H,H,HL,H,D,D,D,D,H,LRR/H,H,HR"          )
#A1._assert("1909       N    16",  10.5)
#checkendturn()

# Check we can select the bank after a DR.

starttestsetup(verbose=False)
A1 = aircraft("A1", "F-80C", "1715", "N", 20, 4.0, "CL")

endtestsetup()
startturn()
A1.move("LVL",  "M", "LRL/H,HL/BKL,EZR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
startturn()
A1.move("LVL",  "M", "LRL/H,HL/WL,EZR/H,H" )
A1._assert("1712       NNE  20",  4.0)
startturn()
A1.move("LVL",  "M", "LRL/H,HL/BKR,EZR/H,H")
A1._assert("1712       NNE  20",  4.0)
startturn()
A1.move("LVL",  "M", "LRR/H,HR/BKL,EZR/H,H")
asserterror("attempt to declare a turn to R while banked to L.")
startturn()
A1.move("LVL",  "M", "LRR/H,HR/WL,EZR/H,H" )
A1._assert("1712       NNW  20",  4.0)
startturn()
A1.move("LVL",  "M", "LRR/H,HR/BKR,EZR/H,H")
A1._assert("1712       NNW  20",  4.0)
startturn()
A1.move("LVL",  "M", "LRL/H,HL/BKR,EZL/H,H")
asserterror("attempt to declare a turn to L while banked to R.")
startturn()
A1.move("LVL",  "M", "LRL/H,HL/WL,EZL/H,H" )
A1._assert("1712       NNE  20",  4.0)
startturn()
A1.move("LVL",  "M", "LRL/H,HL/BKL,EZL/H,H")
A1._assert("1712       NNE  20",  4.0)
startturn()
A1.move("LVL",  "M", "LRR/H,HR/BKR,EZL/H,H")
asserterror("attempt to declare a turn to L while banked to R.")
startturn()
A1.move("LVL",  "M", "LRR/H,HR/WL,EZL/H,H" )
A1._assert("1712       NNW  20",  4.0)
startturn()
A1.move("LVL",  "M", "LRR/H,HR/BKL,EZL/H,H")
A1._assert("1712       NNW  20",  4.0)
endturn()

# Rolls and GSSM/PSSM aircraft

# F-104A is GSSM, F-102A is PSSM, and F-100A is neither.

starttestsetup(verbose=False)
A1 = aircraft("A1", "F-104A", "1215", "N", 20, 7.5, "CL") # GSSM
A2 = aircraft("A2", "F-100A", "1415", "N", 20, 7.5, "CL")
A3 = aircraft("A3", "F-102A", "1615", "N", 20, 7.5, "CL") # PSSM
endtestsetup()

startturn()

A1.move("LVL",  "AB", "H,H,H,H,H,H,H" )
A1._assert("1208       N    20",  8.0)
A2.move("LVL",  "AB", "H,H,H,H,H,H,H" )
A2._assert("1408       N    20",  7.5)
A3.move("LVL",  "AB", "H,H,H,H,H,H,H" )
A3._assert("1608       N    20",  7.5)

startturn()

A1.move("LVL",  "AB", "LRR/H,H,HR,LRL/H,H,HL,H" )
A1._assert("1109       N    20",  7.5)
A2.move("LVL",  "AB", "LRR/H,H,HR,LRL/H,H,HL,H" )
A2._assert("1309       N    20",  7.0)
A3.move("LVL",  "AB", "LRR/H,H,HR,LRL/H,H,HL,H" )
A3._assert("1509       N    20",  6.5)

endturn()



endfile(__file__)