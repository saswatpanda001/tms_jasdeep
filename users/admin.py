from django.contrib import admin
from users.models import AchievementModel, SkillModel, CertificationModel, TrainingProgramModel, PositionModel, UserProfileModel


admin.site.register(UserProfileModel)
admin.site.register(SkillModel)
admin.site.register(TrainingProgramModel)
admin.site.register(CertificationModel)
admin.site.register(PositionModel)


