from django.contrib import admin

from apps.landpage.models import CoursePreview
from apps.landpage.models import LandpageContactMessage
from apps.landpage.models import LandpageCoursePreview
from apps.landpage.models import LandpagePartner
from apps.landpage.models import LandpageTeamMember
from apps.landpage.models import LandpageTopPickCourse

admin.site.register(LandpageTeamMember)
admin.site.register(LandpageCoursePreview)
admin.site.register(LandpageTopPickCourse)
admin.site.register(CoursePreview)
admin.site.register(LandpageContactMessage)
admin.site.register(LandpagePartner)
