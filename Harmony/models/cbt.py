from django.db import models
from datetime import datetime

# Create your models here.
class QuestionsModel(models.Model):
	EXERMS_SUBJECTS = (
		('C++', 'c++'),
		('C-SHARP', 'c-sharp'),
		('PYTHON', 'python'),
		('PHP', 'php'),
		('ORACLE', 'oracle'),
		('POSTGRESQL', 'postgresql'),
		('MANAGEMENT', 'management'),
	)

	exam_subject = models.CharField(choices=EXERMS_SUBJECTS, max_length=255)
	slug = models.SlugField(max_length=150, db_index=True)
	exam_question = models.TextField()
	option_a = models.CharField(blank=True, null=True, max_length=200)
	option_b = models.CharField(blank=True, null=True, max_length=200)
	option_c = models.CharField(blank=True, null=True, max_length=200)
	option_d = models.CharField(blank=True, null=True, max_length=200)
	correct_answer = models.CharField(max_length=200)
	attempted = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		ordering = ('exam_subject',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.exam_subject


class QuestionAnswer(models.Model):
	question = models.OneToOneField(QuestionsModel, on_delete=models.CASCADE, primary_key=True)
	slug = models.SlugField(max_length=150, db_index=True)
	choosed_answer = models.CharField(max_length=200, blank=True)
	exam_date = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return self.choosed_answer

class ExamWriter(models.Model):
	answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def __str__(self):
		return "%s the writer is %s" % (self.name, self.QuestionAnswer, self.QuestionsModel,)



