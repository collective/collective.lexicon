import unittest2 as unittest
from plone.testing.z2 import Browser
from plone.app.testing import login
from plone.app.testing import logout
from transaction import commit
from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.interface import Interface
import zope.event
from zope.component import getGlobalSiteManager
from collective.vocabularymanager.interfaces import IVocabularyRemovedEvent
from collective.vocabularymanager.interfaces import IVocabularyUtility
from collective.vocabularymanager.utility import VocabularyUtility
from collective.vocabularymanager.tests.base import VMTestCase
from zope.component.interface import provideInterface


class MockVocabEventHandler(object):

    def __init__(self):
        self.object = None
        self.event = None

    def __call__(self, object, event):
        self.object = object
        self.event = event


class TestVocabularyManager(VMTestCase):

    def test_event_is_fired_when_vocabulary_deleted(self):
        event_handler = MockVocabEventHandler()
        gsm = getGlobalSiteManager()
        gsm.registerHandler(
            event_handler,
            (IVocabularyUtility, IVocabularyRemovedEvent),
            u'')
        util = VocabularyUtility()
        util.remove_vocab('foo')
        self.failUnless(event_handler.event.vocab_id == 'foo')

    def test_storage_creation(self):
        self.failIf(hasattr(self.layer['portal'], '_vocabularies_'))
        vm = getUtility(IVocabularyUtility)
        vm()
        self.failUnless(hasattr(self.layer['portal'], '_vocabularies_'))


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVocabularyManager))
    return suite
