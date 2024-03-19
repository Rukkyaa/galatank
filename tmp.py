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

def dist(a, b):
  return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def get_closest_position(positions, player_pos):
  if len(positions) == 0:
    return None

  min_distance = dist(player_pos, positions[0])
  closest_position = None

  for position in positions[1:]:
    distance = dist(player_pos, position)

    if distance < min_distance:
      min_distance = distance
      closest_position = position

  return closest_position


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
  if bullet["dx"] > 0:
    return "LEFT"
  elif bullet["dx"] < 0:
    return "RIGHT"
  elif bullet["dy"] > 0:
    return "UP"
  elif bullet["dy"] < 0:
    return "DOWN"
  else:
    return "LEFT"

while True:
  state = json.loads(input())
  
  newBullet = None
  enemy_positions = [(opp['x'], opp['y']) for opp in state["opponents"]]

  player_position = (state["player"]["x"], state["player"]["y"])
  closest_enemy = get_closest_position(enemy_positions, player_position)

  closest_bullet = get_closest_bullet(state)

  # if state["player"]["canShoot"] and closest_enemy is not None:
  #   newBullet = {
  #     "dx": closest_enemy[0] - state["player"]["x"],
  #     "dy": closest_enemy[1] - state["player"]["y"],
  #   }

  direction = get_dodge_direction(closest_bullet) if closest_bullet is not None else None

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
  