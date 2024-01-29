import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

radius = 5  
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is {volume}")
