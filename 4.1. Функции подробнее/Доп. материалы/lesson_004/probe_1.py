import simple_draw as sd

sd.resolution = (1200, 800)

point = sd.get_point(600, 200)
side = sd.get_vector(start_point=point, angle=90, length=100)
side_2 = sd.get_vector(start_point=side.end_point, angle=180, length=200)
# side.draw()
# side_2.draw()
side_3 = side.add(side_2)
print(side.__str__())

sd. pause()
