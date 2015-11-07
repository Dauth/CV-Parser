__author__ = 'Owner'

from Controller import Controller
from Facade import Facade
from InformationNode import InformationNode
from MatchBox import MatchBox
from ResumeNode import ResumeNode
from CustomClassJson import encodeClassToJson
from CustomClassJson import decodeJsonToClass

#newResume = ResumeNode('dd', 'dd', 'ddd', 'ddd')
myController = Controller()
#myController.createNewJob('sfsdf','key words','{"dd": "ff"}')

#myController = Controller()
myController.createNewResume('John', '84554565468', 'sfsdf','dd','{"dd": "ff"}')

#myController = Controller()
#myController.createNewResume('John', '84554565468', 'sfsdf','dd','"{\"py/object\": \"ResumeNode.ResumeNode\", \"contentType\": \"RESUME\", \"experience\": [{\"py/object\": \"ExperienceSubNode.ExperienceSubNode\", \"workDuration\": \"february 2008  -  present \", \"workPosition\": \"senior software engineer  at   continental automotive group\"}, {\"py/object\": \"ExperienceSubNode.ExperienceSubNode\", \"workDuration\": \"january 2000  -  july 2007  \", \"workPosition\": \"senior associate engineer  at   singtel\"}], \"name\": \"desmond\", \"hpNumber\": \"97859875\", \"education\": {\"bachelor of computing\": \"national university of singapore\", \"bachelor of science (bsc), computer software engineering, 2010 - 2012\": \"oxford brookes university\"}, \"email\": \"desmond@gmail.com\", \"content\": [\"Desmond Lim\\nSenior Software Engineer at Continental Automotive Group\\n\\nSummary\\n\\nStrong interest in android app/game development.\\n\\nExperience\\nSenior Software Engineer  at   Continental Automotive Group\\nFebruary 2008  -  Present (7 years 9 months)\\n\\nWindows application developement\\n\\nSenior Associate Engineer  at   SingTel\\nJanuary 2000  -  July 2007  (7 years 7 months)\\n\\nMobile (GSM/3G) network optimization and enhancement\\n\\nPublications\\nApps/Games in Google Play\\nGoogle Play Store   January 1, 2010\\nAuthors: Desmond L.\\n\\nOptimized for Android version 2.3.3 and above. Suitable for small to large screen size.\\n\\nProjects\\nPublished app/games in Google Play\\n2010 to Present\\nMembers:Desmond L.\\n\\nDemonstrating skills: Multi-threading, Camera API, MySQL, UI, Android Animation\\n\\nLanguages\\nEnglish\\nChinese\\n\\nSkills & Expertise\\nAndroid Development\\nMobile Devices\\nWeb Development\\nSoftware Engineering\\nAndroid\\nSoftware Development\\n\\nPage1\\n\\n\\fSoftware Design\\nEclipse\\nEmbedded Software\\nObjective-C\\nObject Oriented Design\\nDebugging\\n\\nEducation\\nOxford Brookes University\\nBachelor of Science (BSc), Computer Software Engineering, 2010 - 2012\\nbachelor of computing\\nnational university of singapore\\n\\nPage2\\n\\n\\fDesmond Lim\\nSenior Software Engineer at Continental Automotive Group\\n\\nContact Desmond on LinkedIn\\n\\nPage3\\n\\n\\f\"], \"skillSet\": {\"py/set\": [\"web development\", \"software development\", \"android development\", \"software engineering\", \"mobile devices\", \"android\"]}}"')

myFacade = Facade()
#myFacade.getNewResumes()
#myFacade.getAllResumes()
#myFacade.getNewJobs()
#myFacade.getAllJobs()

#a = set()
#mb = MatchBox('d')
#a.add(mb)
#myFacade.storeMatchBoxes(a)
#r = dict()
#myFacade.storeResults(r)
        
