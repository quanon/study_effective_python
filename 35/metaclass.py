class Meta(type):
  def __new__(meta, name, bases, class_dict):
    for key, value in class_dict.items():
      if isinstance(value, Field):
        value.name = key
        value.internal_name = '_' + key

    return super().__new__(meta, name, bases, class_dict)


class Field(object):
  def __init__(self):
    self.name = None
    self.internal_name = None

  def __get__(self, instance, instance_type):
    if instance is None:
      return self

    return getattr(instance, self.internal_name, '')

  def __set__(self, instance, value):
    # インスタンス辞書に保護フィールドとして直接保存する。
    setattr(instance, self.internal_name, value)


class DatabaseRow(object, metaclass=Meta):
  pass


class BetterCustomer(DatabaseRow):
  first_name = Field()
  last_name = Field()
  prefix = Field()
  suffix = Field()

if __name__ == '__main__':
  foo = BetterCustomer()
  print(f'Before: {repr(foo.first_name)} {foo.__dict__}')
  # Before: '' {}

  foo.first_name = 'Senjogahara'
  print(f'After: {repr(foo.first_name)} {foo.__dict__}')
  # After: Senjogahara {'_first_name': 'Senjogahara'}
