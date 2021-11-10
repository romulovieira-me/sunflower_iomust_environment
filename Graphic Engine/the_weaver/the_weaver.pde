// Created by Rômulo Vieira & Flávio Schiavoni. September, 2021 
// Inspired by Mr Johnson Computing video 
// GNU General Public License 3

// Import modules that allow you to receive OSC messages 
import oscP5.*;
import netP5.*;
OscP5 osc;

// Setting variable that makes art go into Looping 
Boolean looping = true;
// Setting variable that indicates the direction of the line 
String direction = "DOWN";
// Setting variable that indicates the speed at which the line will be drawn 
float lineSpeed = 0.1;
// Setting X-axis variable 
float x;
// Setting Y-axis variable 
float y;
// Setting the alpha value for colors 
float alpha = 30;
// Setting colors variable
int cor1, cor2, cor3;

// Setting the basic structure of the canvas
void setup() {
  
  // OSC server
  osc = new OscP5(this, 12000);
  
  // Canvas size
  size(800, 800);
  // Setting X-axis
  x = width/2;
  // Setting Y-axis
  y = 0;
}

// Function that receives OSC messages
void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.addrPattern().equals("/cor1")) {
    cor1 = theOscMessage.get(0).intValue();
  }
  if (theOscMessage.addrPattern().equals("/cor2")) {
    cor2 = theOscMessage.get(0).intValue();
  }
  if (theOscMessage.addrPattern().equals("/cor3")) {
    cor3 = theOscMessage.get(0).intValue();
  }
}

// Setting the structures of the drawn elements 
void draw() {
  
  // Setting variable that guarantees screen randomness (lines are ugly at random points) 
  float r3 = random(-1, 1); // Random Number Parameters 
  
  // If the value of r3 is greater than 0.1 
  if (r3 < 0.1) {
    float r2 = random(1); // Set r2 to 1 
    float addition = random(-1,1); // Add to new random value between -1 and 1 
    // If r2 is greater than 0.5 
    if (r2 < 0.5) { 
      x += addition; // x = x + addition 
      // else
    } else {
      y += addition; // y = y + addition
    }
  }
  
  // Call drawLines function
  drawLines(x, y);
  // Setting Line Direction and Speed 
  if (direction == "DOWN") {
   y += lineSpeed; 
  } else if (direction == "LEFT") {
    x -= lineSpeed;
  } else if (direction == "UP") {
    y -= lineSpeed;
  } else if (direction == "RIGHT") {
    x += lineSpeed;
  }  
  
    // Setting Line Direction and Speed 
  if ( y > height) {
    y = height/2;
    x = width;
    direction = "LEFT";  
  } else if (y < 0) {
    y = height/2;
    x = 0;
    direction = "RIGHT"; 
  }
  
    // Setting Line Direction and Speed 
  if (x < 0) {
    y = height;
    x = width/2;
    direction = "UP"; 
  } else if (x > width) {
    y = 0;
    x = width/2;
    direction = "DOWN"; 
  }
}

// Function that draws the lines 
void drawLines(float x, float y) {
  float r = map(x, 0, width, 0, cor1); // Maps the r line colors 
  float g = map(y, 0, height, 0, cor2); // Maps the g line colors 
  float b = map(x + y, 0, width + height, 0, cor3); // Maps the b line colors 
  
  // Creating the colors and positions for the beginning and end of lines 
  stroke(r, g, b, alpha);
  // top-left
  line(0, 0, x, y);
  // top-right  
  line(width, 0, x, y);
  // bottom-left
  line(0,height,x,y);
  // bottom-right
  line(width, height, x, y);
  
  save("wallpaper.png");
  save("wallpaper.svg");
}
    
