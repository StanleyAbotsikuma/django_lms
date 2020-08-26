from django.contrib import admin
from management.models import TeacherModal,Staff,Subject,ClassRoom,Lesson,LessonFiles,Student_info,Student
# Register your models here.

admin.site.register(TeacherModal)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(LessonFiles)
admin.site.register(ClassRoom)
admin.site.register(Student_info)
admin.site.register(Student)

