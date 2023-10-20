from apengine.tests.infrastructure import *
startfile(__file__, "NRM aircraft")

# Rolls and NRM aircraft

starttestsetup()
A1 = aircraft("A1", "B-26B", 2015, "N", 24, 3.0, "CL")
endtestsetup()

startturn()
A1.move("VD/HRD",  "FT", "H,D2,D2,D2")
asserterror("aircraft cannot perform rolling maneuvers.")
A1.move("SD",  "FT", "H,H,D")
A1._assert("2013       N    23",  3.0)
endturn()

startturn()
A1.move("VD",  "FT", "H,D3,D3/VRL/L")
asserterror("aircraft cannot perform rolling maneuvers.")
A1.move("VD",  "FT", "H,D3,D3")
A1._assert("2012       N    17",  4.5)
endturn()


endfile(__file__)