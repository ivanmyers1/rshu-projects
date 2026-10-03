import math
radius = 6.371e6
a = 4 * math.pi * radius ** 2
pressure = 98400
temperature = 288
r = 8.314
m = 0.02896
rs = r/m
h = (rs * temperature)/9.81
ro = pressure / (rs * temperature)
mass = a * ro * h
print(f'{mass=}')
print('-'*50)

# second task
h2 = 500
ro_s = 10e-9
mass_sea_salt = a * 0.7 * ro_s * h2
mass_in_tons = mass_sea_salt/1000
print(f'{mass_in_tons=}')
