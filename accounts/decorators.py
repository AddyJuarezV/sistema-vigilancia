from functools import wraps
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


def _require_groups(groups):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect_to_login(request.get_full_path())
            if user.is_superuser or user.groups.filter(name__in=groups).exists():
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapper
    return decorator


administrador_required = _require_groups(['Administrador'])
guardia_required = _require_groups(['Guardia'])
personal_vigilancia_required = _require_groups(['Administrador', 'Guardia'])
