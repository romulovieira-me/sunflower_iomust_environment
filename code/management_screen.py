"""
Code created by Rômulo Vieira, March 2021
inspired and adapted from the standard code of the python-osc library, available at: https://pypi.org/project/python-osc/

The code causes a Pure data patch to send a message in OSC format to the multicast address of the local network.

The final object of this code is to verify when the patch connects to the network and when it disconnects

Free for use, alteration and distribution 
"""

# Module that creates user-friendly and uncomplicated command line applications 
import argparse

# Pythonosc library module that does not require the sender and receiver of the message to be directly connected 
from pythonosc import dispatcher
# Pythonosc library module that imports a server capable of receiving messages in OSC format 
from pythonosc import osc_server

# Creating the basic functionalities of the server, with IP and standard port 

# Checking the scope of execution. If you run the module directly, execute the function, if you import the module, don’t run it
if __name__ == "__main__":
  # Checks the validity of the past argument. That is, if the input data is accepted by the script
  parser = argparse.ArgumentParser()
  # setting the server IP
  parser.add_argument("--ip",
  # The IP must be from the multicast address of the local network 
      default="224.0.0.1", help="The ip to listen on") 
  # setting the server port     
  parser.add_argument("--port",
  # arbitrarily chosen number. It can be any free port on the computer.
      type=int, default=60000, help="The port to listen on")   
  # Analyzes the data entered and prints it on the screen, if they are valid    
  args = parser.parse_args()  
  # The dispatcher maps OSC addresses to functions and calls the functions with the messages’ arguments.
  dispatcher = dispatcher.Dispatcher() 
  #The dispatcher associates addresses with functions by storing them in a mapping
  # An address can contains wildcards as defined in the OSC specifications
  # Call the Dispatcher.map method with an address pattern and a handler callback function
  dispatcher.map("/hello", print, "Hello") # print Pure Data messages on terminal 
  dispatcher.map("/publish/thing", print) 
  dispatcher.map("/publish/input", print)
  dispatcher.map("/publish/output", print)
  dispatcher.map("/goodbye", print)

  # Establishing connection with OSC server
  server = osc_server.ThreadingOSCUDPServer(
  # Reading IP, port and received message   
      (args.ip, args.port), dispatcher)
  # Prints a message on the screen indicating acceptance of the connection. IP and port used are also displayed     
  print("Serving on {}".format(server.server_address))
  # Indicates which server will remain open until it is manually closed by the user 
  server.serve_forever()