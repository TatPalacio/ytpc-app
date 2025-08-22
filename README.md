# YTPC-App - Gestión de Personas 👩‍⚕️👨‍⚕️

Aplicación web en **Django + Django REST Framework** que permite la **autenticación de usuarios** y el **CRUD de personas**, consumiendo el API expuesto en:

```
http://3.137.160.186:5000/clinica/api/
```

El proyecto incluye una interfaz visual básica con **Bootstrap/Tailwind**, listados en **cards** y formularios para creación y edición de personas.

---

## 🚀 Características

* Autenticación de usuarios con **JWT** o sesión de Django (`/auth/`).
* CRUD de personas (`/api/personas/`):

  * `GET` → listar (con paginación).
  * `POST` → crear.
  * `PUT/PATCH` → editar.
  * `DELETE` → eliminar.
* Templates personalizados con:

  * Lista de personas en **cards**.
  * **Paginador** integrado.
  * Formularios (basados en `forms.ModelForm`) para crear/editar personas.
* Arquitectura **MTV** siguiendo buenas prácticas de Django.

---

## 📂 Estructura del proyecto

```
ytpc-app/
│── personas/              # App principal con modelos, views, serializers, urls
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
│── ytpc_app/              # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── templates/             # Templates HTML con Bootstrap/Tailwind
│── static/                # Archivos estáticos (CSS, JS)
│── requirements.txt       # Dependencias del proyecto
│── manage.py
└── README.md
```

---

## 🛠️ Requisitos previos

* Python **3.10+**
* pip
* virtualenv (opcional pero recomendado)

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tuusuario/ytpc-app.git
   cd ytpc-app
   ```

2. **Crear entorno virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate   # en Linux/Mac
   venv\Scripts\activate      # en Windows
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migraciones de base de datos**

   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario**

   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor**

   ```bash
   python manage.py runserver
   ```

7. Abrir en el navegador:

   ```
   http://127.0.0.1:8000
   ```

---

## 🔑 Endpoints principales

### Autenticación

* `POST /auth/login/` → Login de usuario.
* `POST /auth/logout/` → Logout de usuario.

### API Personas

* `GET /api/personas/` → Listar personas (con paginación).
* `POST /api/personas/` → Crear persona.
* `PUT /api/personas/{id}/` → Editar persona.
* `DELETE /api/personas/{id}/` → Eliminar persona.

### Interfaz web

* `/personas/` → Lista de personas en cards.
* `/personas/crear/` → Formulario para crear persona.
* `/personas/editar/<id>/` → Formulario para editar persona.

---

## 🎨 UI

* **Lista de personas**: cards con nombre y documento.
* **Paginador** para navegar entre registros.
* **Formularios** responsivos con Bootstrap/Tailwind.

---

## ✅ Criterios cumplidos

✔️ Django + Django REST Framework
✔️ Arquitectura MTV
✔️ Login con JWT/sesiones
✔️ CRUD de personas desde API
✔️ Templates con cards, formularios y paginador
✔️ Código en repositorio público

---

## 📄 Licencia

Proyecto de prueba técnica. Uso libre para evaluación.

---

