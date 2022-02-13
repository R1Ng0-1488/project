from django.db import models


class Worker(models.Model):
    """Модель рабочего"""
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Номер телефона', 
        unique=True, max_length=255)

    def __str__(self) -> str:
        return self.name 

    
    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'


class AStore(models.Model):
    """Модель торговая точка"""
    title = models.CharField('Название', max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title 
    

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'


class Visit(models.Model):
    """Модель посещение"""
    datetime = models.DateTimeField('Дата/Время', auto_now_add=True)
    astore = models.ForeignKey(AStore, on_delete=models.CASCADE)
    latitlude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self) -> str:
        return f'{self.datetime} - {self.astore.title}'


    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'