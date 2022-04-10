import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 200, blank = True)
	article_text = models.TextField('Текст статьи', blank = True)
	article_image = models.ImageField('Картинка статьи', blank=True, default="", upload_to = 'images/')
	pub_date = models.DateTimeField('Дата публикации статьи', default=timezone.now)

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField("Имя автора", max_length = 50)
	comment_text = models.CharField('Текст комментария', max_length = 500)
	pub_date = models.DateTimeField("Дата публикации комментария")

	def __str__(self):
		return self.comment_text

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"