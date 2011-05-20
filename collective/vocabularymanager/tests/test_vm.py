import unittest2 as unittest
from zope.component import getUtility
from collective.vocabularymanager.interfaces import IVocabularyUtility
from collective.vocabularymanager.tests.base import VMTestCase


class TestVocabularyManager(VMTestCase):

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
