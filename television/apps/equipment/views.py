from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsTechnician
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [IsTechnician()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"error": "Неавторизованный пользователь"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_equipment(self, request):
        equipment = Equipment.objects.filter(owner=request.user)
        serializer = self.get_serializer(equipment, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['patch'], permission_classes=[IsTechnician()])
    def change_status(self, request, pk=None):
        equipment = self.get_object()
        new_status = request.data.get('status')

        if new_status not in ['available', 'booked', 'maintenance']:
            return Response({"error": "Некорректный статус"}, status=400)

        equipment.status = new_status
        equipment.save()
        return Response(EquipmentSerializer(equipment).data)

