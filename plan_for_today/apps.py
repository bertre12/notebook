from django.apps import AppConfig


class PlanForTodayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plan_for_today'

    # Замена названия.
    verbose_name = 'План на сегодня'
