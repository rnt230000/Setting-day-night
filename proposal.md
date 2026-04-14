# Title
- Day and Night

## Repository
https://github.com/rnt230000/Setting-day-night

## Description
- The user will have the ability to make the environment turn day or night. 

## Features
- pygame.mouse
	- A standard module used to track and control the mouse device.
 	- Main focus:
  		- pygame.mouse.get_pos()
    		- Returns the x & y coordinates of your mouse.
      	- pygame.mouse.get_press()
      		- Returns a sequence of booleans representing the state of all the mouse buttons.
      	 	- It tracks whether a button from the mouse is being pressed or not.
- blit()
	- Will put an image or draw anything on a surface
- blend()
	- Will blend two images together. 

## Challenges
- Learned that tkinter and pygame cannot work together. Need to learn how to make a button work using PyGame.
- Getting the colors to change to another color after clicking the button without any possible errors or crashes.
- Might need research to see if it's possible to use the blend() function for pygame to create a lighting or darkening effect.

## Outcomes
Ideal Outcome:
- After executing the code, a window will open showing a landscape with 2 buttons (day, night). If I select a button that says "night", then the background color will slowly transition to black, along with the images getting darker to fit the mood of "nighttime." If I press the button that says "day," the opposite will happen. The black background will slowly transition to cyan as the images will look brighter.

## Milestones

- Week 1 (April 14-20th)
  1. Goal 1 (Background)
	  	- Create a window.
	  	- Add PNG images of the ground and clouds onto the surface.
	  	- Create 2 surfaces
	  		- One for the water.
	  		- One for the background. 
  2. Goal 2 (Buttons)
		- Create 2 buttons
	 		- One with a text that says "Day."
	   		- One with a text that says "Night."

- Week 2 (April 21-27th)
  1. Goal 1 (Buttons)
	    - Making the buttons able to be pressed.
  			- Making use of pygame.mouse.
     		- Test to see if they work.
  2. Goal 2 (Background color change)
     	- Step 1: Make a code that can switch between two colors.
     	- Step 2: Make it happen upon pressing the buttons.

- Week 3 (April 28th - May 4th)
  1. Goal 1 (Animated blended image)
     	- Make the PNG images look darker using the blend() function if the user clicks on the "night" button.
  2. Goal 2 (Button)
 		- Make it happen upon pressing the buttons
  
- Week 4 (May 5-11th)
  1. Goal 1 (Add stars)
     	- Make it so that every time the background turns back, the stars will become non-transparent.
     	- Make it fully transparent if the background is cyan.
