# Jarad Aker

import graphics
import time
import random


WINDOW_WIDTH = 900
NUM_BAD_GUYS = 16


def loadGoodGuys(window):
    hero = graphics.Image(graphics.Point(200, 450), 'horseman-ne-attack6.gif')
    hero.draw(window)
    return hero

def loadBadGuys(window):
    yIndex = 70
    x = 1
    bgList = []
    for i in range (NUM_BAD_GUYS):
        bg = graphics.Image(graphics.Point(x*70+50, yIndex), 'ogre-attack1.gif')
        bgList.append(bg)
        bg.draw(window)
        x = x + 1
        if i == 7:
            yIndex = 140
            x = 1

    return bgList


def fire_shot(shot_list, hero,window):
        shot = graphics.Image(graphics.Point( 200, 375 ),'shot4.gif' )
        shot_list.append( shot )
        shot.draw( window)

def move_stuff(badGuys, hero, window):
    delta_x = 0
    delta_y = -5
    shot_list = []
    shotVel = 10
    bgVel = 10
    currNumBadGuys = NUM_BAD_GUYS
    currNumAttaker = 0
    counter = 0
    attackList = []
    gameRunning = True

    # Per Iteration
    # 1. Check to see if the user won
    # 2. Move the bad guys side to side every .05ms
    # 3. Choose a bad guy to drop every 60ms
    # 4. Move all dropping bad guys down every 2ms
    # 5. Check for user input and see if we need ot move hero
    while gameRunning:

        if currNumBadGuys == 0 and currNumAttaker == 0:
            print("YOU WIN")
            gameRunning = False

        else:
            if currNumBadGuys > 0:
                for i in range( currNumBadGuys ):
                    if badGuys[i].anchor.x <= 0 or badGuys[i].anchor.x >=WINDOW_WIDTH:
                        bgVel = -bgVel
                #first check if the bad guys are leaving the screen
                if badGuys[0].getAnchor().getX()-(badGuys[0].getWidth()/2) <= 0 or \
                    badGuys[currNumBadGuys-1].getAnchor().getX()+(badGuys[currNumBadGuys-1].getWidth()/2)>=WINDOW_WIDTH:
                    bgVel = -bgVel
                for bg in badGuys:
                    bg.move(bgVel,0)
                # Every 60ms we want to take a badGuy out of the line and move him down the screen
                if counter == 20:
                    # Get a random int that is between the lenght of the badGuys array
                    x = random.randint( 0, (len( badGuys ) - 1) )
                    # Subtract a bad guy from the total number of badGuys
                    currNumBadGuys = currNumBadGuys - 1
                    # badGuys[x].undraw()
                    # Add the chosen badGuy to an attach array, be be used in the move down
                    attackList.append( badGuys[x] )
                    # add to the current number of attackers
                    currNumAttaker += 1
                    # Remove the chosen badGuy from the badGuy array
                    badGuys.remove( badGuys[x] )
                    # Reset the counter to 0
                    counter = 0

            if currNumAttaker > 0:
                for i, e in reversed( list( enumerate( attackList ) ) ):
                    print(i)
                    if attackList[i].anchor.y > 500:
                        attackList[i].undraw()
                        attackList.remove(attackList[i])
                        currNumAttaker -= 1


           #next see if the hero needs to move
            key = window.checkKey()
            if key == 'Right':
                hero.move(8,0)
            elif key == 'Left':
                hero.move(-8,0)
            elif key == 'space':
                fire_shot(shot_list,hero,window)
            for shot in shot_list:
                shot.move(0,delta_y)
            # Move all the attacker down
            for i in range( len(attackList) ):
                attackList[i].move(0,5)

            # Throttle the while statement to only execute every .05ms
            time.sleep(0.05)
            counter = counter + 1
    # Show Score and Result
    # Add a You Win or You Lose Message

def main():
    win = graphics.GraphWin("Project 5 Start", WINDOW_WIDTH, 500)
    hero = loadGoodGuys(win)
    bgList = loadBadGuys(win)
    move_stuff(bgList, hero, win)



main()
