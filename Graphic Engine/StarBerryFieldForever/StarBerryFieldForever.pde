// Created by Rômulo Vieira & Flávio Schiavoni. September, 2021 
// Inspired by The Coding Train code 
// GNU general public license 3

// Import modules that allow you to receive OSC messages 
import oscP5.*;
import netP5.*;
OscP5 osc;
// Setting variables that will receive OSC messages 
int a, b;

// Setting vector that creates stars and makes them disappear when they "leave the canvas" 
Star [] stars = new Star[800];

// Setting the speed variable 
float speed;

// Setting the setup function, used to set the initial properties of the environment 
void setup() {
  
  // OSC server
  osc = new OscP5(this, 12000);
 
    
  // Canvas size
  size(800, 800);
  // Loop that recreates the position of the stars
  for (int i=0; i<stars.length; i++) {
    // Indicates the new position for the star
    stars[i] = new Star();  
  }
}  

// Function that receives OSC messages
void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.addrPattern().equals("/speed")) {
    a = theOscMessage.get(0).intValue();
    b = theOscMessage.get(1).intValue();
  }
}

// Setting the function that will create the graphics in the environment 
void draw () {
  // Setting the speed at which the stars will move 
  speed = a;
  // Canvas background color
  background(0); // Set black clor
  // Moving the stars to the center 
  translate(width/2, height/2);
  // Loop that recreates the position of the stars
  for (int i=0; i<stars.length; i++) {
    // Update the position of the stars 
    stars[i].update();
    // Show the stars
    stars[i].show();
  }
}
