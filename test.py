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

def get_closest_enemy(state):
  player_position = (state["player"]["x"], state["player"]["y"])

  enemies = state["opponents"]
  min_distance = float("inf")
  closest_enemy = None

  for enemy in enemies:
    enemy_position = (enemy["x"], enemy["y"])
    distance = ((player_position[0] - enemy_position[0])**2 + (player_position[1] - enemy_position[1])**2)**0.5

    if distance < min_distance:
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
    newBullet = {
      "dx": closest_enemy["x"] - state["player"]["x"] + random.randint(-4, 4),
      "dy": closest_enemy["y"] - state["player"]["y"] + random.randint(-4, 4),
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
  