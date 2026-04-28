# inspections/models.py

from django.db import models
from complaints.models import Complaint
from django.conf import settings

class Inspection(models.Model):
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name="inspections"
    )
    inspector = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inspections"
    )
    remarks = models.TextField()
    image = models.ImageField(upload_to="inspection_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inspection by {self.inspector.username} for {self.complaint.title}"
