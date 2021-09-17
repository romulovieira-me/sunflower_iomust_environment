// Creating class that generates stars 
class Star {
  // Setting X-axis
  float x;
  // Setting Y-axis
  float y;
  // Settin Z-axis
  float z;
  // Setting the color of the stars 
  color c = color(220,20,60);
  // Setting Pz axis, which will be the main one in the line (trail) of the star 
  float pz;
  
  // Creating Star Object 
  Star () {
    // Setting random values for the x, y, and z axes 
    x = random(-width, width);
    y = random(-height, height);
    z = random(width);
    pz = z; 
    // Fills the line (trail) with the same color as the star
    fill(c);
  }
  
  // Function that updates the position of the stars when they "leave the screen" 
  void update () {  
    z = z - speed;
    if (z < 1) {
      z = width;
      x = random(-width, width);
      y = random(-height, height);
      pz = z;
    }
  }
  
  // Function that displays stars on the screen 
  void show() {
    // Stars color
    fill(220,20,60);
    // No Stroke
    noStroke();

    
    float sx = map(x / z, 0, 1, 0, width); // Mapping the value 
    float sy = map(y / z, 0, 1, 0, height); // Mapping the value 
    
    // Changes the proportion of the size of stars from the moment they "appear" on the canvas to when they "disappear" 
    float r = map(z, 0, width, 16, 0);
    // Stars shape
    ellipse(sx, sy, r, r);
    
    // Creating the line (trail) of the star 
    float px = map(x / pz, 0, 1, 0, width);
    float py = map(y / pz, 0, 1, 0, height);
    
    // Star line (trail) color 
    stroke(220,20,60);
    // Line start and end positions 
    line(px, py, sx, sy);
    
  }
}
