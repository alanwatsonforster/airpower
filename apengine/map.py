"""
The map.
"""

import apengine.azimuth as apazimuth
import apengine.draw    as apdraw
import apengine.hex     as aphex
import apengine.hexcode as aphexcode
import apengine.log     as aplog

import math
import numpy as np

_sheetgrid = []
_sheetlist = []
_nxsheetgrid = 0
_nysheetgrid = 0
_compassrose = None

_dxsheet = 20
_dysheet = 15

_saved = False

level0color = ( 0.850, 0.900, 0.850 )
level1color = ( 0.824, 0.752, 0.640 )
level2color = ( 0.616, 0.664, 0.560 )
ridgecolor  = ( 0.600, 0.500, 0.450 )
woodedcolor = ( 0.300, 0.500, 0.300 )
urbancolor  = ( 0.600, 0.600, 0.600 )
roadcolor   = urbancolor
bridgecolor = urbancolor
watercolor  = ( 0.650, 0.820, 1.000 )
hexcolor    = ( 0.400, 0.400, 0.400 )
runwaycolor = urbancolor
damcolor    = urbancolor

roadwidth        = 3
riverwidth       = 10
wideriverwidth   = 20
clearingwidth    = 14
bridgeouterwidth = 14
bridgeinnerwidth = 7
runwaywidth      = 7
damwidth         = 14

border = 0.75
bordercolor = (1.00, 1.00, 1.00)

def setmap(sheetgrid, compassrose):

  """
  Set the arrangement of the sheets that form the map and the position of the 
  compass rose.
  """

  global _sheetgrid
  global _sheetlist
  global _nysheetgrid
  global _nxsheetgrid
  global _compassrose

  # The sheet grid argument follows visual layout, so we need to flip it 
  # vertically so that the lower-left sheet has indices (0,0).

  # TODO: Validate arguments. For example, that sheet grid is not ["A1"].

  _sheetgrid = list(reversed(sheetgrid))
  _nysheetgrid = len(_sheetgrid)
  _nxsheetgrid = len(_sheetgrid[0])

  aplog.log("sheet layout is:")
  aplog.logbreak()
  for iy in range (0, _nysheetgrid):
     aplog.log("  %s" % " ".join(sheetgrid[iy]))

  _sheetlist = []
  for iy in range (0, _nysheetgrid):
    for ix in range (0, _nxsheetgrid):
      if _sheetgrid[iy][ix] != "--":
        _sheetlist.append(_sheetgrid[iy][ix])

  _compassrose = compassrose

  global _saved
  _saved = False

def startdrawmap():

  """
  Draw the map.
  """

  def toxy(sheet, x, y):
    XX = int(x)
    YY = int(y)
    dx = x - XX
    dy = y - YY
    x0, y0 = aphexcode.toxy(XX * 100 + YY, sheet=sheet)
    return x0 + dx, y0 - dy

  #global _saved
  #if _saved:
  #  apdraw.restore()
  #  return

  apdraw.setcanvas(_nxsheetgrid * _dxsheet, _nysheetgrid * _dysheet)

  # Draw the sheets and level 0.
  for sheet in sheets():
    xmin, ymin, xmax, ymax = sheetlimits(sheet)
    apdraw.drawrectangle(xmin, ymin, xmax, ymax, linecolor=None, fillcolor=level0color, zorder=0)

  # Draw level 1.
  for h in level1hexcodes:
    if aphexcode.tosheet(h) in sheets():
      apdraw.drawhex(*aphexcode.toxy(h), fillcolor=level1color, zorder=0)

  # Draw level 2.
  for h in level2hexcodes:
    if aphexcode.tosheet(h) in sheets():
      apdraw.drawhex(*aphexcode.toxy(h), fillcolor=level2color, zorder=0)

  # Draw the ridges.
  for ridge in ridges:
    sheet = ridge[0]
    if sheet in sheets():
      p = ridge[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=ridgecolor, linewidth=7, zorder=0)
  
  # Draw water.
  for h in waterhexcodes:
    if aphexcode.tosheet(h) in sheets():
      apdraw.drawhex(*aphexcode.toxy(h), fillcolor=watercolor, zorder=0)
      
  # Draw the wooded areas.
  for h in woodedhexcodes:
    if aphexcode.tosheet(h) in sheets():
      apdraw.drawhex(*aphexcode.toxy(h), linecolor=woodedcolor, hatch="oo", zorder=0)

  # Draw the road clearings.
  for clearing in clearings:
    sheet = clearing[0]
    if sheet in sheets():
      p = clearing[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=level0color, linewidth=clearingwidth, zorder=0)

  # Draw the urban areas.
  for h in urbanhexcodes:
    if aphexcode.tosheet(h) in sheets():
      apdraw.drawhex(*aphexcode.toxy(h), linecolor=urbancolor, hatch="xx", zorder=0)

  # Draw the rivers.
  for river in rivers:
    sheet = river[0]
    if sheet in sheets():
      p = river[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=watercolor, linewidth=riverwidth, capstyle="butt", zorder=0)
  for river in widerivers:
    sheet = river[0]
    if sheet in sheets():
      p = river[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=watercolor, linewidth=wideriverwidth, capstyle="butt", zorder=0)

  # Draw the bridges.
  for bridge in bridges:
    sheet = bridge[0]
    if sheet in sheets():
      p = bridge[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=bridgecolor, linewidth=bridgeouterwidth, capstyle="butt", zorder=0)  
      apdraw.drawlines(x, y, color=level0color, linewidth=bridgeinnerwidth, capstyle="butt", zorder=0)  

  # Draw the roads.
  for road in roads:
    sheet = road[0]
    if sheet in sheets():
      p = road[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=roadcolor, linewidth=roadwidth, capstyle="butt", zorder=0)

  # Draw the runways.
  for runway in runways:
    sheet = runway[0]
    if sheet in sheets():
      p = runway[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=runwaycolor, linewidth=runwaywidth, capstyle="butt", zorder=0)
      
  # Draw the dams.
  for dam in dams:
    sheet = dam[0]
    if sheet in sheets():
      p = dam[1]
      xy = [toxy(sheet, *p) for p in p]
      x = [xy[0] for xy in xy]
      y = [xy[1] for xy in xy]
      apdraw.drawlines(x, y, color=damcolor, linewidth=damwidth, capstyle="butt", zorder=0)
    
  # Draw missing sheets.
  for iy in range (0, _nysheetgrid):
    for ix in range (0, _nxsheetgrid):
      if _sheetgrid[iy][ix] == "--":
        xmin = ix * _dxsheet
        xmax = xmin + _dxsheet
        ymin = iy * _dysheet
        ymax = ymin + _dysheet
        apdraw.drawrectangle(xmin, ymin, xmax, ymax, linecolor=None, fillcolor=bordercolor, zorder=0.0)

  # Draw the border.
  xmin = 0
  ymin = 0
  xmax = _nxsheetgrid * _dxsheet
  ymax = _nysheetgrid * _dysheet
  apdraw.drawrectangle(xmin-border, ymin-border, xmax+border, ymin, linecolor=None, fillcolor=bordercolor, zorder=0.0)
  apdraw.drawrectangle(xmin-border, ymax+border, xmax+border, ymax, linecolor=None, fillcolor=bordercolor, zorder=0.0)
  apdraw.drawrectangle(xmin-border, ymin-border, xmin, ymax+border, linecolor=None, fillcolor=bordercolor, zorder=0.0)
  apdraw.drawrectangle(xmax+border, ymin-border, xmax, ymax+border, linecolor=None, fillcolor=bordercolor, zorder=0.0)
  
  # Draw and label the hexes.
  for sheet in sheets():
    xmin, ymin, xmax, ymax = sheetlimits(sheet)
    for ix in range(0, _dxsheet + 1):
      for iy in range(0, _dysheet + 1):
        x = xmin + ix
        y = ymin + iy
        if ix % 2 == 1:
          y -= 0.5
        # Draw the hex if it is on the map and either its center or the center 
        # of its upper left edge are on this sheet.
        if isonmap(x, y) and (isonsheet(sheet, x, y) or isonsheet(sheet, x - 0.5, y + 0.25)):
          apdraw.drawhex(x, y, linecolor=hexcolor, zorder=0.5)
          apdraw.drawhexlabel(x, y, aphexcode.fromxy(x, y), color=hexcolor, zorder=0.5)

  # Label the sheets.
  for sheet in sheets():
    xmin, ymin, xmax, ymax = sheetlimits(sheet)
    apdraw.drawtext(xmin + 1.0, ymin + 1.5, 90, sheet, dy=-0.05, size=12, color=hexcolor, zorder=0.5)

  # Draw the compass rose.
  if _compassrose != None:
    apdraw.drawcompass(*aphexcode.toxy(_compassrose), apazimuth.tofacing("N"), color=hexcolor, zorder=0.5)

  # Draw the sheets outlines.
  for sheet in sheets():
    xmin, ymin, xmax, ymax = sheetlimits(sheet)
    apdraw.drawrectangle(xmin, ymin, xmax, ymax, linecolor=hexcolor, zorder=0.5)

  #apdraw.save()
  #_saved = True

def enddrawmap():
  apdraw.show()

def sheetorigin(sheet):

  """
  Returns the hex coordinates (x0, y0) of the lower left corner of the 
  specified sheet.
    
  The specified sheet must be in the map.
  """

  assert sheet in sheets()

  for iy in range (0, _nysheetgrid):
    for ix in range (0, _nxsheetgrid):
      if sheet == _sheetgrid[iy][ix]:
        x0 = ix * _dxsheet
        y0 = iy * _dysheet
        return x0, y0

def sheetlimits(sheet):

  """
  Returns the hex coordinates (xmin, ymin) and (xmax, ymax) the lower left
  and upper right corners of the specified sheet.
  """

  assert sheet in sheets()

  xmin, ymin = sheetorigin(sheet)

  xmax = xmin + _dxsheet
  ymax = ymin + _dysheet

  return xmin, ymin, xmax, ymax

def sheets():

  """
  Returns a list of the sheets in the map.
  """

  return _sheetlist

def isonsheet(sheet, x, y):

  """
  Returns True if the hex coordinate (x, y) is on the specified sheet, 
  excluding its edges. Otherwise returns false. The sheet must be in the map.
  """

  assert sheet in sheets()

  xmin, ymin, xmax, ymax = sheetlimits(sheet)

  return xmin < x and x < xmax and ymin < y and y < ymax

def isonmap(x, y):

  """
  Returns True if the hex coordinate (x, y) is on the map, excluding its edges. 
  Otherwise returns false.
  """

  if tosheet(x, y) != None:
    return True

  # The point is either off the map or on the edges between adjacent sheets
  # in the map. So, we check the upper left, upper right, lower left, and lower
  # right edges.

  if tosheet(x + 0.50, y + 0.25) == None:
    return False 
  if tosheet(x - 0.50, y + 0.25) == None:
    return False
  if tosheet(x + 0.50, y - 0.25) == None:
    return False
  if tosheet(x - 0.50, y - 0.25) == None:
    return False

  return True

def tosheet(x, y):

  """
  Returns the sheet containing the hex coordinates (x, y). If no sheet contains 
  the coordinates, returns None.
  """

  for sheet in sheets():
    if isonsheet(sheet, x, y):
      return sheet
  return None

################################################################################

level1hexcodes = [

  # B1
  3309, 
  3407, 3408, 3409,
  3506, 3507, 3508, 3509,
  3607, 3608, 3609,
  3707, 3708,

  # B2
  3123, 3124,
  3223, 3224, 3225,
  3322, 3323, 3324, 3325, 3326,
  3425, 3426,
  3525, 3526,
  3626,

  3723,
  3824,
  3923, 3924,
  4020, 4021, 4022, 4023, 4024, 4025, 
  4120, 4121, 4122, 4123, 4124,
  4220, 4221, 4222, 4223, 4224, 
  4318, 4319, 4322, 4323, 4324, 4327, 4328, 4329,
  4418, 4419, 4420, 4424, 4425, 4426, 4427, 4428, 4429,
  4518, 4519, 4520, 4526, 4527, 4528,
  4621, 4626, 4627, 4628,
  4721, 4723, 4724, 4725,
  4822, 4823,

  # C1

  5406, 5407,
  5505, 5506,
  5605, 5606, 5607,
  5704, 5705, 5706, 5707,
  5804, 5805, 5806, 5807, 5808,
  5904, 5905, 5906, 5907, 5908,
  6007, 6008, 6009,
  6107, 6108,

  5613, 5614,
  5711, 5712, 5713,
  5812, 5813,
  5911, 5912, 5913,
  6011, 6012, 6013, 6014,
  6111, 6112, 6113,
  6211, 6212, 6213,
  6310, 6311, 6312, 6313,
  6410, 6411, 6412, 6413,
  6509, 6510, 6511, 6512,
  6609, 6610, 6611, 6612,
  6709, 6710, 6711,
  6810, 6811, 6812,
  6910, 6911,

  # C2

  5217, 5218, 5219,
  5316, 5317, 5318, 5319,
  5417, 5418, 5419,
  5517, 5518,
  5617, 5618, 5619, 5620,
  5716, 5717, 5718, 5719, 5720,
  5817, 5818, 5819, 5820, 5821,
  5919, 5920, 5921,

  6025, 6026, 6027,
  6121, 6122, 6124, 6125, 6126, 6128,
  6220, 6221, 6222, 6223, 6224, 6225, 6226, 6228, 6229,
  6319, 6320, 6321, 6322, 6323, 6324, 6325, 6327, 6328, 6329,
  6420, 6421, 6422, 6423, 6424, 6425, 6427, 6428, 6429,
  6523, 6526,

]

level2hexcodes = [

  # B2
  4320, 4321,
  4421, 4422, 4423,
  4521, 4522, 4523, 4524, 4525,
  4622, 4623, 4624, 4625,
  4722

]

waterhexcodes = [

  # A2
  1219, 1319, 1420,

  # C2
  6127, 6227,

]

ridges = [
  ["B2",[[44.33,21.50],[45.00,22.00],[46.00,23.00],[46.00,24.00],[45.00,24.00],[45.00,27.00],[44.00,28.00],[43.33,28.50],]],
  ["C2",[[52.50,17.25],[54.00,18.00],[54.67,18.00],]],
  ["C2",[[55.33,17.50],[56.00,18.00],[57.00,18.00],[57.00,19.00],[58.50,20.25],]],
  ["C2",[[63.00,19.50],[63.00,24.00],[60.50,25.75],]],
]

woodedhexcodes = [
    
  # A1
  1111, 1112,
  1211, 1212, 1213, 1214, 1215,
  1310, 1311, 1312, 1313, 1314, 
  1411, 1412, 1413, 1414, 1415,
  1510, 1511, 1512, 1513, 1514, 
  1610, 1611, 1612, 1613, 1614, 1615,
  1710, 1711, 1712, 1713, 1714, 1715,
  1811, 1812, 1813, 1814, 1815,
  1910, 1911, 1912, 1913, 1914, 
  2009, 2010, 2011, 2012, 2013, 2014, 2015,
  2109, 2110, 2111, 2112, 2114, 2115,
  2211, 2212, 2214, 2215,
  2310, 2311, 2312, 2314,
  2411, 2412,

  # A2 has no woods.

  # B1

  3103, 3104, 3105, 3108, 3109,
  3202, 3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210,
  3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308,
  3402, 3407, 3408, 3409,
  3501, 3502, 3506, 3507, 3508,
  3602, 3603, 3604, 3605, 3607, 3608,
  3701, 3702, 3703, 3704,
  3802, 3803, 3804, 3805, 3806,
  3901, 3902, 3903, 3904, 3905, 3906, 3907,
  4003, 4004, 4005, 4006, 4007,
  4102, 4103, 4104, 4105,
  4203, 4204, 4205,

  3213,
  3312,
  3411, 3412,

  4606, 4607, 4608,
  4703, 4704, 4706, 4707,
  4803, 4804, 4805, 4806, 4807,
  4902, 4903, 4904, 4905,

  # B2

  3219, 3220,
  3319,

  3123, 3124,
  3223, 3224, 3225,
  3322, 3323, 3324, 3325, 3326,
  3422, 3425, 3426,
  3519, 3521, 3525, 3526,
  3619, 3620, 3621, 3622, 3623, 3624, 3626, 3628, 3629,
  3717, 3718, 3719, 3722, 3723, 3724, 3727, 3728,
  3817, 3818, 3819, 3824, 3825, 3826, 3827, 3828,
  3917, 3918, 3919, 3923, 3924, 3925, 3926, 3927, 3928,
  4018, 4019, 4020, 4021, 4022, 4023, 4024, 4025, 4026, 4027, 4028, 4029,
  4118, 4119, 4122, 4123, 4124, 4125, 4126, 4127,
  4223, 4224, 4225, 4226,


  4418, 4419, 4420,
  4517, 4518, 4519, 4520,
  4617, 4618, 4619, 4620, 4621,

  4820,
  4919, 4920,

  # C1

  6502, 6503,
  6602, 6603, 6605, 6608,
  6701, 6702, 6703, 6704, 6705, 6706, 6707, 6708,
  6802, 6803, 6804, 6805, 6806, 6807, 6808, 6809,
  6903, 6904, 6905, 6906, 6907, 6908, 6909,

  6611, 6612, 6613, 6614, 
  6710, 6711, 6712, 6713, 6714,
  6811, 6813, 6814, 6815,
  6913, 6914, 6915,

  # C2

  5221, 5222,
  5320, 5321,
  5420, 5421, 5422,
  5520, 5521,
  5621, 5622, 5623,
  5721, 5722, 5723,
  5822, 5823, 5824,

]

urbanhexcodes = [
    
  # A1

  1402, 1403,

  1602, 1604, 1605,
  1701, 1702, 1703, 1704, 1705,
  1802,
  1901, 1902, 1903,

  2113,

  2407,

  2603,
  2701, 2702,

  2615,
  2714, 2715,

  2911,

  # A2

  1121, 1125,
  1220, 1221, 1222, 1224, 1225, 1226,
  1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328,
  1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430,
  1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527,
  1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630,
  1721, 1722, 1723, 1724, 1725, 1726, 1727, 1728, 1729,
  1823, 1824, 1825, 1826, 1827, 1828, 
  1923, 1924, 1925, 1926, 1927,
  2028, 2029,

  1516,
  1617,

  1919,
  2020, 2021,
  2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127,
  2222,

  2529,
  2628, 2629,
  2728,

  2618,
  2717, 2718,
  2818,

  2921,

  # B1

  3513, 3514,
  3614, 3615,
  3713,

  4708,
  4808,
  4908,

  # B2

  3227,

  3318,
  3418,

  3630,

  4728, 4729,
  4829, 4830,

  4924, 4925,

  # C1

  5110,

  5215,

  6105,

  6514, 6515,
  6615,
  6715,

  # C2

  5427,

  6630,
  6730,

    
]

rivers = [
  ["A1",[[20.00, 0.50],[20.00, 3.00],[20.50, 3.75],[27.50, 6.75],[28.67, 9.00],
         [27.33,10.50],[29.50,13.75],[29.50,14.75],[30.00,16.00],[30.50,16.25],]],
  ["A1",[[19.00,15.00],[20.00,16.00],[20.00,16.50],]],
  ["A1",[[ 9.67, 0.00],[10.00, 1.00],[11.00, 1.00],[11.50, 0.75],]],
  ["A2",[[20.00,15.50],[20.00,16.50],]],
  ["A2",[[15.50,17.75],[18.00,22.00],[20.00,23.00],]],
  ["A2",[[29.50,29.75],[30.00,31.00],[30.50,31.25],]],
  ["B1",[[29.67, 0.00],[30.00, 1.00],[31.00, 1.00],[31.00, 2.00],[32.00, 3.00],
         [33.00, 2.00],[34.00, 3.00],[34.00, 3.75],[35.50, 3.25],[36.00, 2.00],
         [37.00, 1.00],[38.00, 2.00],[38.00, 3.00],[39.00, 3.00],[40.00, 3.00],
         [40.00, 0.50],]],
  ["B1",[[30.00,16.00],[32.50,14.75],[38.50,14.75],[39.00,14.00],[40.00,15.00],
         [40.00,16.00],]],
  ["B1",[[40.00,16.50],[40.00,15.00],[39.00,14.00],[39.00,13.00],[42.00,12.00],
         [45.50,13.25],[46.50,13.75],[47.50,13.25],[49.00,14.00],[50.00,16.00],
         [50.50,16.25],]],
  ["B2",[[29.67,15.00],[30.00,16.00],[33.00,17.00],[33.00,17.50],[33.50,18.25],
         [34.00,19.00],[36.00,18.00],[37.00,18.00],[37.00,19.00],[39.00,20.00],
         [39.00,22.00],[38.00,23.00],[36.00,22.00],[35.00,22.00],[35.00,24.00],
         [37.00,25.00],[37.00,26.00],[35.00,27.00],[35.00,29.00],[36.00,30.00],
         [38.00,29.00],[40.00,30.00],[40.00,31.50],]],
  ["B2",[[35.00,27.00],[34.50,27.25],[31.50,26.75],[31.00,27.00],[31.00,29.00],
         [30.00,31.00],[29.67,30.00],]],
  ["B2",[[50.50,31.25],[50.00,31.00],[49.50,29.75],[49.50,29.25],[47.00,28.00],
         [47.00,27.00],[48.50,26.75],[48.50,24.00],]],
  ["B2",[[48.00,27.00],[47.00,26.00],]],
  ["B2",[[48.00,26.00],[48.50,26.25],]],
  ["B2",[[40.00,16.25],[41.00,16.00],]],
  ["B2",[[40.00,15.50],[40.00,17.00],[41.00,17.00],[38.00,19.00],[38.00,20.00],]],
  ["B2",[[41.00,17.00],[41.00,18.00],[40.00,19.00],[39.00,18.00],]],
  ["C1",[[49.67, 0.00],[50.00, 1.00],[51.00, 1.00],[51.00, 3.00],]],
  ["C1",[[51.00, 2.00],[52.00, 2.00],[53.00, 2.00],]],
  ["C1",[[60.00, 0.50],[60.00, 1.25],[61.00, 1.00],[61.00, 3.00],[60.00, 4.00],
         [60.00, 6.00],[63.00, 7.00],[63.00, 8.00],[60.00,10.00],[55.00, 7.00],
         [54.00, 8.00],[54.00, 8.00],[54.00, 9.00],[55.00, 9.00],[55.00,11.00],
         [54.00,12.00],[54.00,13.00],[51.00,14.00],[50.00,16.00],]],
  ["C1",[[60.00,16.50],[60.00,15.00],[61.00,14.00],[63.00,15.00],[65.00,14.00],
         [65.00,13.00],[66.00,13.00],[67.00,13.00],[66.00,14.00],[66.00,15.00],
         [67.00,15.00],[68.00,15.00],[68.00,14.00],[69.00,13.00],[69.00,14.00],
         [70.00,16.00],[70.50,16.25]]],
  ["C2",[[49.67,15.00],[50.00,16.00],[51.00,16.00],]],
  ["C2",[[60.00,15.50],[60.00,17.00],[59.00,17.00],[59.00,18.00],[61.00,17.00],
         [61.00,18.00],[61.50,18.25],[63.50,18.25],[65.00,19.00],[65.00,22.00],
         [66.00,23.00],[66.00,24.00],[65.00,24.00],[65.00,25.00],[60.00,28.00],
         [60.00,31.50],]],
  ["C2",[[70.50,31.25],[70.00,31.00],[69.00,29.00],]],
]

widerivers = [
  ["A2",[[ 9.67,15.00],[10.00,16.00],[11.00,16.00],[12.00,16.50],[17.50,18.75],
         [19.00,21.00],[20.00,22.00],[20.00,27.00],[20.67,28.00],[20.67,29.00],
         [20.00,30.00],[20.00,31.50],]],
  ["A2",[[15.50,17.75],[18.00,22.00],[20.00,23.00],]],
  ["A2",[[14.00,20.00],[14.33,20.50],[16.33,21.50],]],
  ["A2",[[17.33,23.50],[17.67,24.00],]],
]

clearings = [
  ["A1",[[15.00,15.00],[15.00,14.00],[18.00,13.00],[18.00,10.00],]],
  ["A1",[[18.00,12.00],[21.00,13.00],]],
  ["B1",[[31.00, 6.00],[34.00, 5.00],]],
  ["B1",[[35.00, 0.50],[35.00, 2.50],]],
  ["C2",[[52.00,20.00],[53.00,20.00],[55.00,19.00],]],
]

bridges = [
  ["A2",[[17.65,21.675],[19.35,20.825],]],
  ["B1",[[35.00, 3.00],[35.00, 3.50],]],
  ["B1",[[45.00,12.75],[45.00,13.25],]],
  ["B1",[[47.00,13.00],[47.00,13.50],]],
]

runways = [
  ["A1",[[12.60, 4.50],[13.75, 5.80],]],
  ["A2",[[22.60,23.25],[25.40,24.25],]],
  ["A2",[[23.00,22.60],[23.00,25.40],]],
]

dams = [
  ["C2",[[60.23,27.35],[60.77,28.15],]],
]

roads = [
  ["A1",[[15.00, 0.50],[15.00, 9.00],]],
  ["A1",[[10.00, 6.00],[12.00, 5.00],[12.00, 4.00],[13.00, 3.00],[17.00, 5.00],[19.00, 4.00],[19.00, 2.00],]],
  ["A1",[[19.00, 4.00],[25.00, 7.00],[25.00,15.50],]],
  ["A1",[[10.00,11.00],[13.00, 9.00],[14.00,10.00],[16.00, 9.00],[18.00,10.00],[18.00,13.00],[15.00,14.00],[15.00,15.50],]],
  ["A1",[[18.00,12.00],[21.00,13.00],]],
  ["A1",[[24.00, 7.00],[25.00, 6.00],]],
  ["A1",[[25.00, 0.50],[25.00, 3.00],[26.00, 4.00],[26.00, 6.00],[28.00, 5.00],[30.00, 6.00],]],
  ["A1",[[30.00,11.00],[29.00,11.00],]],
  ["A1",[[27.00,15.50],[27.00,15.00],]],
  ["A1",[[27.00, 0.50],[27.00, 1.00],]],
  ["A2",[[15.00,15.50],[15.00,16.00],]],
  ["A2",[[10.00,21.00],[15.00,23.00],[10.00,26.00],]],
  ["A2",[[15.00,30.50],[15.00,21.00],]],
  ["A2",[[15.00,24.00],[17.00,23.00],[18.00,24.00],[18.00,28.00],]],
  ["A2",[[15.00,19.00],[15.00,20.00],[17.00,21.00],[17.00,22.00],[19.00,23.00],[19.00,27.00],]],
  ["A2",[[15.00,23.00],[24.00,19.00],[24.00,18.00],[27.00,16.00],[27.00,15.50],]],
  ["A2",[[21.00,20.00],[21.00,26.00],]],
  ["A2",[[25.00,15.50],[25.00,17.00],]],
  ["A2",[[22.00,18.75],[22.00,20.00],[25.00,21.00],[25.00,23.00],[30.00,26.00],]],
  ["A2",[[22.15,18.75],[22.15,19.35],[21.85,18.85],[21.85,18.25],[22.15,18.75],]],
  ["A2",[[22.30,18.75],[22.30,19.35],[21.70,18.85],[21.70,18.25],[22.30,18.75],]],
  ["A2",[[21.00,25.00],[25.00,27.00],[25.00,30.50],]],
  ["A2",[[27.00,30.50],[27.00,30.00],[25.00,29.00],]],
  ["A2",[[25.00,29.00],[27.00,28.00],[27.00,24.00],]],
  ["A2",[[29.00,21.00],[30.00,21.00],]],
  ["B1",[[30.00, 6.00],[31.00, 6.00],[35.00, 4.00],[35.00, 0.50],]],
  ["B1",[[34.00, 5.00],[38.00, 7.00],[38.00,12.00],[36.00,13.00],[35.00,12.00],[32.00,14.00],[31.00,13.00],[31.00,12.00],[32.00,12.00],[32.00,11.00],[31.00,10.00],[30.00,11.00],]],
  ["B1",[[36.00,13.00],[36.00,14.00],]],
  ["B1",[[35.00,15.50],[35.00,15.00],[36.00,15.00],]],
  ["B1",[[45.00, 0.50],[45.00,15.50],]],
  ["B1",[[47.00,15.50],[47.00,11.00],[45.00,10.00],]],
  ["B1",[[45.00, 9.00],[46.00,10.00],[46.00,11.00],]],
  ["B1",[[46.00,10.00],[46.30,10.150],[46.30,11.150],]],
  ["B1",[[46.00,10.00],[46.15,10.075],[46.15,11.075],]],
  ["B1",[[46.00,10.00],[45.85, 9.425],[45.85,10.425],]],
  ["B1",[[46.00,10.00],[45.70, 9.350],[45.70,10.350],]],
  ["B1",[[47.00,11.00],[48.00,12.00],[50.00,11.00],]],
  ["B1",[[47.00, 0.50],[47.00, 1.00],[48.00, 2.00],[48.00, 4.00],[49.00, 4.00],[49.00, 7.00],[48.00, 8.00],]],
  ["B1",[[50.00, 6.00],[49.00, 6.00],]],
  ["B2",[[30.00,21.00],[31.00,20.00],[31.00,18.00],[32.00,18.00],[33.00,18.00],]],
  ["B2",[[35.00,15.50],[35.00,17.00],[33.50,17.75],]],
  ["B2",[[45.00,15.50],[45.00,16.00],[42.00,18.00],[42.00,19.00],[41.00,19.00],[41.00,21.00],[43.00,22.00],[43.00,26.00],[42.00,27.00],[42.00,30.00],[43.00,30.00],[44.00,30.00],[45.00,30.00],[45.00,30.50],]],
  ["B2",[[45.00,30.00],[47.00,29.00],[47.00,30.50],]],
  ["B2",[[47.00,15.50],[47.00,20.00],[49.00,21.00],[50.00,21.00],]],
  ["B2",[[49.00,21.00],[49.00,25.00],[50.00,26.00],]],
  ["B2",[[30.00,26.00],[32.00,27.00],]],
  ["B2",[[35.00,30.50],[35.00,30.00],[35.83,29.67],]],
  ["C1",[[50.00, 6.00],[51.00, 6.00],[51.00, 7.00],[51.50, 7.25],[53.00, 7.25],[53.00,10.00],[52.00,11.00],[51.00,10.00],[50.00,11.00],]],
  ["C1",[[52.00,11.00],[52.00,12.00],[53.00,12.00],[53.00,14.00],[55.00,15.00],[55.00,15.50],]],
  ["C1",[[53.00,14.00],[52.00,15.00],]],
  ["C1",[[55.00, 0.50],[55.00, 2.00],[54.00, 3.00],[54.00, 4.00],[58.00, 6.00],[58.00, 7.00],[60.00, 8.00],[60.00, 9.75],]],
  ["C1",[[59.00, 7.00],[59.00, 6.00],[59.67, 5.67],]],
  ["C1",[[65.00, 0.50],[65.00, 1.00],[63.00, 2.00],[63.00, 4.00],[60.33, 5.83],]],
  ["C1",[[63.00, 4.00],[65.00, 5.00],[65.00, 6.00],[66.00, 7.00],[69.00, 5.00],[70.00, 6.00],]],
  ["C1",[[60.00,10.25],[60.00,12.00],[61.00,12.00],[62.00,12.00],[63.00,12.00],[64.00,13.00],[64.00,14.00],[64.67,14.37],]],
  ["C1",[[64.00,13.00],[67.00,11.00],[68.00,12.00],[70.00,11.00],]],
  ["C1",[[67.00,15.50],[67.00,15.17],]],
  ["C1",[[64.00, 2.00],[65.00, 2.00],[67.00, 1.00],[67.00, 0.50],]],
  ["C1",[[65.00,15.50],[65.00,15.00],]],
  ["C2",[[55.00,15.50],[55.00,19.00],[53.00,20.00],[52.00,20.00],[50.00,21.00],]],
  ["C2",[[50.00,26.00],[54.00,28.00],[54.00,29.00],[55.00,29.00],[55.00,30.50],]],
  ["C2",[[54.00,28.00],[54.00,27.00],[60.00,24.00],[60.00,20.00],[62.00,19.00],]],
  ["C2",[[62.00,18.50],[62.00,18.00],[65.00,16.00],[65.00,15.50],]],
  ["C2",[[67.00,15.50],[67.00,17.50],[68.00,19.50],[68.00,21.00],[69.00,21.00],]],
  ["C2",[[65.00,30.50],[65.00,29.00],[68.00,28.00],[68.00,22.00],[70.00,21.00],]],
  ["C2",[[68.00,25.00],[70.00,26.00],]],
]
