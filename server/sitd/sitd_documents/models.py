"""
ORM models for SITD document handling.

SPDX-License-Identifier: MPL-2.0
Copyright (c) 2021 Andrew MacIsaac
"""
from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager

class Document(models.Model):
    """
    Representation of an archived document.
    """
    # User-friendly document name.
    name = models.CharField(max_length=255)
    # Immutable unique identifier of the document.
    uuid = models.UUIDField(unique=True, editable=False)
    # Tags applicable to all revisions of the document.
    tags = TaggableManager(blank=True)
    # Potential expiry date of the document (UTC).
    expiry = models.DateTimeField()
    # Plain-text abstract or description of the document.
    description = models.TextField(blank=True)

    def __str__(self):
        """
        Readable name of the document.

        :return: Document name.
        :rtype: str
        """
        return str(self.name)

    def __repr__(self):
        """
        Debugging representation of the document object.

        :return: Document representation.
        :rtype: str
        """
        return f"Document<'{self.name!s}' ({self.uuid!s})>"

class DocumentRevision(models.Model):
    """
    Representation of a specific revision of an archived document.
    """
    # Document instance that this is a revision of.
    document = models.ForeignKey(Document, on_delete=models.CASCADE, editable=False)
    # Revision number.
    revision = models.PositiveIntegerField(editable=False)
    # UTC time stamp of revision.
    time = models.DateTimeField(editable=False)

    # User to whom this document revision belongs.
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, editable=False)
    # original_client = ...client...
    # authentication = ...auth...

    # Tags which apply to only this revision of the document.
    tags = TaggableManager(blank=True)
    # MIME type of the document file for this revision.
    file_type = models.CharField(max_length=255, editable=False)
    # Original name of the document file for this revision.
    original_filename = models.TextField(blank=True, editable=False)
    # Physical location of this document revision, if it is a physical document.
    physical_location = models.TextField(blank=True)

    # Digital signature of the revision.
    signature = models.BinaryField(editable=False)

    def __str__(self):
        """
        Document revision number.

        :return: Revision number as a string.
        :rtype: str
        """
        return str(self.revision)

    def __repr__(self):
        """
        Debugging representation of the revision object.

        :return: Revision representation.
        :rtype: str
        """
        return f"DocumentRevision<{self.document!r}, {self.revision!s}>"
