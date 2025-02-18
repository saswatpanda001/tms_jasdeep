from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()



class AchievementModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)


    def __str__(self):
        return self.name

class SkillModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class CertificationModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class TrainingProgramModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class PositionModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserProfileModel(models.Model):
    EMPLOYEE = 'employee'
    MANAGER = 'manager'
    MANAGEMENT = 'hr_manager'
    ADMINISTRATOR = 'administrator'

    ROLE_CHOICES = [
        (EMPLOYEE, 'employee'),
        (MANAGER, 'manager'),
        (MANAGEMENT, 'hr_manager'),
        (ADMINISTRATOR, 'administrator'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(SkillModel, blank=True, null=True)
    certifications = models.ManyToManyField(CertificationModel, blank=True, null=True)
    achievements = models.ManyToManyField(AchievementModel,blank=True, null=True)
    trainings = models.ManyToManyField(TrainingProgramModel, blank=True, null=True)
    rating = models.FloatField(default=0.0, blank=True, null=True)
    performance_history = models.TextField(blank=True, null=True)
    experience_years = models.IntegerField(default=0, blank=True, null=True)
    position = models.ForeignKey(PositionModel, on_delete=models.SET_NULL, null=True, blank=True)
    position_gen = models.CharField(max_length=100,null=True, blank=True)
    notifications_enabled = models.BooleanField(default=True, blank=True, null=True)
    joined = models.DateTimeField(default=timezone.now, blank=True, null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(default="profile_pics/default_profile.png", upload_to="profile_pics", blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} - {self.role}"



