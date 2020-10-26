@namespace
#https://arcade.makecode.com
class SpriteKind:
    Projectile2 = SpriteKind.create()

def on_a_pressed():
    global bubble
    bubble = sprites.create_projectile_from_sprite(img("""
            . 9 9 . 
                    9 1 . 8 
                    8 . . 8 
                    . 8 8 .
        """),
        fish,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

'''
def on_b_pressed():
    global splash
    if info.score() >= 250:
        splash = sprites.create_projectile_from_sprite(img("""
                9 9 . . 
                            . . 9 . 
                            . . . 9 
                            . . . 8
            """),
            fish,
            randint(60, 70),
            randint(-40, -60))
        splash = sprites.create_projectile_from_sprite(img("""
                . 9 . . 
                            . . 9 . 
                            . . . 8 
                            . . . 8
            """),
            fish,
            randint(65, 75),
            randint(-15, -35))
        splash = sprites.create_projectile_from_sprite(img("""
                . . 9 . 
                            . . . 9 
                            . . . 8 
                            . . 8 .
            """),
            fish,
            randint(70, 80),
            randint(-10, 10))
        splash = sprites.create_projectile_from_sprite(img("""
                . . . 9 
                            . . . 9 
                            . . 8 . 
                            . 8 . .
            """),
            fish,
            randint(65, 75),
            randint(15, 35))
        splash = sprites.create_projectile_from_sprite(img("""
                . . . 9 
                            . . . 8 
                            . . 8 . 
                            8 8 . .
            """),
            fish,
            randint(60, 70),
            randint(40, 60))
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)
'''

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.bubbles)
    info.change_score_by(10)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.bubbles)
    info.change_score_by(-10)
sprites.on_overlap(SpriteKind.Projectile2, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

angler: Sprite = None
splash: Sprite = None
bubble: Sprite = None
fish: Sprite = None
fish = sprites.create(img("""
        . . . . . b b b . . . . 
            . . . . b d 3 d b b . . 
            . b . b d d d 3 d 3 b . 
            c d b d d 1 1 d 1 d 3 b 
            c b 3 1 1 1 1 3 1 f d c 
            c 3 c 3 d d d 3 d d 3 c 
            . c . c 3 3 3 3 3 3 c . 
            . . . . c b d b c c . . 
            . . . . . c c c . . . .
    """),
    SpriteKind.player)
fish.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(fish, 200, 200)

def on_update_interval():
    info.change_score_by(1)
game.on_update_interval(1000, on_update_interval)

def on_update_interval2():
    global angler
    angler = sprites.create(img("""
            . . c c c c . . . . . . . . . . 
                    . c c . . c c . . . . . . . . . 
                    5 5 . . . . c c . . . . . . . . 
                    5 5 . . c c b c c c . . . . . . 
                    . . . c c b c b c b c . . c e . 
                    . c c b a c b c b b c . c c c e 
                    . d d c b c c b c c b c c c b e 
                    . . . d c b b c b b b c c b b e 
                    . . . d c b c b c c b c c b b e 
                    . d d c c b b c c b c c c c b e 
                    . c c c b c c b b c c . c c c e 
                    . . c c c b b c c c . . . e e . 
                    . . . . c c c c . . . . . . . .
        """),
        SpriteKind.enemy)
    angler.set_velocity(randint(-70, -90), randint(-30, 30))
    angler.set_position(180, randint(0, 120))
game.on_update_interval(500, on_update_interval2)
