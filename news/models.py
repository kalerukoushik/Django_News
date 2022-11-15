from django.db import models

# Create your models here.

class Reporter(models.Model):
	full_name = models.CharField(max_length=100)

	def __str__(self):
		return self.full_name


class Article(models.Model):
	pub_date = models.DateField()
	head_line = models.CharField(max_length=200)
	content = models.TextField()
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __str__(self):
		return self.head_line