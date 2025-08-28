from django import forms
from .models import Estudiante
from .models import Matricula 

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'dni', 'email']




# registro de matriculas 
class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'curso']