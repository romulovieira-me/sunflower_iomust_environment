"""
Created by Rômulo Vieira & FLávio Schiavoni, July 2021.

The code offers a Command Line Interface responsible for receiving OSC messages 
and listing them according to their input and output data. 

Also, it allows you to connect or disconnect musical things to the network.

If this code/environment was useful to you, consider making a donation to PayPal: romulo_vieira96@yahoo.com.br 

GNU General Public License 3.0
Free for use, modification and distribution. 
"""

# Module that creates user-friendly and uncomplicated command line applications 
import argparse
# Pythonosc library module that does not require the sender and receiver of the message to be directly connected 
from pythonosc import dispatcher
# Pythonosc library module that imports a server capable of receiving messages in OSC format 
from pythonosc import osc_server
# Allows the creation of clients that send OSC messages following the UDP protocol 
from pythonosc.udp_client import SimpleUDPClient
# Build bundles capable of sending messages in OSC format 
from pythonosc import osc_message_builder
# Module that allows the use of regular expressions capable of specifying the rules in strings 
import re
# This module provides access to the BSD socket interface
import socket

# Creating list to receive "hello" messages
hello = []
# Creating list to receive "input" messages
entrada = []
# Creating list to receive "output" messages
saida = []


# Function that attach each message to the list
def getHello(address: str):
    # Append message - Add element to end of list 
    hello.append(address)


# Function that attach each message to the list
def getEntrada(address: str):
    # Append message - Add element to end of list 
    entrada.append(address)


# Function that attach each message to the list
def getSaida(address: str):
    # Append message - Add element to end of list 
    saida.append(address)


# Function that deletes messages from the list
def Goodbye(address: str):
    # Checking conditions for deleting an item from the list when it is disconnected from the network
    del_path = address.split("/")  # Divide the address
    del_idx = del_path[2]  # Checks delete requests
    for addr in hello:  # If the address bound to the socket contains the word "hello"
        he_list = addr.split("/")  # Divide the address
        search = he_list[2]  # Search for the word in the specified list
        if del_idx == search:  # If the ID number is the same as the one that was disconnected
            hello.remove(addr)  # Remove the item from the list
    for addr in entrada:  # If the address bound to the socket contains the word "input"
        ent_list = addr.split("/")  # Divide the address
        search = ent_list[2]  # Search for the word in the specified list
        if del_idx == search:  # If the ID number is the same as the one that was disconnected
            entrada.remove(addr)  # Remove the item from the list
    for addr in saida:  # If the address bound to the socket contains the word "output"
        sai_list = addr.split("/")  # Divide the address
        search = sai_list[2]  # Search for the word in the specified list
        if del_idx == search:  # If the ID number is the same as the one that was disconnected
            saida.remove(addr)  # Remove the item from the list



""" Creating the basic functionalities of the CLI and server """

# Checking the scope of execution. If you run the module directly, execute the function, if you import the module,
# don’t run it
if __name__ == "__main__":
    # Check the validity of the entered argument. That is, if the input data is accepted by the script
    parser = argparse.ArgumentParser(
        # Software name
        prog='sunflower',

        # Usage = How to use the software
        usage='''         --------------------------------------------------
                
                Select one of the available options to connect, disconnect,
                or list available devices, input and output ports. 
                
                --------------------------------------------------
                ''',

        # Description = Software description
        description='''
                
                --------------------------------------------------
               
                Description:
                IoMusT Environment that allows the connection of various musical things 
                from its IP address and port number 

                --------------------------------------------------
                
                ''',

        # Epilog = footnote
        epilog="@ Created by Romulo Vieira & Flavio Schiavoni - GNU General Public License 3.0",
        # Indicates that the description and epilog are already formatted correctly and should not be grouped into lines
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # Add help list
        add_help=True
    )
    # Setting the server IP
    parser.add_argument("--ip",
                        nargs='?',  # The number of command-line arguments that should be consumed
                        default="224.0.0.1",  # The IP must be from the multicast address of the local network
                        help="The ip to listen on")  # tip
    # Setting the server port
    parser.add_argument("--port",
                        nargs='?',  # The number of command-line arguments that should be consumed
                        type=int,  # The type to which the command-line argument should be converted
                        default=60000,  # Arbitrarily chosen number. It can be any free port on the computer
                        help="The port to listen on")  # tip
    # Setting -i command, responsible for listing the input information of musical things 
    parser.add_argument('-i',
                        '--input',
                        action='store_true', # If the option is specified, assign the value True to argument
                        help='list the input ports (read)',  # tip
                        dest="input") # Attribute name 
    # Setting -o command, responsible for listing the output information of musical things
    parser.add_argument('-o',
                        '--output',
                        action='store_true', # If the option is specified, assign the value True to argument
                        help='list output ports (write)',  # tip
                        dest="output") # Attribute name 
    # Setting -c command, responsible for connect devices
    parser.add_argument('-c',
                        '--connect',
                        type=str, # Type of command entered 
                        help='connect the client:port pair',  # tip
                        dest="connect") # Attribute name 
    # Setting -d command, responsible for disconnect devices
    parser.add_argument('-d',
                        '--disconnect',
                        type=str, # Type of command entered 
                        help='disconnect the client:port pair',  # tip
                        dest="disconnect") # Attribute name 

    # Analyzes the data entered and prints it on the screen, if they are valid
    args = parser.parse_args()
    
    """ print Pure Data messages on terminal """

    # Dispatcher maps OSC addresses to functions and calls the functions with the messages’ arguments.
    dispatcher = dispatcher.Dispatcher()
    
    """
    Dispatcher associates addresses with functions by storing them in a mapping;
    An address can contains wildcards as defined in the OSC specifications;
    Call the Dispatcher.map method with an address pattern and a handler callback function.
    
    """
    # Map the OSC messages to this function and call the functions that put them in lists
    dispatcher.map("/hello/*", getHello)  # Map /hello/* messages and call gethHello function
    dispatcher.map("/input/*", getEntrada) # Map /input/* messages and call getEntrada function
    dispatcher.map("/output/*", getSaida)  # Map /output/* messages and call getSaida function
    dispatcher.map("/goodbye/*", Goodbye)  # Map /goodbye/* messages and call Goodbye function

    # If the -c argument is chosen
    if args.connect:
        client_addr = str(args.connect) # Get argument -c parameter
        match = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', client_addr) # Validation IP:Port parameter - More info: https://docs.python.org/3/library/re.html
        if len(match) != 0: # The len() function returns the number of items in an object
            
            clientIP = match[0].split(":") # Split IP and PORT using colon (:)
            
            ip = str(clientIP[0]) # Get the IP address entered by the user
            port = int(clientIP[1]) # Get the port number entered by the user

            client = SimpleUDPClient(ip, port)  # Create a client that sends information to the defined IP and port 

            client.send_message("/connection", str(ip) + " " + str(port)) # Send the OSC message "/connection" to the defined IP and port 
            print("Successful Connection") # When the connection is successful, print this message on the screen 
            quit() # Ends communication
            
    # If the -d argument is chosen
    if args.disconnect:
        client_addr = str(args.disconnect) # Get argument -d parameter
        match = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', client_addr) # Validation IP:Port parameter
        if len(match) != 0: # The len() function returns the number of items in an object
            
            clientIP1 = match[0].split(":") # Define a new client, splitting IP and PORT using colon (:)
        
        ip1 = str(clientIP1[0]) # Get the IP address entered by the user
        port1 = int(clientIP1[1]) # Get the port number entered by the user
        
        client1 = SimpleUDPClient(ip1, port1) # Create a new client that sends information to the defined IP and port 

        
        client1.send_message("/disconnection", str(ip1) + " " + str(port1)) # Send the OSC message "/disconnection" to the defined IP and port 
        print("Closed connection") # When the connection is closed, print this message on the screen 
        quit() # Ends communication
        
    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher) # Create an OSC server on arbitrarily specified IP and port 

    while True:  # Starting server loop
        try:
            print("Serving on {}".format(server.server_address))  # While server is active, receive messages
            server.serve_forever() # Server receives messages until it is manually shut down 
        except KeyboardInterrupt:  # When interrupt key is triggered, end loop
            break  # Ends loop
    # If the chosen command is the input argument (-i)
    if args.input:
        print("\n")  # Print a blank line
        print(entrada)  # Print entrada list
    # If the chosen command is the output argument (-o)        
    if args.output:
        print("\n")  # Print a blank line
        print(saida)  # Print saida list
    # If no command is entered 
    if not args.input and not args.output:
        # Print the three lists                                    
        print("\n")  # Print a blank line
        print(hello)  # Print hello list
        print("\n")  # Print a blank line
        print(entrada)  # print entrada list
        print("\n")  # Print a blank line
        print(saida)  # print saida list
        print("\n")  # Print a blank line

    print("\n")  # Print a blank line
    while input("Do You Want To Continue? [y/n]") == "y":  # As long as the letter typed by the user is "y"
        print("\n")  # Print a blank line
        try:  # Try to do
            print("Serving on {}".format(server.server_address))  # While server is active, receive messages
            server.serve_forever() # Server receives messages until it is manually shut down 
        except KeyboardInterrupt:  # When the interrupt key is triggered
            if args.input:  # ... and when the chosen command is -i
                print(entrada)  # Print entrada list
            if args.output:  # but when chosen command is -o
                print(saida)  # Print saida list
            # If no command is entered
            if not args.input and not args.output:
                print("\n")  # Print a blank line
                print(hello)  # Print hello list
                print("\n")  # Print a blank line
                print(entrada)  # Print entrada list
                print("\n")  # Print a blank line
                print(saida)  # Print saida list
                print("\n")  # Print a blank line
        else:
            if args.connect:
                quit()  # If the key type is not "y", it terminates execution
