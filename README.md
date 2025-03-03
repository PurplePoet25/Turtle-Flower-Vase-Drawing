# Turtle Flower Vase Drawing

## Description
This Python program uses the Turtle graphics library to create a colorful drawing of a blue vase with three red flowers. The program demonstrates object-oriented programming concepts and the use of the Turtle library for creating graphic designs.

## Features
* **Vase Drawing**: Creates a detailed blue vase using coordinate-based drawing
* **Flower Generation**: Draws red flowers with six rounded petals
* **Random Elements**: Incorporates randomization for stem length, thickness, and flower size
* **Pastel Background**: Sets up a pleasant pastel yellow background

## Visual Elements
* **Vase**: A blue vase drawn at the bottom of the screen
* **Flowers**: Three red flowers with varying sizes
* **Stems**: Green stems of different lengths and thicknesses
* **Background**: Lemon chiffon pastel yellow (#FFFACD)

## Implementation Details

### Functions
* `draw_vase()`: Creates a blue vase using a series of coordinates
* `draw_flower(x, y, scale)`: Draws a red flower with six petals at the specified location with the given scale
* `draw_stem(x, y, length, thickness)`: Creates a green stem starting at the specified position with customizable length and thickness

### Key Components
* **Screen Setup**: 800x800 pixel canvas with pastel yellow background
* **Randomization**: Uses the `random` module to vary stem length (80-120 units), thickness (5-10 units), and flower scale (1-1.5)
* **Positioning**: Carefully places flowers and stems to appear to originate from the vase

## Requirements
* Python 3.x
* Turtle graphics library (included in Python's standard library)

## How to Run
1. Save the code to a file (e.g., `flower_vase.py`)
2. Run the file using Python:
3. A window will open displaying the drawing
4. The program will finish when you close the window

## Customization Options
You can modify the code to customize various aspects:
* Change the vase color by modifying the `pen.color("blue")` line in the `draw_vase()` function
* Adjust the flower color by changing the `pen.color("red")` line in the `draw_flower()` function
* Modify the background color by changing the `screen.bgcolor("#FFFACD")` value
* Add more flowers by extending the `stem_origins` list with additional coordinates

## Author
Hasan Bukhari
