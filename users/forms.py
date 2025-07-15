from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
# Custom forms adding Tailwind CSS classes

class StyledAuthenticationForm(AuthenticationForm):  # Style login fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():  # Apply Tailwind classes
            field.widget.attrs.update({'class': 'w-full border rounded p-2'})

class StyledUserCreationForm(UserCreationForm):  # Style registration fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():  # Apply Tailwind classes
            field.widget.attrs.update({'class': 'w-full border rounded p-2'})
