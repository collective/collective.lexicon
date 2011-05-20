from collective.vocabularymanager.interfaces import IVocabularyUtility
from collective.vocabularymanager.events import TermRemovedEvent
from collective.vocabularymanager.events import VocabularyRemovedEvent
from zope.interface import implements
from zope.event import notify

class VocabularyUtility(object):
    implements(IVocabularyUtility)

    def add_term(self, vocab_id, term):
        pass

    def remove_term(self, vocab_id, term_id):
        notify(TermRemovedEvent(vocab_id, term_id))

    def get_vocab(self, vocab_id):
        pass

    def add_vocab(self, id, title):
        pass

    def remove_vocab(self, id):
        notify(VocabularyRemovedEvent(id))

    def order(self, vocab_id, order):
        pass
