from collective.vocabularymanager.interfaces import ITermRemovedEvent, IVocabularyRemovedEvent

class TermRemovedEvent(object):
    implements(ITermRemovedEvent)
 
    def __init__(self, vocab_id, term_id):
        self.vocab_id = vocab_id
        self.term_id = term_id

class VocabularyRemovedEvent(ObjectEvent):
    implements(IVocabularyRemovedEvent)

    def __init__(self, vocab_id):
        self.vocab_id = vocab_id
