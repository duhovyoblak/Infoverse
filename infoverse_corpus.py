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
    journal = None   # Pointer to global journal
    oids    = {}     # Zoznam objektov per objId     {objId: obj}
    alas    = {}     # Zoznam objektov per alias     {alias: obj}

    #--------------------------------------------------------------------------
    @staticmethod
    def infoAll():
        "Returns info about Objects"

        msg = []
        dat = {}
        

        #----------------------------------------------------------------------
        return {'res':'OK', 'msg':msg, 'dat':dat, 'obj':None}

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
        self.name    = name  # Unique object Id
        
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
print('InfvCorpus ver 0.01')

#==============================================================================
#                              END OF FILE
#------------------------------------------------------------------------------