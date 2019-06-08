import pygrid as g

class Grid:

  def __init__(self, _head_banner_text: str = None):
    self._row_sets      = []
    self._head_banner   = None

    if _head_banner_text:
      self._head_banner = g.HeadBanner(_head_banner_text)

  def append(self, _rows: g.RowSet) -> None:
    self._row_sets.append(_rows)

  def __str__(self) -> str:
    text_grid = ''

    for rsi, rs in enumerate(self._row_sets):
      widths       = rs.column_widths
      first_rowset = 0 == rsi

      for ir, r in enumerate(rs.rows):
        text_line_pre  = ''
        text_line      = ''
        text_line_post = ''
        first_row = 0 == ir
        last_row  = len(rs.rows) == ir + 1

        for ic, c in enumerate(r.cells):
          char_length = len(c)
          first_cell  = 0 == ic
          last_cell   = len(r.cells) == ic + 1
          pad         = ' ' * (widths[ic] - char_length)
          align       = rs.schema.columns[ic].get('align', 'left')
          text_cell   = ''
          sepprerow   = ''
          seppostrow  = ''

          if align == 'right':
            text_cell = f'{pad}{c}'
          else:
            text_cell = f'{c}{pad}'

          if first_cell:
            text_line += f' {text_cell} '
          else:
            text_line += f'│ {text_cell} '


          if first_row:
            text_line_pre += '┬' if not first_cell else ''
          elif last_row:
            text_line_pre  += '┼' if not first_cell else ''
            text_line_post += '┴' if not first_cell else ''
          else:
            text_line_pre  += '┼' if not first_cell else ''
            text_line_post += '┼' if not first_cell else ''

          text_line_pre += '─'
          text_line_pre += '─' * widths[ic]
          text_line_pre += '─'

          text_line_post += '─'
          text_line_post += '─' * widths[ic]
          text_line_post += '─'

        if first_row:
          if self._head_banner:
            text_grid += f'├{text_line_pre}┤\n'
          else:
            text_grid += f'┌{text_line_pre}┐\n'

          text_grid += f'│{text_line}│\n'
        else:
          text_grid += f'├{text_line_pre}┤\n'
          text_grid += f'│{text_line}│\n'


        if last_row:
          text_grid += f'└{text_line_post}┘\n'

    return text_grid

