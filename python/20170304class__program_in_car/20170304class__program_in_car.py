class car:
  def __init__(self,s,w):
    self.steering=s
    self.wheel=w
  def drive(self):
    print "drive the car using " + self.steering 
my_car=car("my steering","my wheel")


print my_car.steering
print my_car.wheel
my_car.drive()
