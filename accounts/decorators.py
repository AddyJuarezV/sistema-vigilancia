from django.contrib.auth.decorators import user_passes_test


def administrador_required(view_func):
    return user_passes_test(
        lambda user: (
            user.is_authenticated
            and (
                user.is_superuser
                or user.groups.filter(name="Administrador").exists()
            )
        ),
        login_url="/accounts/login/",
    )(view_func)


def guardia_required(view_func):
    return user_passes_test(
        lambda user: (
            user.is_authenticated
            and (
                user.is_superuser
                or user.groups.filter(name="Guardia").exists()
            )
        ),
        login_url="/accounts/login/",
    )(view_func)

def personal_vigilancia_required(view_func):
    return user_passes_test(
        lambda user: (
            user.is_authenticated
            and (
                user.is_superuser
                or user.groups.filter(
                    name__in=["Administrador", "Guardia"]
                ).exists()
            )
        ),
        login_url="/accounts/login/",
    )(view_func)