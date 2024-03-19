
def det(a, b):
	return a[0] * b[1] - a[1] * b[0]

# rectanlgles(x, y, w, h)

def	intersection_with_rectangles(line, rectangles):
	for rectangle in rectangles:
		a = (rectangle["x"], rectangle["y"])
		b = (rectangle["x"] + rectangle["w"], rectangle["y"])
		c = (rectangle["x"] + rectangle["w"], rectangle["y"] + rectangle["h"])
		d = (rectangle["x"], rectangle["y"] + rectangle["h"])
		line1 = (a, b)
		line2 = (b, c)
		line3 = (c, d)
		line4 = (d, a)
		if line_intersection(line, line1) or line_intersection(line, line2) or line_intersection(line, line3) or line_intersection(line, line4):
			return True
	return False

def line_intersection(line1, line2):
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

	div = det(xdiff, ydiff)
	if div == 0:
	   return False

	d = (det(*line1), det(*line2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div


	return is_point_in_segment(line1, (x, y)) and is_point_in_segment(line2, (x, y))


def is_point_in_segment(line, point):
	# half = ((line[0][0] + line[1][0]) / 2, (line[0][1] + line[1][1]) / 2)
	half = (line[0][0] + (line[1][0] - line[0][0]) / 2, line[0][1] + (line[1][1] - line[0][1]) / 2)
	dist_with_half = dist(half, point)
	return (dist_with_half < dist(line[0], line[1]) / 2)

	
def	dist(point1, point2):
	return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


# tests


# rectangles = [
# 	{
# 		"x": 0.55,
# 		"y": 1.18,
# 		"w": 4.08,
# 		"h": 3.2
# 	}
# ]
# # should be True
# print(intersection_with_rectangles(((0, 0), (5.91, 0.62)), rectangles))

# rectangles = [
# 	{
# 		"x": 0.55,
# 		"y": 1.18,
# 		"w": 7.14,
# 		"h": 0.5
# 	}
# ]
# # should be False
# print(intersection_with_rectangles(((0, 0), (1.84, 4.8)), rectangles))