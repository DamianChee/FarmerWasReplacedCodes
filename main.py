def is_even(n):
	return n % 2 == 0

def GrassMaker():
	for y in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)
		
def WoodMaker(n):
	for y in range(get_world_size()):
		if is_even(n):
			if is_even(y):
				if can_harvest():
					harvest()
					plant(Entities.Bush)
			else:
				if can_harvest():
					harvest()
					plant(Entities.Tree)
		else:
			if not is_even(y):
				if can_harvest():
					harvest()
					plant(Entities.Bush)
			else:
				if can_harvest():
					harvest()
					plant(Entities.Tree)
		move(North)

def CarrotMaker():
	for y in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		if can_harvest() or get_entity_type() == None:
			harvest()
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
		move(North)

while True:
	for x in range(get_world_size()):
		if x == 3:
			CarrotMaker()
		elif x >= 1:
			WoodMaker(x)
		else:
			GrassMaker()
		move(East)
