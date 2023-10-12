import airpower.log as aplog

################################################################################

def closeformationnames(self):

  """
  Return a list containing the names of the aircraft in close formation with the
  aircraft or an empty list if the aircraft is not in close formation.
  """

  return sorted(map(lambda a: a._name, self._closeformation))

################################################################################


def closeformationsize(self):

  """
  Returns the total number of aircraft in the close formation with the
  aircraft or zero if the aircraft is not in close formation.
  """

  return len(self._closeformation)

################################################################################

def leavecloseformation(self):

  """
  The aircraft leaves its close formation.
  """

  aplog.clearerror()
  try:

    if self.closeformationsize() == 0:
     raise RuntimeError("%s: is not in a close formation." % self._name)

    self._leaveanycloseformation()
  
  except RuntimeError as e:
    aplog.logerror(e)

################################################################################

def joincloseformation(self, other):

  """
  The aircraft joins a close formation with other. Any aircraft previously in
  a close formation either with the aircraft or other are also part of the
  resulting close formation.
  """

  aplog.clearerror()
  try:

    if self._x != other._x or self._y != other._y:
      raise RuntimeError("attempt to form a close formation from aircraft with different positions.")
    if self._altitude != other._altitude:
      raise RuntimeError("attempt to form a close formation from aircraft with different altitudes.")
    if self._facing != other._facing:
      raise RuntimeError("attempt to form a close formation from aircraft with different facings.")
    if self._speed != other._speed:
      raise RuntimeError("attempt to form a close formation from aircraft with different speeds.")

    nself  = max(1, self.closeformationsize())
    nother = max(1, other.closeformationsize())
    if nself + nother > 4:
      raise RuntimeError("attempt to form a close formation with more than four aircraft.")

    if self._closeformation == []:
      self._closeformation = [self]

    if other._closeformation == []:
      other._closeformation = [other]
      
    self._closeformation += other._closeformation
    for a in self._closeformation:
      a._closeformation = self._closeformation

    self._checkcloseformation()

  except RuntimeError as e:
    aplog.logerror(e)

################################################################################

def _checkcloseformation(self):

  """
  Raise an exception if any of the other aircraft in close formation with the
  aircraft do not have the same position, altitude, facing, and speed.
  """

  for a in self._closeformation:
    if self._x != a._x or self._y != a._y:
      raise RuntimeError("aircraft %s and %s cannot be in close formation as they do not have the same positions." % (self._name, a._name))
    if self._altitude != a._altitude:
      raise RuntimeError("aircraft %s and %s cannot be in close formation as they do not have the same altitudes." % (self._name, a._name))
    if self._facing != a._facing:
      raise RuntimeError("aircraft %s and %s cannot be in close formation as they do not have the same facings." % (self._name, a._name))
    if self._speed != a._speed:
      raise RuntimeError("aircraft %s and %s cannot be in close formation as they do not have the same speeds." % (self._name, a._name))

################################################################################

def _leaveanycloseformation(self):

  """
  The aircraft leaves its close formation, if it is in one.
  """

  if self._closeformation != []:
    self._closeformation.remove(self)
    self._closeformation = []

################################################################################


