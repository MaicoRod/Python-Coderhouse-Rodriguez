# DiarioGratitud+Rodriguez

**Proyecto Final - Curso Python Django - Coderhouse**

Diario de Gratitud Express: Aplicación web para practicar la gratitud y manejar la ansiedad.

## 📋 Descripción

Aplicación web tipo blog desarrollada en Django que permite a los usuarios:
- Crear entradas de gratitud con texto enriquecido e imágenes
- Gestionar perfiles personalizados con avatar
- Comunicarse entre usuarios mediante mensajería interna
- Buscar y filtrar contenido
- Categorizar entradas por emociones

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/DiarioGratitud+Rodriguez.git
cd DiarioGratitud+Rodriguez
```

### 2. Crear entorno virtual
```bash
python -m venv venv
```

### 3. Activar entorno virtual
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Crear datos de prueba (opcional)
```bash
python crear_datos_prueba.py
```

### 8. Correr el servidor
```bash
python manage.py runserver
```

### 9. Abrir en navegador
```
http://127.0.0.1:8000/
```

## 🧪 Credenciales de Prueba

Si ejecutaste el script de datos de prueba:
- Usuario 1: `maria` / `maria123`
- Usuario 2: `juan` / `juan123`

## 📍 Funcionalidades

| URL | Funcionalidad |
|-----|---------------|
| `/` | Inicio con búsqueda |
| `/about/` | Acerca de mí |
| `/pages/` | Listado de entradas |
| `/pages/<id>/` | Detalle de entrada |
| `/accounts/register/` | Registro |
| `/accounts/login/` | Login |
| `/accounts/profile/` | Perfil |
| `/mensajes/` | Mensajería |
| `/admin/` | Panel admin |

## 👨‍💻 Autor

**Maico Rodríguez**  
Proyecto Final - Coderhouse Python 2026