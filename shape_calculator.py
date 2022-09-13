import math
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self. height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for h in range(self.height):
        picture += "*" * self.width + "\n"
    return picture

  def get_amount_inside(self, shape):
    m = math.floor(self.width/shape.width)
    n = math.floor(self.height/shape.height)
    return m * n
    
  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)
    
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
  
  def set_side(self, side):
    self.width = side
    self.height = side
    
  def __str__(self):
    return "Square(side={})".format(self.width)
  