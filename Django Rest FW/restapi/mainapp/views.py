from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from uuid import uuid4
from rest_framework import status
from mainapp.models import Account
from mainapp.serializers import AccountSerializer


@api_view(['GET', 'POST'])
def get_post_account(request):
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        return Response({})


class AccountCreate(CreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset
