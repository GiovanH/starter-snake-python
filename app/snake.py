import random

class ABCSnake():

    def __init__(self, data):
        super(ABCSnake, self).__init__()
        self.health = data['health']
        self.id = data['id']
        self.body = [(i['x'], i['y']) for i in data['body']]
        self.name = data['name']

        (self.x, self.y) = self.body[0]

    def place(self, board):
        self.board = board
        return self

    def direction(self, d):
        if d == "up":
            r = (self.x, self.y - 1)
        elif d == "down":
            r = (self.x, self.y + 1)
        elif d == "right":
            r = (self.x + 1, self.y)
        elif d == "left":
            r = (self.x - 1, self.y)

        else:
            raise AssertionError(("Not a real direction:", d))

        return r
        

class Board():

    def __init__(self, data):
        super(Board, self).__init__()
        self.width = data['width']
        self.height = data['height']

        self.food = data['food']
        self.snakes = [ABCSnake(d) for d in data['snakes']]

    def isSolid(self, check):
        (x, y,) = check
        print(x, y)
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return True
        for snake in self.snakes:
            for space in snake.body:
                if space == check:
                    return True
        return False


class MySnake(ABCSnake):

    def move(self):

        choices = []
        directions = ['up', 'down', 'left', 'right']
        for d in directions:
            if not self.board.isSolid(self.direction(d)):
                print(d, self.direction(d), "is safe")
                choices.append(d)

        # Don't do a 180, ever

        try:
            direction = random.choice(choices)
        except:
            raise
        return direction
