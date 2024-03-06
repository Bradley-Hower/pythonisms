
class Powers:
  """Class to iterate at power of two"""

  def __init__(self, max=0):
    self.max = max
  
  def __iter__(self):
    self.n = 0
    return self

  def __next__(self):
      if self.n <= self.max:
          tothe = 2
          result = tothe ** self.n
          self.n += 1
          return result
      else:
          raise StopIteration


numbers = Powers(3)

i = iter(numbers)

print(next(i))
print(next(i))
