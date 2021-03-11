from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True, editable=False)
    tags = TaggableManager(blank=True)
    expiry = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Document<'{self.name}' ({self.uuid})>"

class DocumentRevision(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, editable=False)
    revision = models.PositiveIntegerField(editable=False)
    time = models.DateTimeField(editable=False)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, editable=False)
    # original_client = ...client...
    # authentication = ...auth...

    tags = TaggableManager(blank=True)
    file_type = models.CharField(max_length=255, editable=False)
    original_filename = models.TextField(blank=True, editable=False)
    physical_location = models.TextField(blank=True)

    signature = models.BinaryField(editable=False)

    def __str__(self):
        return str(self.revision)

    def __repr__(self):
        return f"DocumentRevision<{self.document!r}, {self.revision!s}>"
