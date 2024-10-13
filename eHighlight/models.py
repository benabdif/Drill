from django.db import models


class eHighlight_Record(models.Model):
    WEEK_CHOICES = [(i, f"Week {i}") for i in range(1, 53)]  # Weeks 1 to 52

    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    user_date = models.DateField(auto_now_add=True)
      # Add a user_date field
    week = models.PositiveIntegerField(choices=WEEK_CHOICES)
    Cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    details = models.TextField(blank=True, null=True)

    UNIT_CHOICES = [
        ('SACU 1', 'SACU 1'),
        ('SACU 2', 'SACU 2'),
        ('SACU 3', 'SACU 3'),
        ('HSE Group', 'HSE Group'),
        ('Dispatcher Group', 'Dispatcher Group'),
        ('Surveyor Group', 'Surveyor Group'),
        ('Waste Management Group', 'Waste Management Group'),
        ('Engineering Support', 'Engineering Support'),
    ]
    unit = models.CharField(max_length=100, choices=UNIT_CHOICES, blank=True, null=True)

    HIGHLIGHT_CHOICES = [
        ('Wellsite Activities', 'Wellsite Activities'),
        ('Accomplishment', 'Accomplishment'),
        ('Initiatives', 'Initiatives'),
        ('Digital Transformation', 'Digital Transformation'),
        ('Cost Optimization', 'Cost Optimization'),
        ('Academic & Professional Certificates', 'Academic & Professional Certificates'),
        ('Awards & Recognitions', 'Awards & Recognitions'),
        ('Workshop', 'Workshop'),
        ('HSE', 'HSE'),
    ]
    highlight_type = models.CharField(max_length=100, choices=HIGHLIGHT_CHOICES, blank=True, null=True)

    WELLSITE_ACTIVITIES = [
        ('Engineering Schedule Meeting', 'Engineering Schedule Meeting'),
        ('Contractors Meeting', 'Contractors Meeting'),
        ('Clean-Up Completed before KPI deadline', 'Clean-Up Completed before KPI deadline'),
        ('Construction Completed before KPI deadline', 'Construction Completed before KPI deadline'),
        ('Special Location / lay-out', 'Special Location / lay-out'),
        ('Rig Move', 'Rig Move'),
        ('Pre-Workover KOM', 'Pre-Workover KOM'),
        ('Emergency Intervention', 'Emergency Intervention'),
        ('Change Request', 'Change Request'),
        ('Site Review', 'Site Review'),
        ('Rig on Location Support (Heavy Equipment)', 'Rig on Location Support (Heavy Equipment)'),
        ('Rig on Location Support (Vacuum Tankers)', 'Rig on Location Support (Vacuum Tankers)'),
        ('Waste Manifest', 'Waste Manifest'),
        ('NA', 'NA'),
    ]
    wellsite_activity = models.CharField(max_length=100, choices=WELLSITE_ACTIVITIES, blank=True, null=True)

    def __str__(self):
        return (f"Record {self.id}: Date: {self.date}, User Date: {self.user_date}, Week: {self.week}, "
                f"Cost: {self.Cost}, Unit: {self.unit}, Highlight Type: {self.highlight_type}, "
                f"Wellsite Activity: {self.wellsite_activity}, Details: {self.details}, "
                f"Document: {self.document.url if self.document else 'No Document'}, "
                f"Image: {self.image.url if self.image else 'No Image'}")
