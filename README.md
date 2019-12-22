# README

## Signup, Login, Logout

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def signup(request):
    return


def login(request):
    return


def logout(request):
    return
```

## Decorators in django

```python
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


@require_POST
def create(request):
    return


@login_required
def delete(request):
    return
```

