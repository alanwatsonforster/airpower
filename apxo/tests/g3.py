from apxo.tests.infrastructure import *
startfile(__file__, "vertical rolls")

# Vertical Rolls

# Check we can only perform a VR on a VFP in a VD or VD.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-80C", "A1-2013", "N", 40, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2213", "N", 40, 4.0, "CL")
A3 = aircraft("A3", "AF", "F-80C", "A1-2413", "N", 10, 5.0, "CL")
endtestsetup()

startturn()
A1.move("LVL",  "N", "H,H,H,H"  )
A1._assert("A1-2009       N    40",  4.0)
A2.move("SD" ,  "N", "H,H,H,D"  )
A2._assert("A1-2210       N    39",  4.0)
A3.move("ZC" ,  "M", "H,H,H,H,C")
A3._assert("A1-2409       N    11",  5.0)
endturn()

startturn()
A1.move("ZC" ,  "M", "H,C,C,VRR/C/R"   )
asserterror("attempt to declare a vertical roll while flight type is ZC.")
startturn()
A1.move("SC" ,  "M", "H,C,C,VRR/C/R"   )
asserterror("attempt to declare a vertical roll while flight type is SC.")
startturn()
A1.move("LVL",  "M", "H,H,H,VRR/H/R"   )
asserterror("attempt to declare a vertical roll while flight type is LVL.")
startturn()
A1.move("SD" ,  "M", "H,D,D,VRR/D/R"   )
asserterror("attempt to declare a vertical roll while flight type is SD.")
startturn()
A1.move("UD" ,  "M", "H,HU,HU,HU/VRR"  )
asserterror("attempt to declare a vertical roll while flight type is UD.")
startturn()
startturn()
A1.move("LVL",  "M", "H,H,H,H"         )
A1._assert("A1-2005       N    40",  4.0)
startturn()
A2.move("VD" ,  "M", "H/VRR,D2,D2,D2"  )
asserterror("attempt to declare a vertical roll during an HFP.")
startturn()
A2.move("VD" ,  "M", "H,VRR/D2/R,D2,D2")
A2._assert("A1-2209       NNE  33",  5.5)
startturn()
A2.move("VD" ,  "M", "H,D2,VRR/D2/R,D2")
A2._assert("A1-2209       NNE  33",  5.5)
startturn()
A2.move("VD" ,  "M", "H,D2,D2,VRR/D2/R")
A2._assert("A1-2209       NNE  33",  5.5)
startturn()
A3.move("VC" ,  "M", "H/VRR/R,H,C,C,C" )
asserterror("attempt to declare a vertical roll during an HFP.")
startturn()
A3.move("VC" ,  "M", "H,H/VRR/R,C,C,C" )
asserterror("attempt to declare a vertical roll during an HFP.")
startturn()
A3.move("VC" ,  "M", "H,H,C/VRR/R,C,C" )
A3._assert("A1-2407       NNE  14",  4.0)
startturn()
A3.move("VC" ,  "M", "H,H,C,C/VRR/R,C" )
A3._assert("A1-2407       NNE  14",  4.0)
startturn()
A3.move("VC" ,  "M", "H,H,C,C,C/VRR/R" )
A3._assert("A1-2407       NNE  14",  4.0)

endturn()

# Check VRs with multiple facing changes.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-80C", "A1-2213", "N", 40, 4.0, "CL")
A2 = aircraft("A2", "AF", "F-80C", "A1-2413", "N", 10, 5.0, "CL")
endtestsetup()

startturn()
A1.move("SD" ,  "N", "H,H,H,D"  )
A1._assert("A1-2210       N    39",  4.0)
A2.move("ZC" ,  "M", "H,H,H,H,C")
A2._assert("A1-2409       N    11",  5.0)
endturn()

startturn()

A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R30" )
A1._assert("A1-2209       NNE  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRR/R30"  )
A2._assert("A1-2407       NNE  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R60" )
A1._assert("A1-2209       ENE  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRR/R60"  )
A2._assert("A1-2407       ENE  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R90" )
A1._assert("A1-2209       E    33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRR/R90"  )
A2._assert("A1-2407       E    14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R120")
A1._assert("A1-2209       ESE  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRR/R120" )
A2._assert("A1-2407       ESE  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R150")
A1._assert("A1-2209       SSE  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRR/R150" )
A2._assert("A1-2407       SSE  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R180")
A1._assert("A1-2209       S    33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRR/R180" )
A2._assert("A1-2407       S    14",  4.0)

startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L30" )
A1._assert("A1-2209       NNW  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRL/L30"  )
A2._assert("A1-2407       NNW  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L60" )
A1._assert("A1-2209       WNW  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRL/L60"  )
A2._assert("A1-2407       WNW  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L90" )
A1._assert("A1-2209       W    33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRL/L90"  )
A2._assert("A1-2407       W    14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L120")
A1._assert("A1-2209       WSW  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRL/L120" )
A2._assert("A1-2407       WSW  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L150")
A1._assert("A1-2209       SSW  33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRL/L150" )
A2._assert("A1-2407       SSW  14",  4.0)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L180")
A1._assert("A1-2209       S    33",  5.5)
startturn()
A2.move("VC" ,  "M", "H,H,C,C,C/VRL/L180" )
A2._assert("A1-2407       S    14",  4.0)
endturn()

# Check VR with shifts off a side.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-80C", "A1-2213", "NNW", 40, 4.0, "CL")
endtestsetup()

startturn()
A1.move("SD" ,  "N", "H,H,H,D"  )
A1._assert("A1-2011/2110  NNW  39",  4.0)
endturn()

startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R30"  )
A1._assert("A1-2010       N    33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R60"  )
A1._assert("A1-2010       NNE  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R90"  )
A1._assert("A1-2010       ENE  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R120" )
A1._assert("A1-2010       E    33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R150" )
A1._assert("A1-2010       ESE  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/RS180")
A1._assert("A1-2010       SSE  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRR/R180" )
A1._assert("A1-2010       SSE  33",  5.5)

startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L30"  )
A1._assert("A1-2010       WNW  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L60"  )
A1._assert("A1-2010       W    33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L90"  )
A1._assert("A1-2010       WSW  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L120" )
A1._assert("A1-2010       SSW  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L150" )
A1._assert("A1-2010       S    33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/LS180")
A1._assert("A1-2010       SSE  33",  5.5)
startturn()
A1.move("VD" ,  "M", "H,D2,D2,D2/VRL/L180" )
A1._assert("A1-2010       SSE  33",  5.5)
endturn()

# Check multiple VRs in the same turn and the extra drag these incur.

starttestsetup()
A1 = aircraft("A1", "AF", "F-80C", "A1-2018", "N", 41, 4.0, "CL")
endtestsetup()

startturn()
A1.move("SD",  "N", "H,H,H,D")
A1._assert("A1-2015       N    40",  4.0)
endturn()

startturn()

A1.move("VD",  "M", "H,D2,D2,D2"                           )
A1._assert("A1-2014       N    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2/VRL/L180,D2,D2"                  )
A1._assert("A1-2014       S    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2/VRL/L180,D2/VRL/L180,D2"         )
A1._assert("A1-2014       N    34",  5.0)
startturn()
A1.move("VD",  "M", "H,D2/VRL/L180,D2/VRL/L180,D2/VRL/L180")
A1._assert("A1-2014       S    34",  4.5)

startturn()
A1.move("VD",  "M", "H,D2,D2,D2"                           )
A1._assert("A1-2014       N    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2/VRR/R180,D2,D2"                  )
A1._assert("A1-2014       S    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2/VRR/R180,D2/VRR/R180,D2"         )
A1._assert("A1-2014       N    34",  5.0)
startturn()
A1.move("VD",  "M", "H,D2/VRR/R180,D2/VRR/R180,D2/VRR/R180")
A1._assert("A1-2014       S    34",  4.5)

startturn()
A1.move("VD",  "M", "H,D2,D2,D2"                           )
A1._assert("A1-2014       N    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2/VRL/L180,D2,D2"                  )
A1._assert("A1-2014       S    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2/VRR/R180,D2/VRL/L180,D2"         )
A1._assert("A1-2014       N    34",  5.0)
startturn()
A1.move("VD",  "M", "H,D2/VRL/L180,D2/VRR/R180,D2/VRL/L180")
A1._assert("A1-2014       S    34",  4.5)

endturn()

# Check VRs with a LRR aircraft.

starttestsetup()
A1 = aircraft("A1", "AF", "Meteor F.8", "A1-2018", "N", 41, 4.0, "CL")
endtestsetup()

startturn()
A1.move("SD",  "N", "H,H,H,D")
A1._assert("A1-2015       N    40",  4.0)
endturn()

startturn()

A1.move("VD",  "M", "H,D2,D2,D2/VRL/L120")
asserterror("attempt to roll vertically by more than 90 degrees in LRR aircraft.")
startturn()
A1.move("VD",  "M", "H,D2,D2,D2/VRL/L90" )
A1._assert("A1-2014       W    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2,D2,D2/VRL/L60" )
A1._assert("A1-2014       WNW  34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2,D2,D2/VRL/L30" )
A1._assert("A1-2014       NNW  34",  5.5)

startturn()
A1.move("VD",  "M", "H,D2,D2,D2/VRR/R120")
asserterror("attempt to roll vertically by more than 90 degrees in LRR aircraft.")
startturn()
A1.move("VD",  "M", "H,D2,D2,D2/VRR/R90" )
A1._assert("A1-2014       E    34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2,D2,D2/VRR/R60" )
A1._assert("A1-2014       ENE  34",  5.5)
startturn()
A1.move("VD",  "M", "H,D2,D2,D2/VRR/R30" )
A1._assert("A1-2014       NNE  34",  5.5)

endturn()

# Check the extra drag of VRs at SS speed.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "F-100A", "A1-2029", "N", 1, 8.0, "CL")
endtestsetup()

startturn()
A1.move("SC",  "AB", "H,H,H,H,H,H,H,C")
A1._assert("A2-2022       N     2",  7.5)
endturn()

startturn()
A1.move("VC",  "AB", "H,H,C2,C2,C2,C2,C2"                        )
A1._assert("A2-2020       N    12",  3.0)
startturn()
A1.move("VC",  "AB", "H,H,C2/VRR/R,C2/VRL/L,C2/VRR/R,C2/VRL/L,C2/VRR/R")
A1._assert("A2-2020       NNE  12",  1.0)
endturn()

# Check VRs with aircraft with the OVR property ("one vertical roll"), such as 
# the B-66B. These can perform only one vertical roll per game turn.

starttestsetup(verbose=False)
A1 = aircraft("A1", "AF", "B-66B", "A1-2030", "N", 30, 5.0, "CL")
endtestsetup()

startturn()
A1.move("VD/HRD",  "M", "H,H,D2,D2,D2/VRL/L180")
A1._assert("A2-2028       S    24",  6.5)
endturn()

startturn()
A1.move("VD"    ,  "M", "D2,D2,D2,D2,D2,D2/VRL/L180"         )
A1._assert("A2-2028       N    12",  6.5)
startturn()
A1.move("VD"    ,  "M", "D2/VRL/L180,D2,D2,D2,D2,D2"         )
A1._assert("A2-2028       N    12",  6.5)
startturn()
A1.move("VD"    ,  "M", "D2/VRL/L180,D2/VRL/L180,D2,D2,D2,D2")
asserterror("aircraft can only perform one vertical roll per turn.")
startturn()
A1.move("VD"    ,  "M", "D2,D2,D2,D2,D2,D2"                  )
A1._assert("A2-2028       S    12",  6.5)
endturn()

# Supersonic speed.

starttestsetup()
A1 = aircraft("A1", "AF", "F-104A", "A1-1215", "N", 30, 7.5, "CL") # GSSM
A2 = aircraft("A2", "AF", "F-100A", "A1-1415", "N", 30, 7.5, "CL")
A3 = aircraft("A3", "AF", "F-102A", "A1-1615", "N", 30, 7.5, "CL") # PSSM
endtestsetup()

startturn()
A1.move("VD/HRD",  "AB", "H,H,D3,D3,D2,D2,VRR/D2/R180" )
A1._assert("A1-1213       S    18",  10.0)
A2.move("VD/HRD",  "AB", "H,H,D3,D3,D2,D2,VRR/D2/R180" )
A2._assert("A1-1413       S    18",   9.0)
A3.move("VD/HRD",  "AB", "H,H,D3,D2,D2,D2,VRR/D2/R180" )
A3._assert("A1-1613       S    19",   9.0)
endturn()

endfile(__file__)