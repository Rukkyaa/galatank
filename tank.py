import json
import sys
import random

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

while True:
  state = json.loads(input())
  
  # direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
  newBullet = None
  closest_enemy = get_closest_enemy(state)
  if state["player"]["canShoot"]:
    newBullet = {
      "dx": closest_enemy["x"] - state["player"]["x"],
      "dy": closest_enemy["y"] - state["player"]["y"],
    }
    
  print(json.dumps({
    "direction": None,
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
  