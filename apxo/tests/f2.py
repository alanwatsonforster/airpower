from apxo.tests.infrastructure import *

startfile(__file__, "special flight")

from apxo.tests.infrastructure import *

starttestsetup()
A1 = aircraft("A1", "AF", "O-1E", "A2-2030", "N", 5, 0, "CL", color="green")
A2 = aircraft("A2", "AF", "O-2A", "A2-2230", "N", 5, 0, "CL", color="green")
A3 = aircraft("A3", "AF", "HH-53C", "A2-2430", "N", 5, 0, "CL", color="green")
endtestsetup()

startgameturn()
A1.move("SP", 1, "H")
A1._assert("A2-2029       N     5", 1)

startgameturn()
A1.move("SP", 1, "HR")
A1._assert("A2-2029       NNE   5", 1)
startgameturn()
A1.move("SP", 1, "HL")
A1._assert("A2-2029       NNW   5", 1)
startgameturn()
A1.move("SP", 1, "HRR")
A1._assert("A2-2029       ENE   5", 1)
startgameturn()
A1.move("SP", 1, "HLL")
A1._assert("A2-2029       WNW   5", 1)

startgameturn()
A1.move("SP", 2, "SR,H")
A1._assert("A2-2029/2129  NNE   5", 2)
startgameturn()
A1.move("SP", 2, "SL,H")
A1._assert("A2-1929/2029  NNW   5", 2)
startgameturn()
A1.move("SP", 2, "SRR,H")
A1._assert("A2-2129       ENE   5", 2)
startgameturn()
A1.move("SP", 2, "SLL,H")
A1._assert("A2-1929       WNW   5", 2)

startgameturn()
A1.move("SP", 1, "SRR")
A1._assert("A2-2030       ENE   5", 1)
startgameturn()
A1.move("SP", 1, "SRRR")
A1._assert("A2-2030       E     5", 1)
startgameturn()
A1.move("SP", 1, "SR120")
A1._assert("A2-2030       ESE   5", 1)
startgameturn()
A1.move("SP", 1, "SLL")
A1._assert("A2-2030       WNW   5", 1)
startgameturn()
A1.move("SP", 1, "SLLL")
A1._assert("A2-2030       W     5", 1)
startgameturn()
A1.move("SP", 1, "SL120")
A1._assert("A2-2030       WSW   5", 1)

startgameturn()
A1.move("SP", 2, "H,D")
A1._assert("A2-2029       N     4", 2)

startgameturn()
A1.move("SP", 2, "HR,D")
A1._assert("A2-2029       NNE   4", 2)
startgameturn()
A1.move("SP", 2, "HL,D")
A1._assert("A2-2029       NNW   4", 2)
startgameturn()
A1.move("SP", 2, "HRR,D")
A1._assert("A2-2029       ENE   4", 2)
startgameturn()
A1.move("SP", 2, "HLL,D")
A1._assert("A2-2029       WNW   4", 2)

startgameturn()
A1.move("SP", 3, "SR,H,D")
A1._assert("A2-2029/2129  NNE   4", 3)
startgameturn()
A1.move("SP", 3, "SL,H,D")
A1._assert("A2-1929/2029  NNW   4", 3)
startgameturn()
A1.move("SP", 3, "SRR,H,D")
A1._assert("A2-2129       ENE   4", 3)
startgameturn()
A1.move("SP", 3, "SLL,H,D")
A1._assert("A2-1929       WNW   4", 3)

startgameturn()
A1.move("SP", 2, "SRR,D")
A1._assert("A2-2030       ENE   4", 2)
startgameturn()
A1.move("SP", 2, "SRRR,D")
A1._assert("A2-2030       E     4", 2)
startgameturn()
A1.move("SP", 2, "SR120,D")
A1._assert("A2-2030       ESE   4", 2)
startgameturn()
A1.move("SP", 2, "SLL,D")
A1._assert("A2-2030       WNW   4", 2)
startgameturn()
A1.move("SP", 2, "SLLL,D")
A1._assert("A2-2030       W     4", 2)
startgameturn()
A1.move("SP", 2, "SL120,D")
A1._assert("A2-2030       WSW   4", 2)

startgameturn()
A3.move("SP", 1, "SR30")
A3._assert("A2-2430       NNE   5", 1)
startgameturn()
A3.move("SP", 1, "SR60")
A3._assert("A2-2430       ENE   5", 1)
startgameturn()
A3.move("SP", 1, "SR90")
A3._assert("A2-2430       E     5", 1)
startgameturn()
A3.move("SP", 1, "SR120")
A3._assert("A2-2430       ESE   5", 1)
startgameturn()
A3.move("SP", 1, "SR150")
A3._assert("A2-2430       SSE   5", 1)
startgameturn()
A3.move("SP", 1, "SR180")
A3._assert("A2-2430       S     5", 1)

startgameturn()
A3.move("SP", 1, "SL30")
A3._assert("A2-2430       NNW   5", 1)
startgameturn()
A3.move("SP", 1, "SL60")
A3._assert("A2-2430       WNW   5", 1)
startgameturn()
A3.move("SP", 1, "SL90")
A3._assert("A2-2430       W     5", 1)
startgameturn()
A3.move("SP", 1, "SL120")
A3._assert("A2-2430       WSW   5", 1)
startgameturn()
A3.move("SP", 1, "SL150")
A3._assert("A2-2430       SSW   5", 1)
startgameturn()
A3.move("SP", 1, "SL180")
A3._assert("A2-2430       S     5", 1)

startgameturn()
A1.move("SP", 2, "H,C")
A1._assert("A2-2029       N     5", 2)
A2.move("SP", 3, "H,H,C")
A2._assert("A2-2228       N     5", 3)
A3.move("SP", 2, "H,C")
A3._assert("A2-2429       N     5", 2)

endgameturn()

startgameturn()
A1.move("SP", 2, "H,C")
A1._assert("A2-2028       N     5", 2)
A2.move("SP", 3, "H,H,C")
A2._assert("A2-2226       N     6", 3)
A3.move("SP", 3, "H,H,C")
A3._assert("A2-2427       N     5", 3)
endgameturn()

startgameturn()
A1.move("SP", 2, "H,C")
A1._assert("A2-2027       N     5", 2)
A2.move("SP", 3, "H,H,C")
A2._assert("A2-2224       N     6", 3)
A3.move("SP", 2, "H,C")
A3._assert("A2-2426       N     5", 2)
endgameturn()

startgameturn()
A1.move("SP", 2, "H,C")
A1._assert("A2-2026       N     6", 2)
A2.move("SP", 3, "H,H,C")
A2._assert("A2-2222       N     7", 3)
A3.move("SP", 3, "H,H,C")
A3._assert("A2-2424       N     6", 3)
endgameturn()

startgameturn()
A1.move("SP", 2, "H")
A1.continuemove("H")
A1._assert("A2-2024       N     6", 2)
A2.move("SP", 3, "H")
A2.continuemove("H,H")
A2._assert("A2-2219       N     7", 3)
A3.move("SP", 3, "H,H")
A3.continuemove("H")
A3._assert("A2-2421       N     6", 3)
endgameturn()

endfile(__file__)
