from django.db import models


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

    def __str__(self):
        return f"Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
# Изображение

# Адрес

# Отзывы

# Контакты продавца

# Похожие товары