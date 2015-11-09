# CV-Parser
Requirements -? pip install -r requirements.txt
* http://spotlight.sztaki.hu/downloads/dbpedia-spotlight-0.7.jar
* http://spotlight.sztaki.hu/downloads/en_2+2.tar.gz
* 1) create a folder named dbpediaspotilight in your project folder
* 2) unzip both the tar.gz file and the jar file into the dbpediaspotlight folder
* 3) rename the en_2+2 folder to  en
* 4) rename jar file to just dbpediaspotlight.jar
* 5) open cmd in the dbpediaspotlight folder
* 6) type java -jar dbpediaspotlight.jar en http://localhost:2222/rest





CustomClassJson

 * call encodeclasstoJson method with your custom class an an argument to encode it into json format
 * call decodeJsonToClass method with json as an argument to decode it into custom class format
 * saveFile and openFile is currently not used. Just for testing purposes since the project is not integrated. Edit it to your own liking.
 * Require jsonpickle, json is optional


Current classes/Node to be passed around are
 * JobDescNode
 * ResumeNode
 * Both inherit from InformationNode

MainController (yusuf)
 * is to pass a json file to Parser NOT a path location to where the json file resides. Parser will decode it before parsing and encode it to return to Maincontroller
 * All done locally


Parser will be using rule based matching for now
