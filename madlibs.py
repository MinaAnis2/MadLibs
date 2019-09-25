import json
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tag import pos_tag, map_tag
from nltk.corpus import wordnet as words

class jsonReader:
    jsonFile = {}
    filename = ''
    def __init__(self, file):
        jsonReader.filename = file
        self.__dict__ = json.load(open(self.filename,'r'))
        
    def print(self):
        print(self.__dict__)

    def save(self):
        with open(jsonReader.filename,'w') as json_file:
            json.dump(self.__dict__, json_file)

    def update(self, dictionary):
        self.__dict__.update(dictionary)

    def get(self):
        return self.__dict__

    def getVal(self, key):
        return self.__dict__[key]

class madlibs:
    def __init__(self):
        self.passages = jsonReader('MadLibs.json')

class madlibPassage:
    def __init__(self, string):
        self.passage = self.prepNLTK(string)
        self.passage = list(self.passage)
        self.wordCounter = []
        i = 0
        for word in self.passage:
            self.wordCounter.append([i,word])
            i += 1
        self.organizeWords()

    def get(self):
        return self.passage

    def wc(self):
        return self.wordCounter

    def prepNLTK(self, string):
        tweet = TweetTokenizer()
        return nltk.pos_tag(tweet.tokenize(string))

    def organizeWords(self):
        self.verb = []
        self.noun = []
        self.pron = []
        self.adj = []
        self.adv = []
        simple = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in self.passage]
        i = 0
        for simp in simple:
            TAG = simp
            if (TAG[1] == 'VERB'): self.verb.append([TAG[0],i])
            if (TAG[1] == 'NOUN'): self.noun.append([TAG[0],i])
            if (TAG[1] == 'PRON'): self.pron.append([TAG[0],i])
            if (TAG[1] == 'ADJ'):  self.adj.append([TAG[0],i])
            if (TAG[1] == 'ADV'):  self.adv.append([TAG[0],i])
            i += 1
        
    def getTags(self):
        self.tags = [self.verb, self.noun, self.pron, self.adj, self.adv]
        return self.tags
