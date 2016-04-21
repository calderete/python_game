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

		elif action = "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgt nebhaz fur ubnfr, fur fvgf nebhaz gur ubhfr."
			print "while he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."

		else:
			print "DOES NOT COMPUTE"
			return 'central_corridor'


class LaserWeaponArmory(Scene):

	def enter(self):
		print "Your do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neurtron bomb in its container.  There's a keypad lock on the box"
		print "and you need the code to get the bomb out.  If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb.  The code is 3 digits."
		code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
		guess = raw_input("[keypad]> ")
		guesses = 0 

		while guess != code and guesses < 10:
			print "BZZZZZZZZEDDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print " bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock bzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print "Your burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship.  Each of them has an even uglier"
		print "clown costume than the last.  They haven't pulled their"
		print "weapons out yet, as they see the active bombunder your"
		print "arm and dont't want to set it off."

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.  Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb.  You die knowing they will probably blow up when"
			print "it goes off"
			return 'death'

		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it"
			print "and blast the lock so the Gothons can't get out"
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can"
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE"
			return 'the_bridge'


class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship despreately trying to make it to"
		print "the escape pod before the whole ship explodes.  It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference.  You get to the chamber with the escape pods, and"
		print "now need to pick one to take.  Some of them could be damaged"
		print " byt you don't have time to look.  There's 5 pods, which one"
		print "do you take?"

		good_pod = randint(1, 5)
		guess = raw_input("[pod #> ")

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass








				