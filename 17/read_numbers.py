class ReadNumbers(object):
  def __init__(self, filepath):
    self.filepath = filepath

  def __iter__(self):
    with open(self.filepath) as f:
      for line in f:
        yield int(line)
