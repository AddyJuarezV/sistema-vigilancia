def roles(request):
    user = request.user
    if not getattr(user, 'is_authenticated', False):
        return {'es_admin': False, 'es_guardia': False}
    es_admin = user.is_superuser or user.groups.filter(name='Administrador').exists()
    es_guardia = user.is_superuser or user.groups.filter(name='Guardia').exists()
    return {'es_admin': es_admin, 'es_guardia': es_guardia}
