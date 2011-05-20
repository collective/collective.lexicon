from zope.interface import implements
from collective.vocabularymanager.interfaces import ITermRemovedEvent
from collective.vocabularymanager.interfaces import IVocabularyRemovedEvent
from zope.component.interfaces import ObjectEvent

class TermRemovedEvent(ObjectEvent):
    implements(ITermRemovedEvent)

    def __init__(self, object, vocab_id, term_id):
        self.object = object
        self.vocab_id = vocab_id
        self.term_id = term_id


class VocabularyRemovedEvent(ObjectEvent):
    implements(IVocabularyRemovedEvent)

    def __init__(self, utility, vocab_id):
        self.object = object
        self.vocab_id = vocab_id
