""" Prototype use case example """

from document import Document

original_document = Document('Original', [[1, 2, 3, 4], [5, 6, 7, 8]])
print('Showing original document:')
print(original_document)
print()


document_copy_1 = original_document.clone(mode=1)
document_copy_1.name = 'Copy 1'
print('Showing original and copied documents without any modification:')
print(original_document)
print(document_copy_1)
print()

# Because using the mode=1 does not really create any new objects,
# the following modification on the copied object will also influence the original object
# If one would tru to override the whole list on the copied object, this however would
# not affect the original object, because what happens is that the variable in the copied
# object simply gets assigned
# to a new object. This also modifies the id of the copied object.
document_copy_1.list[0] = 200
print('Showing original and copy1 document with changes made on copy1 affecting also original document:')
print(original_document)
print(document_copy_1)
print()

original_document = Document('Original', [[1, 2, 3, 4], [5, 6, 7, 8]])
document_copy_2 = original_document.clone(mode=2)
document_copy_2.name = 'Copy 2'
document_copy_2.list[0] = 200
print('Showing that original document is not affected by changes in the copy2 when .copy method was used:')
print(original_document)
print(document_copy_2)
print()

original_document = Document('Original', [[1, 2, 3, 4], [5, 6, 7, 8]])
document_copy_3 = original_document.clone(mode=2)
document_copy_3.name = 'Copy 3'
document_copy_3.list[0][0] = 200
print('This shows that .copy works only one level deep:')
print(original_document)
print(document_copy_3)
print()

original_document = Document('Original', [[1, 2, 3, 4], [5, 6, 7, 8]])
document_copy_4 = original_document.clone(mode=3)
document_copy_4.name = 'Copy 4'
document_copy_4.list[0][0] = 200
print('This shows that deepcopy works recursively and copies every layer of the document:')
print(original_document)
print(document_copy_4)
print()

