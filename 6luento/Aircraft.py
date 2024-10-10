##Keksitkö muita attribuutteja lentokoneelle?


class Aircraft:

  def __init__(self, aircraft_type, max_number_of_passangers):
    print("2. Initialize the new instance of Aircraft.")
    self.aircraft_type = aircraft_type
    self.max_number_of_passangers = max_number_of_passangers

  def __repr__(self) -> str:
    return f"{type(self).__name__}(air_craft_type={self.aircraft_type}, max_number_of_passangers={self.max_number_of_passangers})"

  def invariant(self):
    if (self.aircraft_type is None):
      raise ValueError("Aircraft type is not set!")
    if (self.max_number_of_passangers is None):
      raise ValueError("Max number of passangers is not given")
