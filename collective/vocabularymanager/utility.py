from collective.vocabularymanager.interfaces import IVocabularyUtility
from collective.vocabularymanager.events import TermRemovedEvent
from collective.vocabularymanager.events import VocabularyRemovedEvent
from zope.interface import implements
from zope.event import notify
from zope.app.component.hooks import getSite
from zope.container.ordered import OrderedContainer
from persistent.dict import PersistentDict


class VocabularyUtility(object):
    implements(IVocabularyUtility)

    def __init__(self):
        portal = getSite()
        if not hasattr(portal, '_vocabularies_'):
            setattr(portal, '_vocabularies_', OrderedContainer())
        self.storage = portal._vocabularies_

    def add_term(self, vocab_id, term):
        vocab = self.get_vocab(vocab_id)
        term_key = term #TODO: generate the key
        vocab[term_key] = term

    def remove_term(self, vocab_id, term_id):
        notify(TermRemovedEvent(self, vocab_id, term_id))

    def get_vocab(self, vocab_id):
        if vocab_id in self.storage:
            return self.storage.get(vocab_id)
        raise AttributeError('No vocabulary with %s id found' % vocab_id)
    
    def get_vocab_items(self, vocab_id):
        """ return a list of tuples (k,v)
        """
        vocab = self.get_vocab(vocab_id)
        if vocab is not None:
            return vocab.items()
        return list()

    def add_vocab(self, id, title):
        if id in self.storage:
            return
        self.storage[id] = OrderedContainer()
        setattr(self.storage[id],'_metadata',PersistentDict())
        self.storage[id]._metadata.setdefault('title',title)
        

    def remove_vocab(self, id):
        notify(VocabularyRemovedEvent(self, id))

    def order(self, vocab_id, order):
        pass
