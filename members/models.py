from django.db import models

# Define membership choices at the module level to avoid duplication
MEMBERSHIP_CHOICES = (
    ('standard', 'Standard'),
    ('premium', 'Premium'),
    ('vip', 'VIP'),
)

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(max_length=30, choices=MEMBERSHIP_CHOICES)

    def __str__(self):
        return self.name

class MemberProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='standard')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.membership_type}"

    @property
    def full_name(self):
        """Returns the person's full name."""
        return f"{self.first_name} {self.last_name}"
