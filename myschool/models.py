from django.db import models

# Create your models here.
class Teachers(models.Model):
    teacher_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.teacher_name
    
class Students(models.Model):
    teacher = models.ForeignKey(Teachers,related_name="students_teachers")
    student_rollno = models.IntegerField()
    student_name = models.CharField(max_length=255)
    student_last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.student_name
    
class Subjects(models.Model):
    teacher = models.ForeignKey(Teachers,related_name="subjects_teachers")
    student = models.ForeignKey(Students,related_name="subjects_students")
    book_name = models.CharField(max_length=255)
    book_description = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
        
    def __str__(self):
        return self.book_name