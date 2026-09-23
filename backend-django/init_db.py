import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from inventario.models import UsuarioModel

def setup_users():
    # 1. Crear o actualizar Administrador
    admin_user, created = UsuarioModel.objects.get_or_create(correo='admin@litetest.com')
    admin_user.set_password('password123')
    admin_user.is_admin = True
    admin_user.rol = 'Administrador'
    admin_user.save()
    print("Usuario admin@litetest.com actualizado/creado correctamente.")

    # 2. Crear o actualizar Usuario Externo
    externo_user, created = UsuarioModel.objects.get_or_create(correo='externo@litetest.com')
    externo_user.set_password('password123')
    externo_user.rol = 'Externo'
    externo_user.save()
    print("Usuario externo@litetest.com actualizado/creado correctamente.")

if __name__ == '__main__':
    setup_users()