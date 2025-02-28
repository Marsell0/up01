from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.users.permissions import IsAdmin
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework import viewsets

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return [IsAuthenticatedOrReadOnly()]
