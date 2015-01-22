from sys import exit
life = []
equipment = []

#def adventure():
#	global life
#	life = 10
#	global equipment
#	equipment = []	
	

def death(how):
	print how, "The End."
	exit(0)
#adventure()

#if life <= 0:
#	death(how)
#else:
#	life = life


print "Slowly, you start to open your eyes."
print "As your vision starts to focus, your reality slowly sets in."
print "You realize you have no memories of how you got here."
print '"Who am I?" "Where am I?"'
print "You get on your feet and survey your surroundings."
print "To the north lies a forest."
print "To the east, you can see the tall mountain range."
print "The sound of running water can be heard to the south."
print "Perhaps your eyes are playing tricks on you, but is that house?"

def start():
	print "You get the feeling staying here is a bad idea."


	next = raw_input("What will you do? ")
	if "north" in next or "forest" in next:
		forest()
	elif "east" in next or "mountain" in next:
		mountain()
	elif "south" in next or "river" in next or "water" in next:
		river()
	elif "house" in next or "west" in next:
		ruins()
	else:
		print "That really gets you no where..."
		start()

def forest():
	print "As soon as you cross into the forrest, something feels off."
	print "You're sure something is watching you."

	next = raw_input('"Will I press on?" "Maybe I should head back..."')
	if "keep" in next or "press on" in next:
		trap()
	if next == 'head back':
		start()

def mountain():
	print"As you approach the mountain, you notice a stick on the ground."
	#stick = False
	next = raw_input("> ")
	if "pick" in next or "up" in next:
		print"This should hopefully be useful for the trip up."
		equipment.append("stick")
	else:
		print "You leave it behind and continue towards the mountain"
	print "At the foot of the mountain, you see two possible ways up."
	
	direction = raw_input("Left or Right? ")
	if direction == "left":
		how = '''"Crash!" The mountain starts to tremble. 
You realize too late that a boulder is heading your way.'''
		death(how)
	elif direction == 'right' and "stick" not in equipment:
		death("""You make it around a boulder.
		The peak is close now.
		Suddenly, something pounces on you.
		Yeah, that stick could have been really useful now.""")
	elif direction == 'right' and "stick" in equipment:
		print "You make it around a boulder."
		print "The peak is close now."
		print "Suddenly, something pounces on you."
		wolf_encounter()

def wolf_encounter():
	wolf_life = 6
	hit_point = 10
	print "You're able to fend off the initial attack with your stick."
	print "Before you is an angry wolf."
	print "It looks like it could attack at any moment."
	def wolf_battle_stats():
		print "Health: %d" % hit_point
		print "Wolf: %d" % wolf_life
	while wolf_life > 0 and hit_point >= 1:
		fight = raw_input("What is your next move? ")
		if 'charge' in fight:
			wolf_life -= 3
			hit_point -= 2
			print "You charge at the wolf."
			print "You're able to make a strong blow."
			print "The wolf also makes a gash on arm."
			wolf_battle_stats()
		elif "wait" in fight:
			wolf_life -= 4
			hit_point -= 1
			print "The wolf makes a lunge at you."
			print "It manages to claw your arm, but you land a strike to hits head."
			wolf_battle_stats()
		elif "quick" in fight or "swift" in fight:
			wolf_life -= 1
			hit_point -= 4
			print "You try to land a swift blow on the wolf."
			print "It glances the beast."
			print "The wolf sinks its teeth into your torso."
			print "You fend it off, but now you're bleeding pretty heavily."
			wolf_battle_stats()
		else:
			hit_point -= 10
			
		#life = hit_point
	if wolf_life <= 0 and hit_point >= 1:
		life.append[hit_points]
		print "With your final blow, you have bested the beast."
		print "You finally reach the peak of the mountain."
		peak()
	else:
		how = """The wolf senses your hesitation and lunges at you.
The rage in its eyes immobilizes you.
With a swift bite to the neck, you realize its all over."""
		death(how)

def peak():
	print "You can see the entire area from here."
	print "From the distance, you see that the river leads to an ocean."
	print ""
	print "What you thought was a house appears to be some form of ruins."
	print "Wait, is that smoke coming from there...?"




start()
