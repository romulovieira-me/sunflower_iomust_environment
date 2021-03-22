/* 
Code created by Rômulo Vieira, March 2021
The code receives a message from Pure data in the OSC protocol. 
The final purpose of this code is to receive information from a Pure Data patch and inform that it is connected to the network. 
When the patch is disconnected, a goodbye message should also be shown. 
Free for use, alteration and distribution 
*/

// imports the library responsible for receiving messages in OSC 
import oscP5.*;
// imports the library that allows connection via network 
import netP5.*;

// oscP5 variable receives information from the OSC server 
OscP5 oscP5;
// variable that receives information from the machine trying to connect 
NetAddress myRemoteLocation;

// Function that defines the initial properties of the screen 
void setup() {
// Screen size. No information will be passed on to it, but it is mandatory for this language 
size(300,300);
// Sets frames per second 
frameRate(25);
// OSC server will be heard on multicast address, on the indicated port 
oscP5 = new OscP5(this, "239.255.255.250", 40000);
// indicates which network address and port number you will receive messages from 
myRemoteLocation = new NetAddress("239.255.255.250", 40000);
}

// Function that executes the block's functions continuously, until the program is terminated 
void draw() {
// Background Color
background(0);
}

// Function that receives OSC message 

//Receive Pure data message 
void oscEvent(OscMessage theOscMessage) {
// OSC message when connection is established 
if(theOscMessage.checkAddrPattern("/connected")==true) {
// Receives message in String format 
if(theOscMessage.checkTypetag("s")) {
// Status variable receives the message from Pure data 
String Status = theOscMessage.get(0).stringValue();
// Print message in the Processing terminal 
println(" status: "+Status);
// Indicates value returned from a function 
return;
}
}
// OSC message when connection is closed 
if(theOscMessage.checkAddrPattern("/disconnected")==true) {
// Receives message in String format 
if(theOscMessage.checkTypetag("s")) {
// Status variable receives the message from Pure data 
String Status = theOscMessage.get(0).stringValue();
// Print message in the Processing terminal 
println(" status: "+Status);
// Indicates value returned from a function 
return;
}
}

}
