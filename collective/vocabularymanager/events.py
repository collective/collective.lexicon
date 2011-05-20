from zope.interface import implements
from collective.vocabularymanager.interfaces import ITermRemovedEvent
from collective.vocabularymanager.interfaces import IVocabularyRemovedEvent


class TermRemovedEvent(object):
    implements(ITermRemovedEvent)

    def __init__(self, vocab_id, term_id):
        self.vocab_id = vocab_id
        self.term_id = term_id


class VocabularyRemovedEvent(object):
    implements(IVocabularyRemovedEvent)

    def __init__(self, vocab_id):
        self.vocab_id = vocab_id
