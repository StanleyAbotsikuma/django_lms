from django import forms
from management.models import TeacherModal,Staff,Subject,Lesson,LessonFiles,ClassRoom,Student_info,Student





'''"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TEACHER'S ZONE           TEACHER'S ZONE             TEACHER'S ZONE
TEACHER'S ZONE
TEACHER'S ZONE           TEACHER'S ZONE             TEACHER'S ZONE   TEACHER'S ZONE
TEACHER'S ZONE
TEACHER'S ZONETEACHER'S ZONETEACHER'S ZONE TEACHER'S ZONETEACHER'S ZONE TEACHER'S ZONE
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''


class teacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModal
        fields = [ 
        "first_name",
        "last_name",
        "email",
        "password",
        "profile_picture",
        "mobile",
        "city"
        ]
        

class staffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id','staff_class']

class classForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['class_name']


class subjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["subject_name",'subject_picture','staff_id','classroom']
        



class lessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_title','term','lesson_description','subject']




class learnMaterialsForm(forms.ModelForm):
    class Meta:
        model = LessonFiles
        fields = ['lesson_id','file']





'''"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
STUDENT'S ZONE           STUDENT'S ZONE             STUDENT'S ZONE
STUDENT'S ZONE
STUDENT'S ZONE           STUDENT'S ZONE             STUDENT'S ZONE   STUDENT'S ZONE
STUDENT'S ZONE
STUDENT'S ZONESTUDENT'S ZONESTUDENT'S ZONE STUDENT'S ZONESTUDENT'S ZONE STUDENT'S ZONE
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''

class StudentRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Student_info
        fields = [ 
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "password",
        "profile_picture",
        "mobile",
        "location"
        ]
        


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = [ 
        "student_id",
        "student_class",
        ]
