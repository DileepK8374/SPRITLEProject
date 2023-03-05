from django import forms;
from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User		#it is mysql-db model-table(for auth_app_db)
        fields=['username', 'password','email'];
