import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pi Representation: Circumference and Radius")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Circle parameters
center = (width // 2, height // 2)
radius = 200

# Fonts
font = pygame.font.Font(None, 36)

def draw_circle_and_radius(win, center, radius):
    # Draw the circle
    pygame.draw.circle(win, BLUE, center, radius, 2)
    
    # Draw the radius
    end_of_radius = (center[0] + radius, center[1])
    pygame.draw.line(win, RED, center, end_of_radius, 2)
    
    # Calculate the circumference
    circumference = 2 * math.pi * radius
    
    # Draw the circumference length visually as an arc
    for angle in range(0, 361, 1):  # Draw the full circle as small segments
        x = center[0] + radius * math.cos(math.radians(angle))
        y = center[1] + radius * math.sin(math.radians(angle))
        pygame.draw.circle(win, BLACK, (int(x), int(y)), 2)
    
    # Display the numeric values
    radius_text = font.render(f"Radius: {radius}", True, BLACK)
    circumference_text = font.render(f"Circumference: {circumference:.2f}", True, BLACK)
    
    win.blit(radius_text, (end_of_radius[0] + 10, end_of_radius[1] - 20))
    win.blit(circumference_text, (center[0] - radius - 50, center[1] + radius + 20))

    return circumference

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)  # Limit to 30 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        win.fill(WHITE)
        
        # Draw the circle and radius
        circumference = draw_circle_and_radius(win, center, radius)
        
        # Display Pi and the circumference/radius ratio
        pi_text = font.render(f"Pi (π) ≈ {math.pi:.6f}", True, BLACK)
        ratio_text = font.render(f"Circumference / Radius = {circumference / radius:.6f}", True, BLACK)
        
        win.blit(pi_text, (20, 20))
        win.blit(ratio_text, (20, 60))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
