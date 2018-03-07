#Returns The User Objects thats currently active
from django.contrib.auth import get_user_model
# A user that creates a user with no privileges from the given username and password
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
    # Setting the label to the username and email
     def __init__(self,*args,**kwargs):
         super().__init__(*args, **kwargs)
         self.fields['username'].label = 'Display Name'
         self.fields['email'].label = 'Email Address'

    