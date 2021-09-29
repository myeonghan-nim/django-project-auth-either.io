# README

## Account Handling

```python
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup(request):
    return


def login(request):
    return


def logout(request):
    return
```

## Django Decorator

```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@require_POST
def create(request):
    return


@login_required
def delete(request):
    return
```
