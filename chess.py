import pygame

pygame.init()

width, height = 600, 600
rows, cols = 8, 8
square = width // cols - 10

brown, white = (87, 16, 16), (250, 250, 250)

Win = pygame.display.set_mode((width, height))

# import black pieces
Black_Knight = pygame.transform.scale(pygame.image.load("black cavalier.jpg"), (square, square))
Black_King = pygame.transform.scale(pygame.image.load("black king.jpg"), (square, square))
Black_Pawn = pygame.transform.scale(pygame.image.load("black pawn.png"), (square, square))
Black_Rook = pygame.transform.scale(pygame.image.load("black rook.jpg"), (square, square))
Black_Queen = pygame.transform.scale(pygame.image.load("black queen.jpg"), (square, square))
Black_Bishop = pygame.transform.scale(pygame.image.load("black bishop.jpg"), (square, square))

# import white pieces
White_Knight = pygame.transform.scale(pygame.image.load("white cavalier.jpg"), (square, square))
White_King = pygame.transform.scale(pygame.image.load("white king.jpg"), (square, square))
White_Pawn = pygame.transform.scale(pygame.image.load("white pawn.jpg"), (square, square))
White_Rook = pygame.transform.scale(pygame.image.load("white rook.jpg"), (square, square))
White_Queen = pygame.transform.scale(pygame.image.load("white queen.jpg"), (square, square))
White_Bishop = pygame.transform.scale(pygame.image.load("white bishop.jpg"), (square, square))
