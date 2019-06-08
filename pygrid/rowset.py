import pygrid as g

class RowSet:
  def __init__(self, _schema: g.RowSchema):
    self._schema        = _schema
    self._column_count  = len(_schema)
    self._rows          = []
    self._row_count     = len(self._rows)
    self._column_widths = [0 for column in range(self._column_count)]

  @property
  def rows(self) -> list:
    return self._rows

  @property
  def column_widths(self) -> list:
    return self._column_widths

  @property
  def schema(self) -> g.RowSchema:
    return self._schema

  def append(self, _row: g.Row):
    _column_count = len(_row)

    if _column_count != self._column_count:
      raise Exception(f'{self._column_count} columns expected, {_column_count} given')

    self._rows.append(_row)
    self._row_count += 1

    for _i, _c in enumerate(_row.cells):
      _w      = len(_c)
      _cw     = self._column_widths
      _cw[_i] = max(_w, _cw[_i])

  def __iadd__(self, _row):
    self.append(_row)

    return self

  def __len__(self) -> int:
    return self._row_count

