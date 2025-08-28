Este proyecto es una **aplicación web desarrollada en Django** que se conecta a una base de datos **PostgreSQL** y permite realizar operaciones de mantenimiento  

Este sistema incluye 3 tablas:  

1. **Estudiantes**  
   - Se registran estudiantes con la informacion de nombre, apellido, correo electrónico y fecha de nacimiento.  

2. **Cursos**  
   - Registra los cursos que ofrece la institución, con su nombre y descripción.  

3. **Matrículas**  
   - Representa la relación entre estudiantes y cursos.  
   - Un estudiante puede matricularse en varios cursos, y un curso puede tener varios estudiantes.  

### 🔗 Conexión entre Tablas
- **Estudiantes** y **Cursos** se relacionan mediante la tabla **Matrículas**.  
- Gracias a esta estructura, es posible gestionar fácilmente qué estudiantes están inscritos en qué cursos.  

**Panel del Administrador , donde se puede ingresar un curso y asi mismo realizar matriculas**
( A este apartado le falta la implemetadcion para que los estudiantes realizen sus propias matriculas desde la url /estudiante , puesto que solo las realiza el administrador

Para la cual uno tiene que registrarse como administrador : python manage.py createsuperuser
<img width="1412" height="607" alt="image" src="https://github.com/user-attachments/assets/209ed04c-b51f-43f7-936e-8b245da10d47" />

