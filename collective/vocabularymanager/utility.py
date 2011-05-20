from collective.vocabularymanager.interfaces import IVocabularyUtility
from collective.vocabularymanager.events import TermRemovedEvent
from collective.vocabularymanager.events import VocabularyRemovedEvent
from zope.interface import implements
from zope.event import notify
from zope.app.component.hooks import getSite
from zope.container.ordered import OrderedContainer


class VocabularyUtility(object):
    implements(IVocabularyUtility)

    def __init__(self):
        portal = getSite()
        if not hasattr(portal, '_vocabularies_'):
            setattr(portal, '_vocabularies_', OrderedContainer())
        self.storage = portal._vocabularies_

    def add_term(self, vocab_id, term):
        pass

    def remove_term(self, vocab_id, term_id):
        notify(TermRemovedEvent(self, vocab_id, term_id))

    def get_vocab(self, vocab_id):
        pass

    def add_vocab(self, id, title):
        pass

    def remove_vocab(self, id):
        notify(VocabularyRemovedEvent(self, id))

    def order(self, vocab_id, order):
        pass
