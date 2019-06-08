class Cell:
  def __init__(self, _value):
    self._value  = _value
    self._length = len(str(_value).strip())

  @property
  def value(self):
    return self._value

  def __len__(self) -> int:
    return self._length

  def __str__(self) -> str:
    return str(self._value).strip()

  def __repr__(self):
    return str(self._value)

