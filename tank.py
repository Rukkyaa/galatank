import json
import sys
import random

# Oponent
#   "x": number,
#   "y": number,
#   "direction": "UP" | "DOWN" | "LEFT" | "RIGHT" | "NONE"

# "bullets": {
# 	"fromPlayer": [{ // Les balles tirées par votre tank et encore en jeu
# 		"x": 50,
# 		"y": 20,
# 		"dx": 2,
# 		"dy": 1	
# 	}],
# 	"fromOpponents": [{
# 		"x": 50,
# 		"y": 40,
# 		"dx": 2,
# 		"dy": 1
# 	}]
# }


def	dist(point1, point2):
	return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def det(a, b):
	return a[0] * b[1] - a[1] * b[0]

# rectanlgles(x, y, w, h)

def	intersection_with_rectangles(line, rectangles):
	for rectangle in rectangles:
		a = (rectangle["x"], rectangle["y"])
		b = (rectangle["x"] + rectangle["width"], rectangle["y"])
		c = (rectangle["x"] + rectangle["width"], rectangle["y"] + rectangle["height"])
		d = (rectangle["x"], rectangle["y"] + rectangle["height"])
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

def get_closest_enemy(state):
  player_position = (state["player"]["x"], state["player"]["y"])

  enemies = state["opponents"]
  min_distance = float("inf")
  closest_enemy = None

  for enemy in enemies:
    enemy_position = (enemy["x"], enemy["y"])
    distance = ((player_position[0] - enemy_position[0])**2 + (player_position[1] - enemy_position[1])**2)**0.5

    if distance < min_distance and intersection_with_rectangles((player_position, enemy_position), state["map"]["walls"]) == False:
      min_distance = distance
      closest_enemy = enemy

  return closest_enemy


def get_closest_bullet(state):
  player_position = (state["player"]["x"], state["player"]["y"])

  bullets = state["bullets"]["fromOpponents"]
  min_distance = float("inf")
  closest_bullet = None

  if len(bullets) == 0:
    return None

  for bullet in bullets:
    bullet_position = (bullet["x"], bullet["y"])
    distance = ((player_position[0] - bullet_position[0])**2 + (player_position[1] - bullet_position[1])**2)**0.5

    if distance < min_distance:
      min_distance = distance
      closest_bullet = bullet

  return closest_bullet

def get_dodge_direction(bullet):
  if bullet is None:
    return "UP"
  
  if abs(bullet["dx"]) > abs(bullet["dy"]):
    return "UP" if bullet["dy"] > 0 else "DOWN"
  else:
    return "LEFT" if bullet["dx"] > 0 else "RIGHT"

while True:
  state = json.loads(input())
  
  # direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
  newBullet = None
  closest_enemy = get_closest_enemy(state)

  closest_bullet = get_closest_bullet(state)

  if state["player"]["canShoot"]:
    if closest_enemy is not None:
      newBullet = {
        "dx": closest_enemy["x"] - state["player"]["x"],
        "dy": closest_enemy["y"] - state["player"]["y"],
      }

  direction = get_dodge_direction(closest_bullet)

  print(json.dumps({
    "direction": direction,
    "newBullet": newBullet
  }))
  sys.stdout.flush()
  
# {
# 	"map": {
# 		"width": 400,
# 		"height": 200,
# 		"walls": [{ // Les murs ne peuvent être traversés ni par les tanks, ni par les balles. Si une balle heurte un mur, elle est détruite.
# 			"x": 20,
# 			"y": 40,
# 			"width": 100,
# 			"height": 100
# 		}, {
# 			"x": 320,
# 			"y": 100,
# 			"width": 20,
# 			"height": 50
# 		}]
# 	},
# 	"player": { // Votre tank
# 		"x": 250,
# 		"y": 150,
# 		"canShoot": true /	/ Êtes-vous autorisé à tirer ?
# 	},
# 	"	opponents": [{ // La liste de vos adversaires encore en vie et leur direction actuelle
# 		"x": 150,
# 		"y": 72,
# 		"direction": "UP"
# 	}, {
# 		"x": 300,
# 		"y": 100,
# 		"direction": "NONE"
# 	}],
# 	"bullets": {
# 		"fromPlayer": [{ // Les balles tirées par votre tank et encore en jeu
# 			"x": 50,
# 			"y": 20,
# 			"dx": 2,
# 			"dy": 1	
# 		}],
# 		"fromOpponents": [{
# 			"x": 50,
# 			"y": 40,
# 			"dx": 2,
# 			"dy": 1
# 		}]
# 	}
# }

# Avoir l'enemie le plus proche
  