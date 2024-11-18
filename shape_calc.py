class Rectangle:
  #always initiate functions in class
  def __init__(self,width,height):
    self.width=width
    self.height=height
  # string to return proper format
  def __str__(self):
    string=f'Rectangle(width={self.width}, height={self.height})'
    return string
  #set width
  def set_width(self,width):
    self.width=width
  #set height
  def set_height(self,height):
    self.height=height
  #get the area
  def get_area(self):
    area=self.width*self.height
    return area
  #perimeter
  def get_perimeter(self):
    perimeter=2 * self.width + 2 * self.height
    return perimeter
  #diagonal
  def get_diagonal(self):
    diagonal=(self.width ** 2 + self.height ** 2) ** .5
    return diagonal
  #picture
  def get_picture(self):
    if self.height>50 or self.width>50:
      return 'Too big for picture.'
    picture=(('*'*self.width)+'\n')*self.height
    return picture
  #how many times could a shape fit in this shape
  def get_amount_inside(self,shape):
    shape_in_shape=int(self.get_area()/shape.get_area())
    return shape_in_shape

    

class Square(Rectangle):
  #initiate functions in class
  def __init__(self,side):
    self.width=side
    self.height=side
  #string function
  def __str__(self):
    string=f'Square(side={self.width})'
    return string
  #set side
  def set_side(self,side):
    self.width=side
    self.height=side
