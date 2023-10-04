from types import NoneType
import airpower.hex as aphex
import airpower.map as apmap

def _split(h):

  """ 
  Split the hex code h of the form XXYY and return XX and YY as integers.
  """

  assert isvalidhexcodeforcenter(h)

  h = int(h)
  XX = h // 100
  YY = h % 100
  return XX, YY

def _join(XX, YY):

  """
  Return the hex code XXYY corresponding to the integers XX and YY.
  """

  assert 00 <= XX and XX <= 99 and XX % 1 == 0
  assert 00 <= YY and YY <= 99 and YY % 1 == 0

  return int(100 * XX + YY)

def _inrange(h):

  """
  Return True if h is within the range of valid hex codes of the form XXYY. 
  Otherwise return False.
  """

  return 0 <= h and h <= 9999

def isvalidhexcodeforcenter(h):

  """
  Return True if h is grammatically a hex code that corresponds to a hex 
  center. Otherwise return False.
  """

  if isinstance(h, int) and _inrange(h):
    return True

  if isinstance(h, float) and h % 1.0 == 0.0 and _inrange(h):
    return True

  if isinstance(h, str) and h.isdecimal() and _inrange(int(h)):
    return True

  return False

def checkisvalidhexcodeforcenter(h):

  """
  Raise a RuntimeError exception if h is not a gramatically valid hex code that
  corresponds to a hex center.
  """

  if not isvalidhexcodeforcenter(h):
    raise RuntimeError("%s is not a valid hex code for a hex center." % h)

def isvalidhexcodeforedge(h):

  """
  Return True if h is grammatically a hex code that corresponds to (the center 
  of) the edge of a hex. Otherwise return False.
  """

  if not isinstance(h, str):
    return False

  m = h.split("/")
  if len(m) != 2:
    return False

  if not m[0].isdecimal() or not _inrange(int(m[0])):
    return False

  if not m[1].isdecimal() or not _inrange(int(m[1])):
    return False

  return True

def checkvalidhexcodeforedge(h):

  """
  Raise a RuntimeError exception if h is not a gramatically valid hex code that
  corresponds to (the center of) the edge of a hex.
  """

  if not isvalidhexcodeforedge(h):
    raise RuntimeError("%s is not a valid hex code for a hex edge." % h)

def isvalidhexcode(h):

  """
  Return True if h is a grammatically valid hex code. Otherwise return False.
  """

  return isvalidhexcodeforcenter(h) or isvalidhexcodeforedge(h)

def checkisvalidhexcode(h):

  """
  Raise a RuntimeError exception if h is not a gramatically valid hex code.
  """

  if not isvalidhexcode(h):
    raise RuntimeError("%s is not a valid hex code." % h)

def fromxy(x, y, sheet=None):

  """
  Return the hex code corresponding to the hex coordinate (x, y).
  """

  aphex.checkisvalidposition(x, y)

  if aphex.iscenterposition(x, y):

    if sheet == None:
      sheet = apmap.tosheet(x, y)
      # Check the upper right edge.
      if sheet == None:
        sheet = apmap.tosheet(x - 0.50, y + 0.25)
      if sheet == None:
        raise RuntimeError("position is not within the map.")

    x0, y0 = apmap.sheetorigin(sheet)
    XX0, YY0 = _split(sheetorigin(sheet))
    XX = XX0 + (x - x0)
    YY = YY0 - (y - y0)
    if XX % 2 == 1:
      YY -= 0.5

    return _join(XX, YY)

  else:

    x0, y0, x1, y1 = aphex.edgetocenters(x, y)

    if sheet == None:
      sheet0 = apmap.tosheet(x0, y0)
      sheet1 = apmap.tosheet(x1, y1)
      if sheet0 != None:
        sheet = sheet0
      elif sheet1 != None:
        sheet = sheet1
      else:
        raise RuntimeError("position is not within the map.")

    h0 = fromxy(x0, y0, sheet=sheet)
    h1 = fromxy(x1, y1, sheet=sheet)

    if h0 < h1:
      return "%s/%s" % (h0, h1)
    else:
      return "%s/%s" % (h1, h0)      

def toxy(h, sheet=None):

  """
  Return the hex coordinate (x, y) corresponding to the hex code h.
  """

  checkisvalidhexcode(h)

  if isvalidhexcodeforcenter(h):

    XX, YY = _split(h)

    if sheet == None:
      sheet = tosheet(h, strict=False)
      if sheet == None:
        raise RuntimeError("hex code %s is not within the map." % h)

    XX0, YY0 = _split(sheetorigin(sheet))
    x0, y0 = apmap.sheetorigin(sheet)

    dx = XX - XX0
    dy = YY0 - YY
    if XX % 2 == 1:
      dy -= 0.5

    return x0 + dx, y0 + dy

  else:

    m = h.split("/")
    h0 = m[0]
    h1 = m[1]

    if sheet == None:
      sheet0 = tosheet(h0, strict=True)
      sheet1 = tosheet(h1, strict=True)
      if sheet0 == None:
        sheet0 = sheet1
      elif sheet1 == None:
        sheet1 = sheet0

    x0, y0 = toxy(h0, sheet=sheet0)
    x1, y1 = toxy(h1, sheet=sheet1)

    return 0.5 * (x0 + x1), 0.5 * (y0 + y1)

def sheetorigin(sheet):

  """
  Return the hex code of the center of the lower left hex in the specified sheet.
  """

  sheetletter = sheet[0]
  if sheetletter == "A":
    XX = 10
  elif sheetletter == "B":
    XX = 30
  elif sheetletter == "C":
    XX = 50
  else:
    raise RuntimeError("invalid sheet %s." % sheet)

  sheetnumber = sheet[1]
  if sheetnumber == "1":
    YY = 16
  elif sheetnumber == "2":
    YY = 31
  else:
    raise RuntimeError("invalid sheet %s." % sheet)

  return _join(XX, YY)

def isonsheet(h, sheet):

  """
  Return True if the hex code h is on the specified sheet. The hex code must
  correspond to the center of a hex, not an edge.
  """

  checkisvalidhexcodeforcenter(h)

  XX, YY = _split(h)
  XX0, YY0 = _split(sheetorigin(sheet))

  if XX < XX0 or XX >= XX + 20:
    return False
  elif XX % 2 == 1 and YY > YY0 or YY < YY0 - 14:
    return False
  elif YY > YY0 + 1 or YY < YY0 - 13:
    return False

  return True

def tosheet(h, strict=False):

  """
  Returns the sheet containing the hex code h, which must refer to a hex center.
  If strict is true, do not include the half-hexes on the lower and right sides.
  if strict is false, include them.
  """

  checkisvalidhexcodeforcenter(h)

  XX, YY = _split(h)

  if strict:
    if 11 <= XX and XX <= 29:
      sheetletter = "A"
    elif 31 <= XX and XX <= 49:
      sheetletter = "B"
    elif 51 <= XX and XX <= 69:
      sheetletter = "C"
    else:
      return None
  else:
    if 11 <= XX and XX <= 30:
      sheetletter = "A"
    elif 31 <= XX and XX <= 50:
      sheetletter = "B"
    elif 51 <= XX and XX <= 70:
      sheetletter = "C"
    else:
      return None
  
  if strict:

    if XX % 2 == 1 and 1 <= YY and YY <= 15:
      sheetnumber = "1"
    elif XX % 2 == 0 and 2 <= YY and YY <= 15:
      sheetnumber = "1"
    elif XX % 2 == 1 and 16 <= YY and YY <= 30:
      sheetnumber = "2"
    elif XX % 2 == 0 and 17 <= YY and YY <= 30:
      sheetnumber = "2"
    else:
      return None

  else:

    if XX % 2 == 1 and 1 <= YY and YY <= 15:
      sheetnumber = "1"
    elif XX % 2 == 0 and 2 <= YY and YY <= 16:
      sheetnumber = "1"
    elif XX % 2 == 1 and 16 <= YY and YY <= 30:
      sheetnumber = "2"
    elif XX % 2 == 0 and 17 <= YY and YY <= 31:
      sheetnumber = "2"
    else:
      return None

  return sheetletter + sheetnumber

