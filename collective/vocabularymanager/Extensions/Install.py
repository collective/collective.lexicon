from Products.CMFCore.utils import getToolByName
from zope.container.ordered import OrderedContainer

def install(self, reinstall=False):
    portal = getToolByName(self, 'portal_url').getPortalObject()
    if not hasattr(portal, '_vocabularies_'):
        portal._vocabularies_ = OrderedContainer()

def uninstall(self, reinstall=False):
    if not reinstall:
        ps = getToolByName(self, 'portal_setup')
