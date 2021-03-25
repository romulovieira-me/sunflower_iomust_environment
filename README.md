# Sunflower IoMusT Environment 🌻

The Internet of Musical Things (IoMusT) is an interdisciplinary field of study that expands the domains of the Internet of Things (IoT) for musical practice. Although it is a new area, it already has well-defined concepts and difficulties, such as environmental, social, and those inherent to security, privacy, and copyright. From a computational point of view, the biggest challenge concerns the lack of standardization in the environment, with the protocols, data types, and behavior of musical things not being well defined.

In this context, the Sunflower environment emerges. Making a relationship between the software architecture Pipes-and-Filters and the behavior of musical things, this work intends to define the basic design for musical practice using this concept. Thus, the network communication protocols (UDP), the musical information communication protocol (OSC), the type and specification of the audio (wav, 44100 Hz), and so on are established.

The environment also intends to accept the connection of different traditional or digital musical instruments, as well as patches created by the users themselves.

## Installation

Not done yet


## Usage

For prototyping and testing, Pure Data was used, both to simulate instruments and to allow them to send their data to the network. Pure Data is available for GNU / Linux, macOS, and Windows. The download can be performed at: https://puredata.info/downloads

To send data over the network, UDP was used. For that, it is necessary to install the mrpeach library in Pure Data.
In the PD itself, go to: Help -> search for externals
In the search bar, search for "mrpeach" and download the most current version.

The second library required is to allow video capture in Pure Data.
Again, in the PD, go to: Help -> search for externals
In the search bar, search for "gem" and download the most current version.

For the use of patches, the information is found within them 



## License



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
