import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(900, 680))
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()  # Close Window
            quit()  # End Pygame
