from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': '',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        # Criar o usuário sem salvar imediatamente no banco de dados
        user = super().save(commit=False)
        
        # Configurar a senha do usuário (fazendo o hash da senha)
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()  # Agora salva o usuário no banco de dados com a senha criptografada
        return user
