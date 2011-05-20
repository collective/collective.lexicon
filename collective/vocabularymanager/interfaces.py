from zope.interface import Interface, Attribute

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


class ITermRemovedEvent(Interface):
    vocab_id = Attribute()
    term_id = Attribute()

class IVocabularyRemovedEvent(Interface):
    vocab_id = Attribute()
