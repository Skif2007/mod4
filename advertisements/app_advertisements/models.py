from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    # Заголовок
    title = models.CharField("Заголовок", max_length=128)
    # Описание
    description= models.TextField("Описание")
    # Цена
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    # Дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    # Дата изменения
    updated_at = models.DateTimeField(auto_now=True)
    # Торг
    auction = models.BooleanField("Торг", help_text="Ответьте, если хотите торговаться")
    # продавец
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    # картинка
    image = models.ImageField('изображение', upload_to = 'advertisements/')

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone

        if self.created_at.date()== timezone.now().date():
            created_time = self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
            return format_html("<span style='color:green; font-weight:hold;'> Сегодня в {}</span>", created_time)

        return self.created_at.strftime(" %H:%M:%S")
    @admin.display(description="Время обновления")
    def updated_date(self):
        from django.utils import timezone

        if self.updated_at.date()== timezone.now().date():
            updated_time = self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
            return format_html("<span style='color:blue; font-weight:hold;'> Сегодня в {}</span>",updated_time)

        return self.updated_at.strftime(" %H:%M:%S")

    def __str__(self):
        return f"Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
    # Изображение

    # Адрес

    # Отзывы

    # Контакты продавца

    # Похожие товары