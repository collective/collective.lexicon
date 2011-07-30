import unittest2 as unittest
from zope.component import getUtility
from collective.vocabularymanager.interfaces import IVocabularyManager
from collective.vocabularymanager.tests.base import VMTestCase
from zope.container.ordered import OrderedContainer


class TestVocabularyManager(VMTestCase):

    def test_storage_creation(self):
        self.failIf(hasattr(self.layer['portal'], '_vocabularies_'))
        vm = getUtility(IVocabularyManager)
        vm()
        self.failUnless(hasattr(self.layer['portal'], '_vocabularies_'))

    def test_add_vocab(self):
        vm = getUtility(IVocabularyManager)
        vocab_tool = vm()
        vocab_tool.add_vocab('vocab1', 'vocabulary1')
        test_vocab = vocab_tool.storage.get('vocab1')
        self.failUnless(test_vocab._metadata['title'] == 'vocabulary1')
        self.failUnless(isinstance(test_vocab, OrderedContainer))

    def test_get_empty_vocab(self):
        vm = getUtility(IVocabularyManager)
        vocab_tool = vm()
        vocab_tool.add_vocab('vocab1', 'vocabulary1')
        test_vocab = vocab_tool.get_vocab_items('vocab1')
        self.assertEqual(test_vocab, [])

    def test_get_vocab(self):
        vm = getUtility(IVocabularyManager)
        vocab_tool = vm()
        vocab_tool.add_vocab('vocab1', 'vocabulary1')
        # TODO: test unicode values!
        vocab_tool.add_term('vocab1', 'term_value')
        test_vocab = vocab_tool.get_vocab('vocab1')
        self.assertEqual(len(test_vocab), 1)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVocabularyManager))
    return suite
