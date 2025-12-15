# HackaGames - To Do list

## Hacka 0.5.1

Align Hackagames with hackapy0.5.1

[x] Make py421 tests working
[x] Make Connect4 tests working
[x] Make TicTacToe tests working
[x] Generate play, launch, connect and firstBot commands

## Shell games

[ ] Connect Bots with arguments (server, port)
[ ] With color (python rich)

## Game Zomb'Building

A game of exploration of infested building...

State :
┌╴ ╶─────┬╴ Hall(Deep)
│        │  Team    : 6 (score)     
│        │  Zombies : 3     
│      ◈ ◃  Danger  : 2
└────────┼╴ 

[ ] Create the new game squeletum (+ tutorial)
[ ] Set forward (enter a room), explo and back action mecanism (Kitchen, Armury or Nurcing appear only after a given deep)
[ ] Include zombies and fight action - potential zombie dependent on the room type (Hall, Corridor, Room, Office,Sters,...)
[ ] More actions: run-out, defend (fight entering zombie)
[ ] Labythinth (Left, right...)
[ ] Split action

Room : Name (Hall, Corridor, Room, Office, Kitchen, Stairs,...), deep, potential zombies, potential treasure, nb de-6, doors
 

Danger : Value/6
Team : number(6), 4/6
Zombies: number, 2/6

Action:
- fight/defend (fight x2, explo x 0),
- explore (fight x1, explo x 1),
- run-out (fight x0 / Zombie x 0.5),
- back    (fight x1 / Zombie x 1),

Charset:
┌───┐ ┌╴▿╶┐ ┌─┬─┐
│ ◈   ▹ ◈ ◃ ├   ┤     
└───┘ └╴▵╶┘ └─┴─┼



## Game C421
