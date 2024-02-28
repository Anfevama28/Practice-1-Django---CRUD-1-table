from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]



class UserUpdate(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name"]
        

    def __init__(self, *args, **kwargs) -> None:
        super(UserUpdate, self).__init__(*args, **kwargs)
        del self.fields["password1"]
        del self.fields["password2"]

    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['password1'] = self.initial.get('password1', '')
        cleaned_data['password2'] = self.initial.get('password2', '')
        return cleaned_data