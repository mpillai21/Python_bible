import random

health=50
difficulty=3
potion_health = int(random.randint(25,50)/3)

health+=potion_health
print(potion_health)
print(health)
