import unittest2 as unittest
from zope.component import getGlobalSiteManager
from collective.vocabularymanager.interfaces import IVocabularyRemovedEvent
from collective.vocabularymanager.interfaces import ITermRemovedEvent
from collective.vocabularymanager.interfaces import IVocabularyUtility
from collective.vocabularymanager.utility import VocabularyUtility
from collective.vocabularymanager.tests.base import VMTestCase


class MockVocabEventHandler(object):

    def __init__(self):
        self.object = None
        self.event = None

    def __call__(self, object, event):
        self.object = object
        self.event = event


class TestEvents(VMTestCase):

    def test_event_is_fired_when_vocabulary_deleted(self):
        event_handler = MockVocabEventHandler()
        gsm = getGlobalSiteManager()
        gsm.registerHandler(
            event_handler,
            (IVocabularyUtility, IVocabularyRemovedEvent),
            u'')
        util = VocabularyUtility()
        util.remove_vocab('vocab_id')
        self.failUnless(event_handler.event.vocab_id == 'vocab_id')

    def test_event_is_fired_when_term_deleted(self):
        event_handler = MockVocabEventHandler()
        gsm = getGlobalSiteManager()
        gsm.registerHandler(
            event_handler,
            (IVocabularyUtility, ITermRemovedEvent),
            u'')
        util = VocabularyUtility()
        util.remove_term('vocab_id', 'term_id')
        self.failUnless(
            event_handler.event.vocab_id == 'vocab_id',
            event_handler.event.term_id == 'term_id')


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEvents))
    return suite
