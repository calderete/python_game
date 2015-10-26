from sys import exit
from random import ranint


class Scene(object):

	def enter(self):
		print "This scene is not yet configured, needs sublclass"
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "/n-------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene)next_scene_name)

class Death(Scene):

	quips = [
	"You died.  You kinda suck at this.",
	"Your mom would be proud...if she were smarter",
	"Such a luser.",
	"I have a small puppy that is better at this."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class CentralCorridor(scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded you ship and destroyed"
		print "your entire crew.  Your are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an"
		print "escape pod."
		print "/n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body  He's blocking the door to the"
		print "Armor and abou to pull a weapon to blast you."

		action = raw_input("> ")

		if action = "shoot":
			print "Quick on the draw you yank our your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entireley. This"
			print "completely ruins his brandn new costume his mother bought him, which"
			print "makes him jly into a rage and blast you repeatedly in the face until"
			print "you are dead.  Then he eats you."
			return 'death'

		elif action = "dodge":
			print "Like a world class boxer you dodge, weave, slop and slide right"
			print "as the Gothon's blaster cranks a laser pase your head."
			print "In the middle of you artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "you wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you"
			return 'death'


class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass








				