from zope.component import queryUtility
from zope.component import adapts
from plone.i18n.normalizer.interfaces import IURLNormalizer
from Products.GenericSetup.utils import XMLAdapterBase
from Products.GenericSetup.utils import exportObjects
from Products.GenericSetup.utils import importObjects
from Products.GenericSetup.interfaces import ISetupEnviron

from collective.lexicon.interfaces import IVocabularyManager


class VocabularyXMLAdapter(XMLAdapterBase):
    """export the vocab as xml"""

    adapts(IVocabularyManager, ISetupEnviron)
    _LOGGER_ID = 'lexicon'
    name = 'lexicon'

    def _exportNode(self):
        node = self._doc.createElement('vocabularies')
        node.appendChild(self._extractVocabs())
        self._logger.info('Vocabularies exported')
        return node

    def _extractVocabs(self):
        fragment = self._doc.createDocumentFragment()
        for vocab_id, vocab in self.context.storage.items():
            fragment.appendChild(self._extractVocabulary(vocab_id, vocab))
        return fragment

    def _extractVocabulary(self, vocab_id, vocab):
        child = self._doc.createElement('vocabulary')
        metadata = vocab._metadata
        child.setAttribute('title', metadata.get('title', ''))
        child.setAttribute('id', vocab.__name__)
        child.setAttribute('description', metadata.get('description', ''))
        child.setAttribute('sort', metadata.get('sort', ''))
        # add the terms
        for term_id, term_value in vocab.items():
            subnode = self._doc.createElement('item')
            subnode.setAttribute('key', term_id)
            subnode.setAttribute('value', term_value)
            child.appendChild(subnode)
        return child

    def _importNode(self, dom):
        """import vocabs

        TODO: This doesn't handle updates of items
        """
        id_gen = queryUtility(IURLNormalizer).normalize
        for vocabulary in dom.getElementsByTagName("vocabulary"):
            # We're going to make a simple dict-representation of the data
            vocab_title = vocabulary.getAttribute("title")
            vocab_id = vocabulary.getAttribute("id")
            if (not vocab_id or vocab_id is None) and vocab_title is not None:
                vocab_id = vocab_title
            normalized_id = id_gen(vocab_id)
            # XXX: need to check for title
            self.context.add_vocab(normalized_id, vocab_title)

            for item in vocabulary.getElementsByTagName("item"):
                # XXX: need to support key and value for term adding
                value = item.getAttribute("value")
                #key = item.getAttribute("key") or name_chooser(value)
                try:
                    self.context.add_term(normalized_id, value)
                except KeyError:
                    # XXX: fix me
                    pass


def import_vocabularies(context):
    """Import vocabulary settings from an XML file.
    """
    logger = context.getLogger('lexicon')
    util = queryUtility(IVocabularyManager)()
    logger.info('importing lexicon vocabularies')
    if util is not None:
        importObjects(util, '', context)


def export_vocabularies(context):
    """Export vocabulary settings as an XML file.
    """
    logger = context.getLogger('lexicon')
    util = queryUtility(IVocabularyManager)()
    logger.info('exporting lexicon vocabularies')
    if util is None:
        logger.info('Nothing to export.')
        return
    exportObjects(util, '', context)
