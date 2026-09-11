# Sistema Integral de Vigilancia y Administración

Sistema web en Django para la administración de un fraccionamiento: residentes, viviendas, cuotas semanales, pagos, control de visitantes, servicios, paquetería, avisos comunitarios, correo y dashboard.

## Puesta en marcha en Windows / PowerShell

```powershell
cd $HOME\Desktop\sistema_vigilancia
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations residentes pagos accesos servicios
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir: http://127.0.0.1:8000/

## Roles

La migración de `accounts` crea dos grupos:

- Administrador
- Guardia

Los superusuarios tienen acceso administrativo completo.

## Flujo recomendado

1. Registrar viviendas y residentes.
2. Definir la cuota semanal de cada vivienda.
3. En Pagos, generar las cuotas de la semana.
4. Registrar pagos en efectivo o transferencia.
5. Usar `Enviar recordatorios` para avisar por correo a quienes tengan adeudo.
6. El guardia registra visitantes, servicios y paquetería y marca su salida.
7. Desde Avisos se puede emitir un aviso general o el ingreso del camión de basura.

## Correo

Por defecto el sistema usa el backend de consola: los correos aparecen en PowerShell.
Para correo real copia `.env.example` como `.env` y configura SMTP.

## Git

No subir `venv`, `db.sqlite3`, `.env` ni `media/`.
