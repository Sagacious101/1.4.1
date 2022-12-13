from createhero import *
import os


os.system("cls")
player = make_hero(name="Искатель", money=1000000, mp_curret=10, mage=True, defense_base=1)

game = True
while game:
	visit_hub(player)
	




