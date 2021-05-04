"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
added some functions for the BreakOut game
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved, onmousedragged
import random

# constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title='Breakout')

        # Element score label
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))

        # Element for game winning
        self.win_show = GLabel('Create by Mike Lin', x=100, y=100)
        self.win_show2 = GLabel('March 20 stanCode SC101', x=135, y=115)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset)
        self.window.add(self.paddle)
        self.paddle.filled = True

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius, x=window_width/2 - ball_radius,
                          y=window_height/2 - ball_radius)
        self.ball_x = window_width/2 - ball_radius
        self.ball_y = window_height/2 - ball_radius

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Other variables
        self.total_bricks = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)  # using own method must add 'self.' in the front
        onmouseclicked(self.clicked)
        self.draw_bricks_and_ball()

    def draw_bricks_and_ball(self):
        """
        set the bricks and balls
        """
        self.window.add(self.score_label, x=0, y=15)
        self.window.add(self.ball)
        self.ball.filled = True
        color_num = BRICK_COLS / 5
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                if j // color_num == 0:
                    color = 'red'
                elif j // color_num == 1:
                    color = 'orange'
                elif j // color_num == 2:
                    color = 'yellow'
                elif j // color_num == 3:
                    color = 'green'
                else:
                    color = 'blue'
                bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.window.add(bricks, x=0+i*(BRICK_WIDTH+BRICK_SPACING),
                                y=BRICK_OFFSET+j*(BRICK_HEIGHT+BRICK_SPACING))
                bricks.filled = True
                bricks.fill_color = color
                self.total_bricks += 1

    def paddle_move(self, m):
        """
        :param m: mouse you move
        this function controls the moving of the paddle and prevents it from disappearing
        """
        if self.paddle.width/2 <= m.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = m.x - self.paddle.width/2
        elif m.x >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif m.x < 0:
            self.paddle.x = 0

    def clicked(self, m):
        """
        the boolean that controls the start of the game once you clicked the mouse
        """
        if (self.ball.x, self.ball.y) == (self.ball_x, self.ball_y):
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def set_ball_direct(self):
        """
        to set the ball's direction and the action the ball takes when hitting the walls, bricks, paddle
        """
        self.ball.move(self.__dx, self.__dy)
        self.meet_the_wall()
        if self.meet_object() is self.paddle:
            self.__dy = -abs(self.__dy)
        elif self.meet_object() is self.ball:
            pass
        elif self.meet_object() is self.score_label:
            pass
        elif self.meet_object() is not None:
            self.window.remove(self.meet_object())
            self.__dy *= -1
            self.total_bricks -= 1
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)
            if self.total_bricks == 0:
                self.ball.x = self.ball_x
                self.ball.y = self.ball_y
                self.window.add(self.win_show)
                self.window.add(self.win_show2)
                self.win_show.font = '-30'

    def meet_the_wall(self):
        """
        the function that determines the ball's vy
        """
        if self.ball.x <= 0:
            self.__dx *= -1
        elif self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        elif self.ball.y <= 0:
            self.__dy *= -1
        elif self.ball.y + self.ball.height >= self.window.height:
            self.__dx = 0
            self.__dy = 0

    def dead(self):
        """
        to set the ball to start point when falling under the bottom window
        """
        if self.ball.y + self.ball.height >= self.window.height:
            self.ball.x = self.ball_x
            self.ball.y = self.ball_y
            return True

    def meet_object(self):
        """
        the detector for checking what the ball hits
        :return: the obstacle that ball hits
        """
        obstacle1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obstacle2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obstacle3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        obstacle4 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if obstacle1 is not None and not self.ball:
            return obstacle1
        elif obstacle2 is not None:
            return obstacle2
        elif obstacle3 is not None:
            return obstacle3
        elif obstacle4 is not None:
            return obstacle4
        else:
            return None

    def get_dx(self):
        """
        to get dx speed
        :return: dx speed
        """
        return self.__dx

    def get_dy(self):
        """
        to get dy speed
        :return: dy speed
        """
        return self.__dy
