def fight(robot_1, robot_2, tactics):
  hp1 = robot_1.get('health')
  rb1attack = robot_1.get('tactics')
  hp2 = robot_2.get('health')
  rb2attack = robot_2.get('tactics')


  #whose attacking 1 = robot_1 and 2 = robot_2
  pos = 0
  if robot_1.get('speed') == robot_2.get('speed'):
    pos  = 1
  elif robot_1.get('speed') > robot_2.get('speed'):
    pos = 1
  else:
    pos = 2
  
  fighton = True
  while fighton:
    # determining who wins
    if hp1 <= 0:
      return robot_2.get('name') + " has won the fight."
    elif hp2 <= 0:
      return robot_1.get('name') + " has won the fight."
    elif len(rb1attack) == 0 and len(rb2attack) == 0:
      if hp1 > hp2:
        return robot_1.get('name') + " has won the fight."
      elif hp1 == hp2:
        return "The fight was a draw."
      else:
        return robot_2.get('name') + " has won the fight."


    if len(rb1attack) == 0:
      hp1 = hp1 - tactics.get(rb2attack[0])
      rb2attack.pop(0)
    elif len(rb2attack) == 0:
      hp2 = hp2 - tactics.get(rb1attack[0])
      rb1attack.pop(0)
    elif pos == 1:
      hp2 = hp2 - tactics.get(rb1attack[0])
      rb1attack.pop(0)
      pos = 2
    elif pos == 2:
      hp1 = hp1 - tactics.get(rb2attack[0])
      rb2attack.pop(0)
      pos = 1


    

    





robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}



print(fight(robot_1, robot_2, tactics))