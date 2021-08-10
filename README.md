# Sunflower IoMusT Environment 🌻

The Internet of Musical Things (IoMusT) is an interdisciplinary field of study that emerges from the expansion of the concepts of the Internet of Things (IoT) into musical practice. Despite being a novelty, this area already has well-defined concepts and difficulties, whether those related to artistic practice or those related to socio-environmental issues. From a computational point of view, one of the biggest challenges concerns the lack of standardization and interoperability of this environment. 

In this context, the authors of this work propose the Sunflower, a protocol that aims to standardize communication in an IoMusT environment. To put its validity to the test, an environment was developed with a mode of operation similar to the Pipes-and-Filters architecture, where musical things behave like filters, communicating only from their input and output data. There is also a division into four layers, classified according to the objects, network and musical information exchange protocols, data and actors present in each one of them. 

Sunflower is still in the development stage, so programmers, designers, artists, musicians, composers and beta testers are welcome to join the club. 
Contact us: romulo_vieira96@yahoo.com.br 

If this code or environment was useful to you, consider donating on Paypal: romulo_vieira96@yahoo.com.br 

## Installation

Just run Python scripts in a terminal.


## How to Use

In the **“code”** directory are two files. One called **“management_screen.py” and one called “sunflower_cli.py”**. Although the second is capable of performing all the functions of the first, both can be performed simultaneously. The first file acts as an Open Sound Control (OSC) server, capable only of receiving messages from musical things. The second also receives messages from musical things, but is able to classify them into input and output information, in addition to connecting and disconnecting these objects without the need to contact them. 

The first command available in the Command Line Interface (CLI) is **input (-i)**. Just enter **“python3 sunflower_cli.py -i”** into the terminal and connect your musical thing to the network and the CLI only displays the object's input information. 

Similarly, the **output (-o)** command displays only the output information of musical things. To do this, enter the command **“python3 sunflower_cli.py -o”**. 

To connect a musical thing using the CLI, enter “python3 sunflower_cli.py -c IP:port” (i.e **“python3 sunflower_cli.py -c 224.0.0.0:3000**). The IP:port pair capable of receiving connections must be in the input information. This is the working protocol of Sunflower, where more information is available in the **“Publications”** repository. 

To disconnect, just follow the same pattern, just replacing the -c command with -d.

If you don't have musical things or patches on Pure Data, don't hesitate to use one of ours, as well as modify them to fit your artistic proposal. See more in the **“audio engine”** repository. 

**Here, some points should be highlighted:**
1) Due to the need to receive messages from the network, the CLI behaves like a server. Therefore, it MUST BE started before musical things connect to the network. Otherwise, even if connected, your information will not show up to the administrator, which can cause usability problems;

2) We recommend opening two terminals, each one executing a list command (-i or -o), so that the server is always open and updated when using the environment;

3) The -c and -d commands only accept one connection or disconnection at a time. And after performed, the script is closed. This is to avoid problems when trying to reach an IP or port that is already in use.

## License

GNU General Public License 3.0 – More info: https://www.gnu.org/licenses/gpl-3.0.en.html


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
