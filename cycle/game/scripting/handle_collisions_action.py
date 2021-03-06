import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        #Start change
        self._player = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over and self._player == 0:
            # start change
            # self._handle_food_collision(cast)
            # end change
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cyclist1 = cast.get_first_actor("cyclist")
        head1 = cyclist1.get_segments()[0]
        segments1 = cyclist1.get_segments()[1:]
        
      #   for segment in segments:
      #       if head.get_position().equals(segment.get_position()):
      #           self._is_game_over = True
      #           self._player = 1
        
        #start change - adding second cyclist
        cyclist2 = cast.get_second_actor("cyclist")
        head2 = cyclist2.get_segments()[0]
        segments2 = cyclist2.get_segments()[1:]
        
        for segment1 in segments1:
           for segment2 in segments2:
               # print("head1 pos, seg2 pos", head1.get_position().get_x(), head1.get_position().get_y(), \
                  # head2.get_position().get_x(), head2.get_position().get_y(), \
                  # segment2.get_position().get_x(), segment2.get_position().get_y())
               if head1.get_position().equals(segment2.get_position()) or \
                  head2.get_position().equals(segment1.get_position()):# or \
                  # head2.get_position().equals(head1.get_position()):
                  self._is_game_over = True
                  # print("collision")
                  break
                  #  self._player = 2


        #end change
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        if self._is_game_over: # and (self._player == 1 or self._player == 2):
            cyclist = cast.get_first_actor("cyclist")
            segments = cyclist.get_segments()
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            
            for segment in segments:
                segment.set_color(constants.WHITE)

            cyclist = cast.get_second_actor("cyclist")
            segments = cyclist.get_segments()
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            for segment in segments:
                segment.set_color(constants.WHITE)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
