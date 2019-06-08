import pygrid as g

class Banner(g.Row):
  def __init__(self, _banner_text: str='New Banner'):
    self._text = _banner_text

    super().__init__(1)
    self.append(g.Cell(_banner_text))

  def __str__(self) -> str:
    return self._text

