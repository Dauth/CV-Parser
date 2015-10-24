# CV-Parser

CustomClassJson
  call encodeClassToJson method with your custom class as an argument to encode it into json format
  call decodeJsonToClass method with json as an argument to decode it into custom class format
  saveFile and openFile is currently not used. Just for testing purposes since the project is not integrated. Edit it to your own liking.
  ***Require jsonpickle, json is optional
  
Current classes/Node to be passed around are
  1)JobDescNode
  2)ResumeNode
  ***Both inherit from InformationNode
  
MainController is to pass a json file to Parser NOT a path location to where the json file resides. Parser will decode it before parsing and encode it to return to Maincontroller
  ***All done locally
  
Parser will be using rule based matching for now
