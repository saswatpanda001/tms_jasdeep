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




class CertificationModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class PositionModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class SkillModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class TrainingProgramModel(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    duration = models.IntegerField(blank=True,null=True)
    skills= models.ManyToManyField(SkillModel,blank=True,null=True)
    eligible_positions = models.ManyToManyField(PositionModel,blank=True,null=True)

    def __str__(self):
        return self.name





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
    points = models.IntegerField(blank=True,null=True,default=200)


    def __str__(self):
        return f"{self.user.username} - {self.role}"




class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300,blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    time = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title


class AppreciationPoints(models.Model):
    sender = models.ForeignKey(UserProfileModel, related_name='sent_points', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfileModel, related_name='received_points', on_delete=models.CASCADE)
    points = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender.user.username} sent {self.points} points to {self.receiver.user.username}"

    def save(self, *args, **kwargs):
        # Update the sender and receiver points when saving a transaction
        if self.pk is None:  # Only run when saving a new transaction (not an update)
            self.sender.points -= self.points
            self.receiver.points += self.points
            self.sender.save()
            self.receiver.save()
        super().save(*args, **kwargs)
        