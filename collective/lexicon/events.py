from zope.interface import implements
from collective.vocabularymanager.interfaces import ITermRemovedEvent
from collective.vocabularymanager.interfaces import IVocabularyRemovedEvent
from zope.component.interfaces import ObjectEvent


class TermRemovedEvent(ObjectEvent):
    implements(ITermRemovedEvent)

    def __init__(self, object, vocab_id, term_id):
        super(TermRemovedEvent, self).__init__(object)
        self.term_id = term_id
        self.vocab_id = vocab_id


class VocabularyRemovedEvent(ObjectEvent):
    implements(IVocabularyRemovedEvent)

    def __init__(self, object, vocab_id):
        super(VocabularyRemovedEvent, self).__init__(object)
        self.vocab_id = vocab_id
