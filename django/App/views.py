from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def nuevo_usuario (request):

        if request.method=='POST':
            formulario= UserCreationForm(request.POST)
            if formulario.is_valid:
                formulario.save()
                returnHttpResponseRedirect('/')
        else:
            formulario =UserCreationForm()
        return  render_to_response ('nuevousuario.html',{'formulario':formulario},context_instance=RequestContext(request))