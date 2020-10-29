scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleBlueCrystal, function (sprite, location) {
    game.over(true)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleRedCrystal, function (sprite, location) {
    game.over(false)
})
let myCorg = corgio.create(SpriteKind.Player)
myCorg.updateSprite()
myCorg.horizontalMovement()
myCorg.verticalMovement()
myCorg.follow()
tiles.setTilemap(tilemap`Level_0`)
