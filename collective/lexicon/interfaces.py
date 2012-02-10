from zope.interface import Interface, Attribute
from zope.component.interfaces import IObjectEvent


class IVocabularyManager(Interface):

    def add_term(self, vocab_id, term):
        pass

    def remove_term(self, vocab_id, term_id):
        pass

    def get_vocab(self, vocab_id):
        pass

    def get_vocab_items(self, vocab_id):
        pass

    def add_vocab(self, id, title):
        pass

    def remove_vocab(self, id):
        pass

    def order(self, vocab_id, order):
        pass


class ITermRemovedEvent(IObjectEvent):
    vocab_id = Attribute(
        'The id of the vocabulary that the terms is being removed from')
    term_id = Attribute('The id of the term being removed')


class IVocabularyRemovedEvent(IObjectEvent):
    vocab_id = Attribute('The id of the vocabulary being removed')
