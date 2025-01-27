# To-Do Map


## Pod -> Data 

- Data (typeXlen, values, children)
- DataType: 0:void, 1:str, 2:int32, 3:float32, 4:int64, 5:float64. 

## Map Structure

- Pod, a tuple < wording - integerValues - floatValues > rather than < family, status, flags, values >
- Map - asPod() - piecesAsPod() and piecesFromPod()
- Generic map structure: form tiledLand.
- Use it on Risky

## Integration

- Make it pip installable without clonning ?
- Make a generic connect command + autocompletion etc...
- Super command `hacka`

### View:

- View sub-package: Cairo based drawing functionnality.
- pyCairo base Artist class.
- Map view
- Test img ?

### Tutorials:

- Decition Tree..
- Connect4: Deep Learning + MCTS
- Optimization: MoveIt - Risky Zombi - or - new specific game ?

### Protocol:

- Uncoople Perception and Decision loop (perceive intermediate state, opponent combinaison for instance in Py421 Duo)
- Parrallelisation : Computation / Assimilate Perception (> bool last)

### New Games:

- **SpaceInvader**: Play versus the game (Perfect for Deep, optimization...) - restart until win.
- **MoveIt**: Pick-Up delivery problem.

### Project evolution:

- hackagames: meta command: hag or hk ...
- croupier + permanent web platform. (a first one on `ktorz.net`)

...

### Cleanup:

- Handle player or game interuption.
- Search for bash testing enviromnement (multi-process...) 
- reprendre les Tutos
- Capture signals
- Tests HackaPy interprocess.
- Revise doc structure with section/directories.
- Complete Tutos and set a first clean version (WebPage), WebPage Doc with no subterfuge

### hackalib:

- c based hacka client/server lib.
- gamec421 hackalib version of 421 game.

### Revice Load and Dump:

- Add a first control line, with a encoding and list of Pod families.

```pod
txt 3 Map Cell Pod
0 0 0 0 3 :
1 0 3 2 1 : 1 1 2 1.0 4.0
2 4 1 0 0 : Army 10
1 0 3 2 0 : 2 2 3 3.0 2.0
1 0 3 2 0 : 3 3 1 4.0 1.0
```

- Add bit encoding


### Going Futher:

- Map cell with 2D geometry 2D (coordinates, shape/radius, ...)

- Reinforcement-Learning:
	* Sleep with last perception elements or wake-up with first game state ?
	* perception including trace (event based variable modification)
- Complete HackaGames Py421 state (i.e. horizon = 0 wen `keep-keep-keep`, and modify stateStr in Q-Learning tutorials).
- Complete Tutos and set a first clean version (WebPage), WebPage Doc with no subterfuge

- TicTacToe: Terminate the tutorial.
- Initialize a `log` function in games and players to put the things potentially silent.
- HackaLib - C lib + gameC421 exemple (game421 -> gamePy421).
- Change `local` to `start` or `play` and pootentially `start` to `server`. Attention to change the documentation as well.
- Look at PAIO-promo2022-grp-vert code and their python based viewer...
- Initialize a move game (no crach, MAPF) or something like that.
- larger dice game - the return of zombie game ?
- Integrate a Game Engine (gestion des collision, rendu graphique....): Option: (Best Box2d - godot)
	+ RayLib (Simple...)
	+ Godot - https://en.wikipedia.org/wiki/Godot_(game_engine)
	+ ClanLib - https://github.com/sphair/ClanLib
	+ Delta3D - https://en.wikipedia.org/wiki/Delta3D
	+ ORX - https://orx-project.org/news/
	+ box2d.org
	+ FlatLand
	+ Cairo - https://en.wikipedia.org/wiki/Cairo_%28graphics%29
- Integrate ShapeFile format.

Aprés HackaGames se veux etre un game Engine a TDH engine (Two Dimension and a Half)

Q= {
    'end'= { 'kkk': 0, 'rkk': 0 .... },
    '4-2-1'= { 'kkk': 0, 'rkk': 0 .... },
    'X-2-1'= { 'kkk': 0, 'rkk': 0 .... },
    'X-1-1'= { 'kkk': 0, 'rkk': 0 .... },

    ...
 }

 168 X 8 : q-valeurs.
