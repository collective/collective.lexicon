from zope.interface import Interface, Attribute
from zope.component.interfaces import IObjectEvent


class IVocabularyUtility(Interface):

    def add_term(self, vocab_id, term):
        pass

    def remove_term(self, vocab_id, term_id):
        pass

    def get_vocab(self, vocab_id):
        pass

    def add_vocab(self, id, title):
        pass

    def remove_vocab(self, id):
        pass

    def order(self, vocab_id, order):
        pass


class ITermRemovedEvent(IObjectEvent):
    vocab_id = Attribute('')
    term_id = Attribute('')


class IVocabularyRemovedEvent(IObjectEvent):
    vocab_id = Attribute('')
