from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # score = cast.get_first_actor("scores") remove score from game
        
        # start change
        # food = cast.get_first_actor("foods")
        # end change

        cyclist = cast.get_first_actor("cyclist")
        segments = cyclist.get_segments()
        messages = cast.get_actors("messages")

        #start change
        cyclist2 = cast.get_second_actor("cyclist")
        segments2 = cyclist2.get_segments()
        messages2 = cast.get_actors("messages")
        #end change

        self._video_service.clear_buffer()

        # start change
        # self._video_service.draw_actor(food)
        # end change

        #start change
        self._video_service.draw_actors(segments)   # Cyclist 1
        self._video_service.draw_actors(segments2)  # Cyclist 2
        # self._video_service.draw_actor(score) remove score from game
        self._video_service.draw_actors(messages, True)   #Cyclist 1
        self._video_service.draw_actors(messages2, True)  #Cyclist 2
        self._video_service.flush_buffer()
        #end change
