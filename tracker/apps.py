from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'


class Bus(models.Model):
    name = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.route})"
