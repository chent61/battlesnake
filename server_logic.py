import random
from typing import List, Dict

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""
def avoid_the_wall(my_head, possible_moves: List[str], board_height, board_width: List[str]) -> List[str]:
   if my_head["y"] == board_height - 1:
     possible_moves.remove("up")
   if my_head["y"] == 0:
     possible_moves.remove("down")
   if my_head["x"] == 0:
     possible_moves.remove("left")
   if my_head["x"] == board_width - 1:
     possible_moves.remove("right")
   return possible_moves

# def check_list(position, possible_moves:List[str]) -> List[str]:
#   if (position in possible_moves):
#     possible_moves.remove(position)
#   return possible_moves

def avoid_my_body(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str], board_height, board_width, my_neck) -> List[str]:
    for i in my_body:
       # possible_moves = ["up", "down", "left", "right"]
      if (i["x"] < my_head["x"]) or (my_head["x"] + 1 == 0) or (my_head["x"] == 0):  
        possible_moves.remove("left")
      if (i["x"] > my_head["x"]) or (my_head["x"] == (board_width - 1)) or (my_head["x"] + 1 == (board_width - 1)):
        possible_moves.remove("right")
      if (i["y"] < my_head["y"]) or (my_head["y"] + 1 == 0) or (my_head["y"] == 0): 
        possible_moves.remove("down")
      if (i["y"] > my_head["y"]) or (my_head["y"] == (board_height - 1)) or (my_head["y"] + 1 == (board_height - 1)):  
        possible_moves.remove("up")

    return possible_moves

   
def get_food(my_head: Dict[str, int], possible_moves: List[str]) -> List[str]:
    for i in possible_moves:
      if i["y"] == my_head["y"] + 1:  # my neck is left of my head
        possible_moves.clear()
        possible_moves.append("up")
      if i["y"] == my_head["y"] - 1:  # my neck is right of my head
        possible_moves.clear()
        possible_moves.append("down")
      if i["x"] == my_head["x"] + 1:  # my neck is below my head
        possible_moves.clear()
        possible_moves.append("right")
      if i["x"] == my_head["x"] - 1:  # my neck is above my head
        possible_moves.clear()
        possible_moves.append("left")

    return possible_moves


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    # print(f"All board data this turn: {data}")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    print(f"My BATTLESNAKE STARTS HERE")

    possible_moves = ["up", "down", "left", "right"]

    # Don't allow your Battlesnake to move back in on it's own neck


    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    board_height = data["board"]["height"]
    # print(f"My Battlesnakes height this turn is: {board_height}")

    board_width = data["board"]["width"]
    
    # possible_moves = avoid_the_wall(my_head, possible_moves, 
    # board_height, board_width)
    my_neck = my_body[1]
    possible_moves = avoid_my_body(my_head, my_body, possible_moves,board_height, board_width, my_neck)
    # possible_moves = get_food(my_head, possible_moves)

    # TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves} where x is {data['you']['body']}")

    return move
