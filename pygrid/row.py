import pygrid as g

class Row:
  def __init__(self, _cell_count_limit: int):
    self._cell_count_limit = _cell_count_limit
    self._cells            = []
    self._cell_count       = len(self._cells)

  @property
  def cells(self) -> list:
    return self._cells

  @property
  def width(self) -> int:
    return 1

  def append_one(self, _value) -> None:
    if type(_value) is g.Cell:
      self._cells.append(_value)
    else:
      self._cells.append(g.Cell(_value))

    self._cell_count += 1

  def append(self, *args) -> None:
    if self._cell_count == self._cell_count_limit:
      raise Exception('Cell limit reached')

    if len(args) == 0:
      raise Exception('Cannot append nothing')

    for _value in args:
      self.append_one(_value)

    return self

  def __len__(self) -> int:
    return self._cell_count

