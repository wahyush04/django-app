from django.core.management.base import BaseCommand
from api.models import Component

class Command(BaseCommand):
    help = 'Seed database with dummy PC components'

    def handle(self, *args, **kwargs):
        components = [
            Component(name="Intel Core i5-12400F", brand="Intel", category="CPU", price=2300000, stock=10),
            Component(name="NVIDIA RTX 4060", brand="NVIDIA", category="GPU", price=5000000, stock=5),
            Component(name="Kingston Fury 16GB DDR4", brand="Kingston", category="RAM", price=800000, stock=20),
            Component(name="Samsung 980 1TB NVMe SSD", brand="Samsung", category="SSD", price=1200000, stock=8),
            Component(name="Corsair CX550M", brand="Corsair", category="PSU", price=900000, stock=12),
        ]

        Component.objects.bulk_create(components)
        self.stdout.write(self.style.SUCCESS('Successfully seeded components!'))
