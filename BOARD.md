# HackaGames - To Do list

## Hacka 0.5.1

Align Hackagames with hackapy0.5.1

[x] Make py421 tests working
[x] Make Connect4 tests working
[x] Make TicTacToe tests working
[ ] Generate play, launch, connect and firstBot commands
[ ] Connect Bot with arguments (server, port)

## Game ZomBuilding

Danger : Value/6
Team : number(6), 4/6
Room : Name (Hall, Corridor, Room, Office, Kitchen, Sters,...), deep, potential zombies, potential treasure, nb de-6, doors
Zombies: number, 2/6

Action:
- fight/defend (fight x2, explo x 0),
- explore (fight x1, explo x 1),
- forward (enter a room), 
- back    (fight x1 / Zombie x 1),
- run-out (fight x0 / Zombie x 0.5),

State :
last move : up/down/left/right
┌───┐ ┌╴▿╶┐ ┌─┬─┐      ┌┬
│ ◈   ▹ ◈ ◃ │   ├      ┼─┤     
└───┘ └╴▵╶┘ └─┴─┘      └─├┤┴┼
┌╴ ╶─────┬╴ Hall
│        │  Team    : 6     Treasure : 4
│        │  Zombies : 3     Danger   : 2
│      ◈ ◃  
└────────┴╴ 
[ ] Labythinth (Left, right...)
[ ] Split action
[ ] With color (python rich)

s
## Game C421
