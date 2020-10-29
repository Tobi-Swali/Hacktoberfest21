def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile2)

myCorg = corgio.create(SpriteKind.player)
myCorg.update_sprite()
myCorg.horizontal_movement()
myCorg.vertical_movement()
myCorg.follow()
tiles.set_tilemap(tilemap("""
    Level_0
"""))