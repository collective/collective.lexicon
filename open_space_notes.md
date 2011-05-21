# Vocabulary Manager redux

Notes from open space at Plone Symposium East 2011

## Goals

- Lightweight
- Install and uninstall cleanly
- GS import/export of vocabularies
- Initial simple flat vocabulary
- De-couple the term id from the object id
  - Changing values does not affect the key
- Way to manage the vocab with ease
- Orderable vocabs
  - Manual
  - On specific fields
- Define an API to retrieve vocabularies and terms
  - DisplayList
  - zope vocabulary
  - A volatile zope utility
  - Persistent storage
- Make sure there are no significant performance issues with large number of vocabs and terms
- Documentation. Use read the docs.
- Tests

## Storage layer

- Handle multiple vocabs
- Nested structure of vocabs and then the terms
- No special objects to leave behind
- Use zope.container.ordered.OrderedContainer to store the vocabs and the terms
- Add a counter attribute to the container in order to create the next unique item

## API

- retrieve a vocabulary
  - ordered by value
  - ordered by object position
  - As a particular vocabulary type
    - DisplayList
    - Zope3 Vocab
    - List of tuples (container.items)
- add a term to a vocab
  - Create a key that has the vocab id and the term id
- remove a term from the vocab
  - fire event
- remove a vocab
  - fire event
- add a vocab
- change term order
- optionally change vocab order

- Migration from ATVM to this product

## Down The Road

- Complex nested vocabs
- VDEX support
  - Relationships
  - Translations
