class RowSchema:
  def __init__(self, _columns: list):
    self._columns             = []
    self._column_names        = []
    self._column_name_lengths = {}
    self._column_count        = len(self._columns)

    for _index, _column in enumerate(_columns):
      _name  = _column.get('name')
      _align = _column.get('align', 'left')
      _width = _column.get('width', 'auto')

      if not _name:
        raise Exception(f'Column {_index} has no name')

      if _name in self._column_names:
        raise Exception(f'"{_name}" column already exists')

      if not _align in ['left', 'right']:
        raise Exception(f'Unknown column alignment "{_align}" in "{_name}" column')

      if not _width in ['auto', 'fixed']:
        raise Exception(f'Unknown column width "{_width}" in "{_name}" column')

      self._columns.append(
      {
        'name': _name
        ,'align': _align
        ,'width': _width
      })
      self._column_names.append(_name)
      self._column_name_lengths[_name] = len(_name)

    self._column_count = len(self._columns)

  @property
  def columns(self) -> list:
    return self._columns

  @property
  def column_names(self) -> list:
    return self._column_names

  @property
  def column_name_lengths(self) -> dict:
    return self._column_name_lengths

  def __len__(self) -> int:
    return self._column_count

  def __iter__(self):
    return iter(self._columns)

