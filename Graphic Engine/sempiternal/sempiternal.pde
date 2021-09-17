// Created by Rômulo Vieira & Flávio Schiavoni. September, 2021 
// Inspired by thedotisblack creative coding video
// GNU general public license 3

// Import modules that allow you to receive OSC messages 
import oscP5.*;
import netP5.*;
OscP5 osc;

// Setting X-axis variable 
float x = 400;
// Setting Y-axis variable 
float y = 400;
// Setting angle variable value 
float angle = 90;
// Setting the diameter of the circle 
float dia = 20; 
// Setting environment color variables and their initial values 
int cor_de_fundo = #4F0D97, cor_das_linhas = #08E75C, preenchimento_elipses = #08E75C, cor_elipses = #08E75C; 

// Setting the basic properties of the canvas
void setup(){
  
  // OSC Server
  osc = new OscP5(this, 12000);
  
  // Canvas size
  size(800, 800);
}

 // Function that receives OSC messages
void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.addrPattern().equals("/corfundo")) {
    cor_de_fundo = theOscMessage.get(0).intValue();
   
  }
  if (theOscMessage.addrPattern().equals("/corlinhas")) {
   cor_das_linhas = theOscMessage.get(0).intValue();
    
  }
  if (theOscMessage.addrPattern().equals("/preenchimento")) {
    preenchimento_elipses = theOscMessage.get(0).intValue();
    
  }
  
  if (theOscMessage.addrPattern().equals("/corelipse")) {
    cor_elipses = theOscMessage.get(0).intValue();
    
  }

}

// Setting the properties of the drawn elements 
void draw() {
  // Setting canvas background color 
  background(cor_de_fundo);
  // Centering the circle's origin 
  translate(width/2, height/2);
  // Setting rotation movement for all elements 
  rotate(radians(14.3+angle/3));
  // Creating Line Rotation 
  for (float a=0; a<360; a+=10) {
  // Starting rotation (angle = 0) 
  pushMatrix();  
  
  // Intro effect
  if (angle<360) rotate(radians(a)*cos(radians(angle)));  
  else rotate(radians(a));
  // LInes color
  stroke(cor_das_linhas);
  // Lines weight
  strokeWeight(3);
  // Adding movement to lines 
  line(x*sin(radians(angle)), 0, 0, y-dia/2); // Avoid overlapping lines 
  
  // Creating smaller ellipses 
  
  // No Stroke
  noStroke();
  // Filling in the ellipses  
  fill (preenchimento_elipses);
  // Add ellipses to the end of each line 
  ellipse(x*sin(radians(angle)), 0, dia/2, dia/2);
  
  // Creating bigger ellipses 
  
  // Ellipse color 
  stroke(cor_elipses);
  // No fill
  noFill();
  // Ellipse coordinates (to give a sense of movement) 
  ellipse(0, y, dia, dia);
  popMatrix();
}
// Once the rotation is complete, add 1 to the angle and rotate again 
angle++;
}
