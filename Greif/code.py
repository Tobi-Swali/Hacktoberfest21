def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    crop.set_position(randint(10, 160), randint(10, 120))
    info.start_countdown(5)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

crop: Sprite = None
scene.set_background_color(15)
greif = sprites.create(img("""
        . . . . . f f f f f f . . . . . 
            . . . f f f 5 5 5 5 f f f . . . 
            f f f f 2 f f 5 5 f f 2 f f f f 
            f 6 f 2 2 2 f f f f 2 2 2 f 6 f 
            f 6 f f 2 2 2 f f 2 2 2 f f 6 f 
            f f 6 f f 2 f f f f 2 f f 6 f f 
            f f f f f f f 4 4 f f f f f f 8 
            f 8 f f a f 4 4 4 4 f a f f 8 f 
            f f 8 f a f f 4 4 f f a f 8 f f 
            . f f f a a f 4 4 f a a f f f . 
            . . f f f a f f f f a f f f . . 
            . . f c f a a f f a a f c f . . 
            . . f c f f a a a a f f c f . . 
            . . f c c f f f f f f c c f . . 
            . . f c c f f . . f f c c f . . 
            . . f f f f . . . . f f f f . .
    """),
    SpriteKind.player)
crop = sprites.create(img("""
        . e e e e . 
            e d e e e e 
            . e d d e .
    """),
    SpriteKind.food)
controller.move_sprite(greif)
greif.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
crop.set_flag(SpriteFlag.STAY_IN_SCREEN, True)