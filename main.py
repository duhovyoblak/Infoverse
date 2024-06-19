#==============================================================================
#  Infoverse: main file
#------------------------------------------------------------------------------
import sys
sys.path.append('..\siqo_lib')

from   siqo_journal    import SiqoJournal

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


import gensim.models

from infoverse_corpus import InfvCorpus

#==============================================================================
# package's constants
#------------------------------------------------------------------------------


#==============================================================================
# package's tools
#------------------------------------------------------------------------------

#==============================================================================
# Functions
#------------------------------------------------------------------------------
if __name__ =='__main__':
    
    journal = SiqoJournal('InfVerse', debug=3)
    journal.I('Main start')

    sentences = InfvCorpus(journal, 'InfoVerse')
    model = gensim.models.Word2Vec(sentences=sentences)
    
    journal.O('Main end')
    
#==============================================================================
#                              END OF FILE
#------------------------------------------------------------------------------
