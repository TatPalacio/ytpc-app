Objetivo
El desarrollador debe demostrar sus habilidades entregando un código fuente en Django
que permita ejecutar una aplicación web con autenticación y CRUD de personas,
consumiendo un API y mostrando una interfaz visual básica.
Tiempo
El ejercicio tendrá una duración de 4 horas
Calificación
● 30% de la calificación es el tiempo donde las 4 horas definidas para la evaluación es
el 100%
○ Por cada hora adicional se le quita el 25% de la calificación del tiempo.
● 60% de la calificación es la funcionalidad operando con calidad
● 10% de la calificación es la calidad visual
Reglas
● El tiempo de prueba arranca cuando se termine la presentación del ejercicio
● Pueden usar cualquier tipo de apoyo (IA, apuntes del curso, etc) pero no preguntar
a un compañero de equipo.
● Se deben despejar todas las dudas durante la presentación del ejercicio
● El proyecto debe llamarse con las iniciales del participante, ej: lmj-app
● El código fuente desarrollado debe ser subido a un repositorio público para su
revisión
Historia de usuario
Yo como usuario final, requiero una aplicación que permita autenticar a un usuario para
poder acceder a las funcionalidades de listar, crear, editar y eliminar los registros de
personas usando el api de desarrollo expuesto en la url
http://3.137.160.186:5000/clinica/api/
Una vez dentro de la aplicación, el usuario registrará una persona y ésta deberá aparecer
en la lista.
Criterios de aceptación
1. La aplicación debe usar Django + Django REST Framework.
2. Usar arquitectura MTV para el desarrollo del proyecto
3. Implementar login de usuario con JWT o sesión de Django (/auth/).
4. Implementar un CRUD de personas (/api/personas/):
- GET → listar (con paginación).
- POST → crear.
- PUT/PATCH → editar.
- DELETE → eliminar.
5. Debe haber templates personalizados con Bootstrap/Tailwind que:
- Muestren la lista de personas en cards.
- Tengan un paginador.
- Permitan crear/editar personas con formularios (forms.ModelForm).
Entregables
1. Repositorio en GitHub/GitLab con:
- Código fuente Django.
- Archivo requirements.txt.
- Instrucciones en README.md para ejecutar localmente.
- Aplicación funcional con login + CRUD de personas.
