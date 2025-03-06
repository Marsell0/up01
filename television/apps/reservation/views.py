from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsOperator
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve', 'destroy']:
            return [IsOperator()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(operator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.operator != request.user:
            return Response({"error": "Вы можете отменять только свои бронирования."}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Бронирование отменено."}, status=status.HTTP_204_NO_CONTENT)
