import graphics


def main():
    window = graphics.GraphWin("scrap", 500, 500)

    bg = graphics.Image(graphics.Point(400, 100), 'ogre-attack1.gif')
    bg.draw(window)
    L2xPos_bg = bg.getAnchor().getX() - bg.getWidth() / 2
    L2yPos_bg = bg.getAnchor().getY() - bg.getHeight() / 2
    R2xPos_bg = bg.getAnchor().getX() + bg.getWidth() / 2
    R2yPos_bg = bg.getAnchor().getY() + bg.getHeight() / 2
    l2 = bg.graphics.Point(L2xPos_bg, L2yPos_bg)
    r2 = bg.graphics.Point(R2xPos_bg, R2yPos_bg)
    hero = graphics.Image(graphics.Point(200, 300), 'horseman-ne-attack6.gif')
    hero.draw(window)
    L1xPos_hero = hero.getAnchor().getX() - hero.getWidth() / 2
    L1yPos_hero = hero.getAnchor().getY() - hero.getHeight() / 2
    R1xPos_hero = hero.getAnchor().getX() + hero.getWidth() / 2
    R1yPos_hero = hero.getAnchor().getY() + hero.getHeight() / 2
    l1 = hero.graphicsPoint(L1xPos_hero, L1yPos_hero)
    r1 = hero.graphicsPoint(R1xPos_hero, R1yPos_hero)

    if l1.getX() > r2.getX() or l2.getX() > r1.getX():
        return False
        # If one rectangle is above other
    if (l1.getY() > r2.getY() or l2.getY() > r1.getY()):
        return False
    return True  # we could use else but not really needed


    window.getMouse()

main()