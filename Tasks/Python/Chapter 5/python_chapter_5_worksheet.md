# 1. Explain how the computer coordinate system differs from the standard Cartesian coordinate system. There are two main differences. List both.

- 0-Y Coordinate wurde von unten nach oben verlegt
- Es wird auf den unteren-rechten Quadranten fokusiert nicht auf den oberen-rechten Quadranten

# 2. Before a Python Pygame program can use any functions like pygame.display.set_mode(), what two lines of code must occur first?

- import pygame
- pygame.init()

# 3. Explain how WHITE = (255, 255, 255) represents a color.

- (xxx, xxx, xxx) = RGB code
- 0: No color
- 255: Max color
- WHITE is a difinition of a color with RGB code

# 4. When do we use variable names for colors in all upper-case, and when do we use variable names for colors in all lower-case? (This applies to all variables, not just colors.)

- Upper: Constant (Not changable)
- Lower: Variable (Later changable)

# 5. What does the pygame.display.set_mode() function do?
- It is creating a display surface.
- This can be modified

# 6. What does this for event in pygame.event.get() loop do?

- It is getting all events and removes them from the queue

# 7. What is pygame.time.Clock used for?

- Is creating an object to help tracking time

# 8. For this line of code: (3 pts) - pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

# 8.1 What does screen do?
- Is the surface to be drawn on
# 8.2 What does [0, 0] do?
- X & Y coordinates of the surface (Start of line)
# 8.3 What does [100, 100] do?
- X & Y coordinates of the surface (End of line) 
# 8.4 What does 5 do?
- Width

# 9. What is the best way to repeat something over and over in a drawing?

- With a for-loop

# 10. When drawing a rectangle, what happens if the specified line width is zero?

- It will be filled

# 11. Describe the ellipse drawn in the code below. - pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

# 11.1 What is the x, y of the origin coordinate?
- x: 20, 20
- y: 250, 100
# 11.2 What does the origin coordinate specify? The center of the circle?
- 
# 11.3 What is the length and the width of the ellipse?
- Lenght: 230
- Width: 80

# 12. When drawing an arc, what additional information is needed over drawing an ellipse?

- start-angel
- stop-angle

# 13. Describe, in general, what are the three steps needed when printing text to the screen using graphics?

- Text information (color, size, ...)
- Stamp of text
- Coordinates, where to put text on screen

# 14. When drawing text, the first line of the three lines needed to draw text should actually be outside the main program loop. It should only run once at the start of the program. Why is this? You may need to ask.

- 

# 15. What are the coordinates of the polygon that the code below draws? - pygame.draw.polygon(screen, BLACK, [[50,100],[0,200],[200,200],[100,50]], 5)

- Points the polygon-border is following

# 16. What does pygame.display.flip() do?

- Is updating the display on the screen

# 17. What does pygame.quit() do?

- Closes pygame library

# 18. Look up on-line how the pygame.draw.circle works. Get it working and paste a working sample here. I only need the one line of code that draws the circle, but make sure it is working by trying it out in a full working program.

- python_chapter_5_worksheet.py
