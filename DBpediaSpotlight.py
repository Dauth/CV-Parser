__author__ = 'Owner'
import spotlight

def annotate(text):
    return spotlight.annotate('http://spotlight.sztaki.hu:2222/rest/annotate',
                                      text,
                                      confidence=0.30, support=30, spotter='Default')
    #return [i.get('surfaceForm') for i in annotation]


def candidate(text):
    annotation = spotlight.candidates('http://localhost:2222/rest/candidates',
                                            text,
                                            confidence=0.30, support=30, spotter='Default')
    return [i.get('name') for i in annotation]
