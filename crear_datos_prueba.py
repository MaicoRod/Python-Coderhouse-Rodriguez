import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diario_project.settings')
django.setup()

from django.contrib.auth.models import User
from diario.models import Emocion, Categoria, EntradaGratitud
from mensajeria.models import Mensaje
from accounts.models import Perfil

def crear_usuarios():
    print("Creando usuarios...")
    
    if not User.objects.filter(username='maria').exists():
        user1 = User.objects.create_user(
            username='maria',
            email='maria@example.com',
            password='maria123',
            first_name='María',
            last_name='González'
        )
        Perfil.objects.create(
            user=user1,
            biografia='Me encanta escribir sobre mis experiencias diarias'
        )
        print("✅ Usuario 'maria' creado")
    else:
        user1 = User.objects.get(username='maria')
        print("⚠️  Usuario 'maria' ya existe")
    
    if not User.objects.filter(username='juan').exists():
        user2 = User.objects.create_user(
            username='juan',
            email='juan@example.com',
            password='juan123',
            first_name='Juan',
            last_name='Pérez'
        )
        Perfil.objects.create(
            user=user2,
            biografia='Practico la gratitud desde hace 2 años'
        )
        print("✅ Usuario 'juan' creado")
    else:
        user2 = User.objects.get(username='juan')
        print("⚠️  Usuario 'juan' ya existe")
    
    return user1, user2


def crear_emociones():
    print("\nCreando emociones...")
    
    emociones_data = [
        {'nombre': 'Feliz', 'descripcion': 'Sentimiento de alegría y satisfacción'},
        {'nombre': 'Tranquilo', 'descripcion': 'Estado de paz y calma'},
        {'nombre': 'Agradecido', 'descripcion': 'Reconocimiento por lo bueno'},
        {'nombre': 'Esperanzado', 'descripcion': 'Confianza en el futuro'},
    ]
    
    emociones = []
    for data in emociones_data:
        emocion, created = Emocion.objects.get_or_create(**data)
        if created:
            print(f"✅ Emoción '{data['nombre']}' creada")
        else:
            print(f"⚠️  Emoción '{data['nombre']}' ya existe")
        emociones.append(emocion)
    
    return emociones


def crear_categorias():
    print("\nCreando categorías...")
    
    categorias_data = [
        {'nombre': 'Familia', 'descripcion': 'Momentos con seres queridos'},
        {'nombre': 'Trabajo', 'descripcion': 'Logros y experiencias laborales'},
        {'nombre': 'Salud', 'descripcion': 'Bienestar físico y mental'},
        {'nombre': 'Amistad', 'descripcion': 'Relaciones y conexiones'},
    ]
    
    categorias = []
    for data in categorias_data:
        categoria, created = Categoria.objects.get_or_create(**data)
        if created:
            print(f"✅ Categoría '{data['nombre']}' creada")
        else:
            print(f"⚠️  Categoría '{data['nombre']}' ya existe")
        categorias.append(categoria)
    
    return categorias


def crear_entradas(user1, user2, emociones, categorias):
    print("\nCreando entradas...")
    
    entradas_data = [
        {
            'titulo': 'Un día maravilloso con mi familia',
            'subtitulo': 'Almuerzo dominical inolvidable',
            'descripcion': '<p>Hoy fue un día especial. Nos reunimos toda la familia para almorzar. <strong>Compartimos risas, historias</strong> y buenos momentos.</p><p>Estoy muy agradecido por tener una familia tan unida.</p>',
            'autor': user1,
            'emocion': emociones[0],
            'categoria': categorias[0],
        },
        {
            'titulo': 'Logro importante en el trabajo',
            'subtitulo': 'Finalmente terminé el proyecto',
            'descripcion': '<p>Después de semanas de esfuerzo, <em>logré completar el proyecto</em> que me habían asignado.</p><p>Mi jefe me felicitó y me siento muy orgulloso del resultado.</p>',
            'autor': user1,
            'emocion': emociones[0],
            'categoria': categorias[1],
        },
        {
            'titulo': 'Caminata matutina',
            'subtitulo': 'Empezando el día con energía',
            'descripcion': '<p>Hoy me levanté temprano y salí a caminar. El aire fresco y el ejercicio me hicieron sentir <strong>renovado y lleno de energía</strong>.</p><p>Es increíble cómo algo tan simple puede mejorar tanto el día.</p>',
            'autor': user2,
            'emocion': emociones[1],
            'categoria': categorias[2],
        },
        {
            'titulo': 'Reunión con viejos amigos',
            'subtitulo': 'Reencuentro después de años',
            'descripcion': '<p>Me encontré con amigos que no veía hace años. Fue maravilloso recordar viejos tiempos y actualizarnos sobre nuestras vidas.</p><p>La amistad verdadera no tiene tiempo.</p>',
            'autor': user2,
            'emocion': emociones[2],
            'categoria': categorias[3],
        },
        {
            'titulo': 'Nuevos proyectos en el horizonte',
            'subtitulo': 'Mirando hacia el futuro',
            'descripcion': '<p>Tengo varios proyectos en mente que quiero desarrollar. Me siento <em>esperanzado</em> y motivado.</p><p>El futuro se ve brillante y lleno de posibilidades.</p>',
            'autor': user1,
            'emocion': emociones[3],
            'categoria': categorias[1],
        },
    ]
    
    for data in entradas_data:
        entrada, created = EntradaGratitud.objects.get_or_create(
            titulo=data['titulo'],
            defaults=data
        )
        if created:
            print(f"✅ Entrada '{data['titulo'][:30]}...' creada")
        else:
            print(f"⚠️  Entrada '{data['titulo'][:30]}...' ya existe")


def crear_mensajes(user1, user2):
    print("\nCreando mensajes...")
    
    mensajes_data = [
        {
            'remitente': user1,
            'destinatario': user2,
            'asunto': '¡Hola Juan!',
            'contenido': 'Vi tu entrada sobre la caminata matutina. ¡Me inspiraste! Voy a empezar a caminar yo también.',
        },
        {
            'remitente': user2,
            'destinatario': user1,
            'asunto': 'Re: ¡Hola Juan!',
            'contenido': '¡Qué bueno María! Te va a encantar. Es una excelente forma de empezar el día con energía positiva.',
        },
        {
            'remitente': user1,
            'destinatario': user2,
            'asunto': 'Pregunta sobre gratitud',
            'contenido': '¿Cómo haces para ser tan constante escribiendo en el diario? Quiero mejorar mi disciplina.',
        },
    ]
    
    for data in mensajes_data:
        mensaje, created = Mensaje.objects.get_or_create(
            asunto=data['asunto'],
            remitente=data['remitente'],
            defaults=data
        )
        if created:
            print(f"✅ Mensaje '{data['asunto']}' creado")
        else:
            print(f"⚠️  Mensaje '{data['asunto']}' ya existe")


def main():
    print("="*50)
    print("CREANDO DATOS DE PRUEBA")
    print("="*50)
    
    user1, user2 = crear_usuarios()
    emociones = crear_emociones()
    categorias = crear_categorias()
    crear_entradas(user1, user2, emociones, categorias)
    crear_mensajes(user1, user2)
    
    print("\n" + "="*50)
    print("✅ DATOS DE PRUEBA CREADOS EXITOSAMENTE")
    print("="*50)
    print("\nCredenciales de acceso:")
    print("Usuario 1: maria / maria123")
    print("Usuario 2: juan / juan123")


if __name__ == '__main__':
    main()