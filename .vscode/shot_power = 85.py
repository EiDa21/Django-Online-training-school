shot_power = 85
long_shot = 76

weights = {'shot_power': 0.7, 'long_shot': 0.3}
overall_shot = sum(value * weights[key] for key, value in {'shot_power': shot_power, 'long_shot': long_shot}.items())
print(overall_shot)