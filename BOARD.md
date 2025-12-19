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


## PixGames

 [x] Initialize a Bi421 (Binary Image 421 game)
▐▀▀▀▜   █▀▀▀▀▀▀▀█  █▀▀▀▀▀▀▀█  █▀▀▀▀▀▀▀█  █▀▀▀▀▀▀▀█  █▀▀▀▀▀▀▀█  █▀▀▀▀▀▀▀█
▐▝  ▐   █ ▀     █  █       █  █ ▀   ▀ █  █ ▀   ▀ █  █  ▄    █  █       █
▐ ▝ ▐   █   ▀   █  █   ▀   █  █   ▀   █  █ ▀   ▀ █  █    ▄  █  █       █
▐  ▝▐   █     ▀ █  █       █  █ ▀   ▀ █  █ ▀   ▀ █  █       █  █       █
▝▀▀▀▀   ▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀
 [x] Implement a Binary rendering  ▘▝ ▀▖▗▘▙▚▛▜▝▞▟▄▌▐ ▐ █
 [ ] set a B.I. player shell 
 [ ] Introduce DeepRL with a tuto on [PPO](https://en.wikipedia.org/wiki/Proximal_policy_optimization).
 [ ] get action in the random order.
 [ ] Move BinIm. to hackapy rather than hackagames ?
 [ ] Activate Duo mode
 [ ] Set a frame on shell image

## Game Cofee Fleet

A Pick and Delivery under uncertainty...

```
☀    ☂ ╶───╴ B ╶───╴ 2      ☀☁☔
   ╱   ╲   ╱   ╲   ╱   ╲ 
│❰ ❱├──┤   ├───╴   ╶───╴   
   ╲   ╱   ╲   ╱   ╲   ╱
   │▂▅█├───╴ A ╶───┤ 1 │

 A:▕▅▏ 1 ☂ | B:▕█▏ 2         ▕▁▂▃▄▅▆▇█    - 1 2 ... 9 ♻  
                             0 2 4 6 8
```

1: 

[ ] Create the new game squeletum (+ tutorial).
[ ] Initialize quit, wait, move-1/6 actions.
[ ] Initialize quit, wait, move-1/6 actions.
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
│◖1◗  ▹◖1◗◃ ├   ┤
└───┘ └╴▵╶┘ └─┴─┼


## Game Zomb'Building

A game of exploration of infested building...

State :
┌╴ ╶─────┬╴ - Hall(4) -             | Required back action to get out.
│        │  Team    : 6 (12)        | Team size + score
│        │  Zombies : 3             | Nb of zombies
│     ◖1◗◃  Danger  : 2/6           | Probability to pop
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
│◖1◗  ▹◖1◗◃ ├   ┤     
└───┘ └╴▵╶┘ └─┴─┼

## Game C421




