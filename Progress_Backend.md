Started work on project : 18.4.22

# COMMIT #1
Liran Friedman, 19.4.22
## Communication check went ok, all types of requests are functioning:
    - get, post, update, delete.
## users app should now be deleted and instead figure out how to use the built in django user.
    - should be much easier, with auto authentication and administration.
    - Structure of view functions in this model are preety good, i intend to keep using them.

## Thinking on how to create the model that will represent a game.

# COMMIT #2
Liran Friedman 20.4.22

## User model changed to django built in user:
    - Clean sign in form
    - password authentication
    - username is unique
    - update and delete method currently stopped working properly, i will need to implement it differently now.
    - this makes it hard to add new fields (** we need to add user score **),
        so probably this structure will change again and we will create a customUser which takes the benefits from django user and also can have new fields.
        * note - it is much more complicated, will improve when oother components are interacting well.
        
    - ** i had a question for Tamir about redirecting from back-end, should i have some html templates on the back-end server, 
        or is this bad architecture.
    
## Built models for saving games:
    - So we have the main data structure for the database basically figured out:
        USER --(one to many)--> GAME --(one to one for bridging gap)--> Board --(one to many[6])--> Attempt
    - Game has all game details - [won/lost, duration, secret(word)] and the relations : user (dad) board (child).
    - Board links to 6 attempts (children) and has game(dad).
    - Attempts have the number of attempt (1-6) and the word attempted, and the relation to board (dad).
    - All fields have id's.
    - Relations are defined and accessible both ways.
    - on delete of user, games will assign defaultly to guest user. (for now the username "guest").
        on delete of game (which is not expected) all connected items will cascade.

# COMMIT #3
Liran Friedman, 26.4.22

## New clean project:
    - no copy paste.
    - only relevant methods and imports.

## Game saving is now fully functional:
- all game components will be created with one 'POST' request carrying the following data:
            
          { game_id (int), 
            player_id (int),
            secret (str len=5), 
            duration (time), 
            won (bool)
            attempts: ["word1", "word2", "word3"..."word6"] }

## working on structuring the program:
  - for now, extracted some logic to games.helpers file.
  - for testing purposes, for now, the player list will always contain the first 10 players (by id)
  maybe it should be the 10 players with the highest score. need to think on how to do that.
  - serializers are cool

# COMMIT #4
Liran Friedman, 27.4.22

## Some nice improvements:
- game detail is now available both in /api/games/$ and in /api/players/$/games/$
- games list by player is displayed in api/players/$/games and all games displayed in api/games
- changes in data structure for save game request:

          { ** NO LONGER NEEDED game_id (int) **
            ** NO LONGER NEEDED player_id (int) **

            secret (str len=5), 
            duration (time), 
            won (bool)
            attempts: ["word1", "word2", "word3"..."word6"]
         ** score: (int) ADDED FIELD ** }

** To save a game from listed user, send request POST to /api/players/{player.pk}/games/ **

** To save a game from guest user, send request POST to /api/games/ **


## created new logic behind choosing game, board, and attempt id:
  - game id will now always be player_id * 1000 + no.game.
  - attempt id will be game_id * 10 + no.attempt.
  - so for now we can save 1000 games per player.

## Added score field to game model. player score now updates when a game is saved. (except for guest user).

## players_list now returns a list with the 10 players with the highest score (ordered by score).

## games list for now gives the last 10 games.

## ideas for next missions:
- provide what is needed to login and logout users from frontend.
- arrange views in view classes.
- provide views to access specific words.
- learn a "best practice" way to organize helper functions.
- we can not intervene in game id, and just get each player's games and reorder by game_id, still...:)

# COMMIT #5
Liran Friedman, 2.5.22

## Some nice improvements:

    - improved url files: no re_path, no ^$ tags.
    - all numbers given in url now work properly (before numbers greater than 9 did not respond)
    - deleted unused files. * "attempts/views.py", "boards/views.py" will be used in the near future.
    - split logic to helper files, created helper in main folder.
    - added routing of serialization errors back to view response. (logic - int return type always means save success)
    - added get_obj_or_404 shortcut.
    - added correct response status to all routes of all views.
    - removed all added logic for id, and all id fields in database models.
    automated pk fields will now be generated not just for the player model, but for all models.
    queries will remain untouched, still ordering is expected to remain chronological by default.
    all links and consequences were updated and are functioning properly.
    - in general, all current functionalities seem to be responding well.

## Some possible problems:
    - Since the user model changed to a custom one, some benefits were lost:
      password is no longer demanding. password is no longer hashed.
    - for now, in players, create player will be at "players/create/" while all other functions - 
      put, get, delete - are at "players/<player_id>".
      this is because i want to separate views into smaller functions, although, the way i define urls now, 
      i need a separate url for each function.
      this probably could be solved by switching to class based views, which i have started approaching.
    - get_absolute_url method is not used (player model).

# COMMIT #6
Liran Friedman, 2.5.22

## Some nice improvements:
    - fixed password validation for Player model. (using built in create_user method and changes in auth settings.)
    - added logic to check&save serializer helper : password validation, many, added args
    - changed create user logic to create_user built in method - provides hashing and password authentication.
    - added jwt tokens that are now available on "api/players/token/" and "api/players/token/refresh".

# COMMIT #7
Liran Friedman, 3.5.22
## Quick update:
    - notice strict mode was replaced with router (not yet used) in index.js.
    - added number of games to players list.
    - commit in order to close and merge this branch and open a new one for all work on auth.

#Working on production:
Liran Friedman, 7.5.22
- created new project in new venv
- changed user model and created admin
- secret key is now hidden.
- Project deployed successfully on heroku!