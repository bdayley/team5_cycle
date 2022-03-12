# import constants (unused)

from game.casting.cast import Cast
# from game.casting.food import Food (removing food from the game)
# from game.casting.score import Score (removing score from the game)
from game.casting.cyclist import Cyclist
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
# from game.shared.color import Color  (unused) 
# from game.shared.point import Point  (unused)
  

def main():
    
    # create the cast
    cast = Cast()
    # Change start
    # cast.add_actor("foods", Food())
    # change ends
    
    # Change start 
    # adding two cylyst and two scores
    cast.add_actor("cyclist", Cyclist())
    cast.add_actor("cyclist", Cyclist())
    # cast.add_actor("scores", Score()) remove score
    # cast.add_actor("scores", Score())
    # Change ends
   
    # initiate the services
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # create the script
    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    # start the game
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()