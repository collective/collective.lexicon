import unittest2 as unittest
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import login
from zope.configuration import xmlconfig
from plone.app.testing.layers import FunctionalTesting
from plone.testing import z2


class VocabularyManager(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # load ZCML
        import collective.vocabularymanager
        xmlconfig.file('configure.zcml', collective.vocabularymanager,
                       context=configurationContext)
        z2.installProduct(app, 'collective.vocabularymanager')

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'collective.vocabularymanager:default')

        # create admin user
        # z2.setRoles(portal, TEST_USER_NAME, ['Manager']) does not work
        # setRoles(portal, TEST_USER_NAME, ['Manager']) is not working either
        portal.acl_users.userFolderAddUser('admin',
                                           'secret',
                                           ['Manager'],
                                           [])
        login(portal, 'admin')

VM_FIXTURE = VocabularyManager()
VM_FUNCTIONAL_TESTING = FunctionalTesting(bases=(VM_FIXTURE,),
                                              name="VocabularyManager:Functional")
class VMTestCase(unittest.TestCase):
    layer = VM_FUNCTIONAL_TESTING
