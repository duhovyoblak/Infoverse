#==============================================================================
# Siqo class InfoVerse Corpus
#------------------------------------------------------------------------------
# from  datetime import datetime, timedelta

import  siqo_general     as     gen

from gensim.test.utils import datapath
from gensim import utils

#==============================================================================
# package's constants
#------------------------------------------------------------------------------
_VER    = '1.00'

STATES  = ['EMPTY', 'RAW DATA', 'CORPUS READY']

#==============================================================================
# package's variables
#------------------------------------------------------------------------------

#==============================================================================
# InfvCorpus
#------------------------------------------------------------------------------
class InfvCorpus:

    #==========================================================================
    # Static variables & methods
    #--------------------------------------------------------------------------

    #==========================================================================
    # Decorators
    #--------------------------------------------------------------------------
    def isNotEmpty():
        
        
    def isPrepared(:)

    #==========================================================================
    # Constructor & utilities
    #--------------------------------------------------------------------------
    #
    #
    #--------------------------------------------------------------------------
    def __init__(self, journal, name):
        "Calls constructor of InfvCorpus for respective content"

        self.journal = journal
        self.journal.I("InfvCorpus.constructor:")
        
        #----------------------------------------------------------------------
        # datove polozky triedy
        #----------------------------------------------------------------------
        self.name    = name       # Unique object Id
        self.state   = STATES[0]  # State of the corpus
        self.raws    = []         # List of raw data to be preprocessed
        self.corpus  = []         # Preprocessed corpus
        
        #----------------------------------------------------------------------
        # Update zoznamov a indexov
        #----------------------------------------------------------------------
        
        self.journal.O(f"{self.name}.constructor: done")

    #--------------------------------------------------------------------------
    def __str__(self):
        "Prints info about this object"

        toRet = ''
        for line in self.info()['msg']: toRet += line +'\n'

        return toRet

    #--------------------------------------------------------------------------
    def __iter__(self):
        """An iterator that yields sentences (lists of str)."""

        corpus_path = datapath('lee_background.cor')
        for line in open(corpus_path):
            # assume there's one document per line, tokens separated by whitespace
            yield utils.simple_preprocess(line)
        
        
    #--------------------------------------------------------------------------
    def info(self):
        "Returns info about this Object"

        dat = {}
        
        dat['name'] = self.name
        

        return {'res':'OK', 'msg':['InfvCorpus.info()'], 'dat':dat, 'obj':self}

    #--------------------------------------------------------------------------
    def clear(self):
        "Clear the corpus"
        
        self.journal.I(f"{self.name}.clear:")
        
        self.raws.  clear()
        self.corpus.clear()
        
        self.state = STATES[0]
        
        self.journal.O()
        
    #==========================================================================
    # Raw data API
    #--------------------------------------------------------------------------
    def rawsFromPath(self, path):
        "Reads raw data from path"
        
        self.journal.I(f"{self.name}.rawsFromPath: path = '{datapath}'")
        
        #----------------------------------------------------------------------
        # Clear the corpus
        #----------------------------------------------------------------------
        self.clear()
        
        #----------------------------------------------------------------------
        # Load raws from the path
        #----------------------------------------------------------------------
        corpus_path = datapath('lee_background.cor')
        
        for line in open(corpus_path):
            
            self.raws.append(line)
            
        self.state = STATES[1]
        
        #----------------------------------------------------------------------
        self.journal.O(f"{self.name}.rawsFromPath: {len(self.raws)} lines was loaded")

    #--------------------------------------------------------------------------

    #==========================================================================
    # API
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    def toJson(self):
        "Converts Object into json structure"
        
        self.journal.I(f"{self.name}.toJson:")
        
        toRet = {}

        self.journal.O(f"{self.name}.toJson: Done")
        return toRet

#------------------------------------------------------------------------------
print(f"InfvCorpus ver {_VER}")

#==============================================================================
#                              END OF FILE
#------------------------------------------------------------------------------