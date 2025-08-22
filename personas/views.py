from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Medico
from .serializers import MedicoSerializer

def index(request):
    return render(request, "index.html")

class MedicoViewSet(viewsets.ViewSet):
    # GET /clinica/api/medico
    def list(self, request):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)

    # GET /clinica/api/medico/{tipoDocumento}/{numeroDocumento}
    def retrieve(self, request, tipo_documento=None, numero_documento=None):
        try:
            medico = Medico.objects.get(tipo_documento=tipo_documento, numero_documento=numero_documento)
            serializer = MedicoSerializer(medico)
            return Response(serializer.data)
        except Medico.DoesNotExist:
            return Response({"error": "Médico no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # POST /clinica/api/medico
    def create(self, request):
        serializer = MedicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT /clinica/api/medico
    def update(self, request):
        try:
            medico = Medico.objects.get(
                tipo_documento=request.data.get("tipoDocumento"),
                numero_documento=request.data.get("numeroDocumento")
            )
            serializer = MedicoSerializer(medico, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Medico.DoesNotExist:
            return Response({"error": "Médico no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE /clinica/api/medico
    def destroy(self, request):
        try:
            medico = Medico.objects.get(
                tipo_documento=request.data.get("tipoDocumento"),
                numero_documento=request.data.get("numeroDocumento")
            )
            medico.delete()
            return Response({"message": "Médico eliminado"})
        except Medico.DoesNotExist:
            return Response({"error": "Médico no encontrado"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def authenticate_user(request):
    username = request.data.get("username")
    password = request.data.get("password")


    if username == "yenko" and password == "jk$2034#":
        refresh = RefreshToken.for_user(None)  
        return Response({"token": str(refresh.access_token)})
    return Response({"error": "Credenciales inválidas"}, status=401)