from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.users.permissions import IsAdmin, IsOperator
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [IsOperator()]
        elif self.action in ['approve', 'reject']:
            return [IsAdmin()]
        return [IsAdmin()]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """ Подтверждение бронирования администратором """
        booking = self.get_object()
        booking.status = 'approved'
        booking.save()
        return Response({'status': 'Бронирование подтверждено'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """ Отклонение бронирования администратором """
        booking = self.get_object()
        booking.status = 'rejected'
        booking.save()
        return Response({'status': 'Бронирование отклонено'}, status=status.HTTP_200_OK)