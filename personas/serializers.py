from rest_framework import serializers
from .models import Persona, Medico

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'nombres','apellidos', 'email', 'telefono', 'created_at')
        #Para no modificar info de creacion
        read_only_fields = ('created_at', )
        
class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = "__all__"        