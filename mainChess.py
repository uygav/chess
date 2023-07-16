# this is our main driver file . it will be respobsible for handling user input and displaying the current gameState object.

import pygame as p 
import engineChess

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ["wR","wN","wB","wQ","wK","wB","wN","wR","bR","bN","bB","bQ","bK","bB","bN","bR"]
    for piece in pieces:
        IMAGES[piece] = p.transorm.scale(p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engineChess.GameState()   # gs = game state