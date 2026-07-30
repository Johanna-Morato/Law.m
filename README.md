# Law.m

#### Video Demo:
https://youtu.be/pnKx7h8LpEU

# English

#### Description

Law.m is a web application developed as the final project for **Harvard University's CS50x course**. Its primary purpose is to provide a simple, organized, and secure platform for managing clients within a law firm.

The idea for this project came from observing that many small and medium-sized law offices still manage client information through spreadsheets, text documents, or even paper records. These methods often make organization, information retrieval, and client follow-up inefficient. Law.m was created to centralize that information into a single web application with a clean and intuitive interface.

Although this first version focuses on client management, the application was designed from the beginning with scalability in mind. The long-term goal is to transform it into a complete legal practice management system.

The current version includes secure user authentication and a fully functional client management module, allowing users to create, view, edit, and delete client records after logging into the system.


# Project Objective

The primary objective of Law.m was to develop a functional web application that demonstrates the concepts learned throughout CS50x, including Flask, SQLite, HTML, CSS, Bootstrap, authentication, and database management.

However, the true purpose of this project extends beyond the course itself.

Law.m represents the foundation of a long-term personal project that will continue evolving after completing CS50x. My goal is to transform this initial version into a comprehensive management system for law firms that can eventually be used in real professional environments.

Rather than being developed solely to satisfy the course requirements, Law.m was conceived as the beginning of a larger software project that will continue growing as I gain more experience in both Software Development Engineering and Law.



# Current Features

The current version includes:

- User registration.
- User authentication.
- Secure logout.
- Password hashing using Werkzeug Security.
- Protected routes.
- Dashboard.
- Client registration.
- Client listing.
- Client editing.
- Client deletion with confirmation.
- Flash success messages.
- Responsive interface built with Bootstrap 5.

Although the Dashboard already displays future modules such as Cases, Hearings, and Documents, these are intentionally presented as upcoming features to illustrate the long-term architecture of the system.


# Technologies Used

Law.m was developed using the following technologies:

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Werkzeug Security

These technologies were selected because they provide an excellent balance between simplicity, maintainability, and scalability for this stage of the project.


# Project Structure

The following files represent the core of the application.

## app.py

The main application file. It contains the Flask configuration, database connection, authentication system, and all application routes.

## schema.sql

Defines the database schema by creating the necessary tables for users and clients.

## crear_db.py

Automatically creates the SQLite database by executing the SQL statements contained in `schema.sql`.

## lawm.db

SQLite database that stores all user accounts and client information.

## templates/

Contains every HTML template rendered by Flask, including authentication pages, the dashboard, and client management views.

## static/

Stores all static project resources.

### static/css/

Contains the custom stylesheet responsible for maintaining the application's visual identity.

## README.md

Provides detailed documentation about the project, including its purpose, technologies, architecture, design decisions, and future plans.


# Design Decisions

Several design decisions were made to keep the application organized, maintainable, and prepared for future growth.

## Why Flask?

Flask was selected because of its lightweight architecture, flexibility, and excellent integration with Python. It allows the application to remain easy to understand while providing enough scalability for future development.

## Why SQLite?

SQLite was chosen because it requires no separate database server, making deployment straightforward and ideal for both an academic project and the first version of a legal management system.

Future versions may migrate to PostgreSQL or MySQL if the application grows significantly.

## Why Bootstrap?

Bootstrap allowed the development of a clean, responsive, and modern user interface while reducing development time.

## Why use layout.html?

A shared template was implemented to eliminate duplicated HTML code across different pages.

Using a common layout greatly simplifies maintenance since modifications made to the base template automatically propagate throughout the application.

## Why implement authentication?

Legal information often contains confidential client data.

For this reason, secure authentication was implemented using hashed passwords and protected routes, preventing unauthorized access to the application.

## Why begin with only the Client module?

Although the long-term vision includes additional modules such as Cases, Hearings, and Documents, the decision was made to first complete one module with high quality instead of partially implementing several.

This approach resulted in a stable, polished client management system that serves as the foundation for future development.


# Challenges

Developing Law.m involved several technical challenges that strengthened my understanding of web application development.

Among the most significant challenges were designing the database structure, integrating Flask with SQLite, implementing secure authentication, organizing reusable templates with Jinja, and debugging routing, SQL, and rendering issues.

Each challenge contributed to improving both my programming skills and my problem-solving abilities.


# Future Improvements

The current version fulfills the objectives established for the CS50x final project. However, development will continue beyond the course.

Future versions may include:

- Case management.
- Document management.
- PDF uploads.
- Hearing scheduling.
- Legal calendar.
- Notifications and reminders.
- User roles and permissions.
- Advanced search.
- Reporting tools.
- Automatic backups.
- Cloud integration.
- Additional security improvements.


# Project Vision

Although Law.m was developed as the final project for CS50x, it represents much more than an academic assignment.

From the beginning, it was conceived as the first stage of a long-term personal software project whose objective is to become a complete legal practice management system.

The current version establishes a solid foundation that will continue evolving as I advance in my studies in **Software Development Engineering** and **Law**. My goal is to combine knowledge from both fields to build practical technological solutions for legal professionals.

Rather than ending with the completion of CS50x, Law.m marks the beginning of a continuous development process.

# Name Origin

The name **Law.m** was carefully chosen to create a distinctive identity for the project.

The word **"Law"** represents the legal field for which the application was developed, while the **".m"** was intentionally added as a reference to my surname, **Morato**. This decision allowed the project to maintain a professional image while also giving it a unique personal identity.

From the beginning, Law.m was envisioned not simply as the title of an academic assignment but as the brand of a software project with long-term potential.

My intention is for Law.m to continue growing through future versions until it becomes a comprehensive legal management platform capable of providing real value to lawyers and law firms.

This project therefore represents not only the completion of CS50x, but also the starting point of a personal initiative that I plan to continue developing well beyond this course.

# Español

#### Descripción

Law.m es una aplicación web desarrollada como proyecto final para el curso **CS50x de Harvard University**. Su propósito principal es ofrecer una plataforma sencilla, organizada y segura para la administración de clientes dentro de un despacho jurídico.

La idea de este proyecto nació al observar que muchos despachos jurídicos pequeños y medianos aún administran la información de sus clientes mediante hojas de cálculo, documentos de texto o incluso registros físicos. Estos métodos suelen dificultar la organización, la búsqueda de información y el seguimiento de los asuntos de cada cliente. Como resultado, el trabajo diario puede volverse menos eficiente y más propenso a errores.

Con el desarrollo de Law.m se buscó crear una solución que centralizara toda esa información en un solo lugar mediante una interfaz intuitiva y fácil de utilizar. Aunque esta primera versión se enfoca únicamente en la gestión de clientes, desde el inicio el proyecto fue diseñado pensando en convertirse en un sistema mucho más amplio para la administración integral de despachos jurídicos.

Actualmente el sistema permite registrar usuarios, iniciar sesión de forma segura, administrar clientes mediante operaciones de creación, consulta, edición y eliminación, así como proteger toda la información mediante autenticación de usuarios.

# Objetivo del proyecto

El objetivo principal de Law.m fue desarrollar una aplicación web funcional que demostrara la integración de los conocimientos adquiridos durante CS50x, incluyendo desarrollo web con Flask, bases de datos SQLite, HTML, CSS, Bootstrap y autenticación de usuarios.

Sin embargo, el verdadero objetivo del proyecto va mucho más allá del curso.

Law.m representa el inicio de un proyecto personal que continuará desarrollándose después de la finalización de CS50x. Mi intención es aprovechar esta primera versión como una base sólida para construir un sistema jurídico mucho más completo, capaz de ser utilizado por abogados y despachos jurídicos reales.

Este proyecto no fue concebido únicamente para cumplir con un requisito académico o para obtener el certificado del curso. Desde el principio fue pensado como el punto de partida de una plataforma profesional que seguirá creciendo mediante la incorporación de nuevas funcionalidades y mejoras constantes.

Como estudiante de Ingeniería en Desarrollo de Software y Licenciatura en Derecho, considero que este proyecto representa la oportunidad perfecta para combinar ambas disciplinas y desarrollar herramientas tecnológicas que puedan aportar soluciones reales al ámbito jurídico.

# Funcionalidades actuales

La versión presentada para CS50x incluye las siguientes funcionalidades:

- Registro de usuarios.
- Inicio de sesión.
- Cierre de sesión.
- Contraseñas protegidas mediante hash utilizando Werkzeug Security.
- Protección de rutas para impedir el acceso sin autenticación.
- Dashboard principal.
- Registro de nuevos clientes.
- Consulta de clientes registrados.
- Edición de información de clientes.
- Eliminación de clientes con confirmación.
- Mensajes de confirmación utilizando Flask Flash.
- Interfaz moderna y adaptable desarrollada con Bootstrap 5.

Aunque el Dashboard muestra módulos como Expedientes, Audiencias y Documentos, estos permanecen como futuras extensiones del sistema y fueron incluidos para reflejar la arquitectura y visión general del proyecto.

# Tecnologías utilizadas

Para el desarrollo de Law.m se utilizaron las siguientes tecnologías:

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Werkzeug Security

Cada una de estas tecnologías fue seleccionada por su facilidad de integración, estabilidad y capacidad para construir una aplicación web ligera, organizada y escalable.


# Estructura del proyecto

Uno de los requisitos del proyecto final consiste en explicar la función de los archivos principales. A continuación se describe la estructura general del sistema.

## app.py

Es el archivo principal de la aplicación. Contiene la configuración de Flask, la conexión con la base de datos, la autenticación de usuarios y todas las rutas del sistema. Desde este archivo se controla el funcionamiento completo de Law.m.

## schema.sql

Define la estructura de la base de datos. En este archivo se crean las tablas utilizadas por la aplicación, incluyendo las tablas de usuarios y clientes.

## crear_db.py

Este archivo ejecuta automáticamente el contenido de `schema.sql` para generar la base de datos SQLite utilizada por la aplicación.

## lawm.db

Es la base de datos SQLite donde se almacena toda la información registrada por los usuarios, incluyendo cuentas y clientes.

## templates/

Esta carpeta contiene todas las plantillas HTML utilizadas por Flask para construir la interfaz del sistema. Incluye las páginas de inicio, autenticación, dashboard, administración de clientes y las diferentes vistas utilizadas por la aplicación.

## static/

Contiene todos los archivos estáticos del proyecto.

### static/css/

Almacena la hoja de estilos personalizada (`estilos.css`), encargada de mantener una apariencia uniforme en toda la aplicación.

## README.md

Este documento explica el funcionamiento del proyecto, las tecnologías utilizadas, las decisiones de diseño adoptadas durante el desarrollo y la visión futura de Law.m.


# Decisiones de diseño

Durante el desarrollo de Law.m se tomaron diversas decisiones de diseño con el objetivo de construir una aplicación organizada, fácil de mantener y con posibilidades de crecimiento en el futuro.

## ¿Por qué Flask?

Flask fue elegido como framework principal debido a su simplicidad, flexibilidad y excelente integración con Python. Al ser un framework ligero, permite comprender con claridad cómo interactúan las rutas, las plantillas HTML y la base de datos, además de facilitar la incorporación de nuevas funcionalidades conforme el proyecto evolucione.

Otra razón importante fue que Flask es una tecnología ampliamente utilizada para el desarrollo de aplicaciones web pequeñas y medianas, por lo que resulta una excelente base para continuar ampliando Law.m en futuras versiones.


## ¿Por qué SQLite?

SQLite fue seleccionado como motor de base de datos porque no requiere la instalación ni configuración de un servidor independiente. Esto permite que la aplicación pueda ejecutarse fácilmente en cualquier equipo simplemente contando con los archivos del proyecto.

Además, para una primera versión del sistema, SQLite ofrece un excelente equilibrio entre simplicidad, rendimiento y facilidad de mantenimiento.

En futuras versiones del proyecto podría migrarse a motores de bases de datos como PostgreSQL o MySQL si el crecimiento del sistema así lo requiere.

## ¿Por qué Bootstrap?

El objetivo fue desarrollar una interfaz moderna, limpia y adaptable sin invertir una gran cantidad de tiempo construyéndola completamente desde cero.

Bootstrap permitió crear una experiencia visual consistente, responsiva y agradable para el usuario, facilitando además futuras modificaciones en el diseño del sistema.


## ¿Por qué utilizar layout.html?

Durante el desarrollo observe que muchas páginas compartían exactamente la misma estructura, incluyendo la barra de navegación, la carga de Bootstrap, la hoja de estilos y otros elementos comunes.

Para evitar la duplicación de código se implementó una plantilla base llamada **layout.html**, la cual es heredada por las demás vistas mediante Jinja.

Esta decisión facilita enormemente el mantenimiento del proyecto, ya que cualquier modificación realizada en la plantilla principal se refleja automáticamente en todas las páginas del sistema.


## ¿Por qué implementar autenticación?

La información almacenada por un despacho jurídico puede contener datos personales y confidenciales de sus clientes.

Por esta razón se implementó un sistema de autenticación mediante usuarios y contraseñas cifradas utilizando Werkzeug Security.

Las contraseñas nunca se almacenan en texto plano, sino mediante funciones hash, incrementando así la seguridad de la aplicación.

Además, todas las rutas sensibles fueron protegidas para impedir que usuarios no autenticados puedan acceder directamente mediante la URL.


## ¿Por qué comenzar únicamente con el módulo de Clientes?

Desde el inicio del proyecto se contempló el desarrollo de módulos adicionales como Expedientes, Audiencias y Documentos.

Sin embargo, se tomó la decisión de concentrar el desarrollo en un único módulo completamente funcional antes de comenzar nuevas funcionalidades.

Esta decisión me permitió dedicar más tiempo a mejorar la calidad del código, la organización de la aplicación, la experiencia de usuario y la estabilidad del sistema.

Como resultado, la primera versión de Law.m presenta un módulo de clientes completamente operativo que servirá como base para el crecimiento del proyecto.

## ¿Por qué mostrar módulos aún no implementados?

El Dashboard incluye secciones correspondientes a Expedientes, Audiencias y Documentos, aunque actualmente aparecen como módulos "Próximamente".

La intención fue mostrar la arquitectura general del sistema y reflejar la visión completa del proyecto desde sus primeras versiones.

Esto permite que la aplicación tenga una estructura preparada para incorporar nuevas funcionalidades sin necesidad de rediseñar completamente la interfaz.

# Retos encontrados durante el desarrollo

El desarrollo de Law.m representó diversos desafíos técnicos que permitieron fortalecer mis conocimientos adquiridos durante CS50x.

Uno de los principales retos consistió en diseñar correctamente la estructura de la base de datos y lograr una integración adecuada entre Flask, SQLite y las plantillas HTML.

También fue necesario comprender el funcionamiento de la autenticación de usuarios, el manejo de sesiones, la protección de rutas y el almacenamiento seguro de contraseñas mediante funciones hash.

Otro desafío importante fue organizar correctamente el proyecto utilizando una plantilla base (`layout.html`) para evitar la duplicación de código y facilitar el mantenimiento futuro.

Además, durante el desarrollo fue necesario solucionar distintos errores relacionados con rutas, estructura de la base de datos, consultas SQL y renderizado de plantillas, lo que permitió adquirir una mejor comprensión del proceso completo de desarrollo de aplicaciones web.

Cada uno de estos retos contribuyó significativamente a mejorar tanto mis habilidades de programación como mi capacidad para analizar y resolver problemas.

# Mejoras futuras

Aunque la versión actual cumple plenamente con los objetivos establecidos para el proyecto final de CS50x, el desarrollo de Law.m continuará después de la finalización del curso.

Entre las funcionalidades planeadas se encuentran:

- Administración completa de expedientes.
- Gestión documental con carga de archivos PDF.
- Calendario de audiencias.
- Agenda jurídica.
- Recordatorios automáticos.
- Historial completo de actividades.
- Panel administrativo.
- Control de usuarios mediante roles y permisos.
- Búsqueda avanzada de clientes y expedientes.
- Generación de reportes.
- Respaldo automático de la información.
- Integración con servicios en la nube.
- Mejoras continuas en seguridad y rendimiento.

Estas funcionalidades permitirán que Law.m evolucione gradualmente hasta convertirse en una plataforma integral para despachos jurídicos.

# Visión del proyecto

Aunque Law.m fue desarrollado como proyecto final para CS50x, este proyecto representa mucho más que una entrega académica.

Desde el inicio fue concebido como el primer paso de un proyecto personal de largo plazo cuyo objetivo es desarrollar un sistema profesional para la administración de despachos jurídicos.

La versión presentada constituye únicamente la primera etapa de ese proceso. Mi intención es continuar desarrollándolo durante mi formación universitaria y después de ella, incorporando nuevas tecnologías, mejores prácticas de desarrollo de software y funcionalidades que respondan a las necesidades reales de abogados y despachos jurídicos.

Como estudiante de Ingeniería en Desarrollo de Software y Licenciatura en Derecho, considero que Law.m representa la oportunidad de integrar ambas áreas de conocimiento para construir soluciones tecnológicas con una aplicación práctica dentro del ámbito jurídico.

Más que concluir con la obtención del certificado de CS50x, este proyecto marca el inicio de un camino de aprendizaje continuo y de la construcción de un sistema que aspira a tener un impacto real en el ejercicio profesional del Derecho.

# Origen del nombre

El nombre **Law.m** fue elegido con el propósito de crear una identidad propia para el proyecto.

La palabra **"Law"** representa el ámbito jurídico al que está dirigida la aplicación, mientras que la **".m"** fue incorporada como un elemento distintivo inspirado en mi apellido, **Morato**. Esta decisión buscó darle al proyecto una identidad personal sin perder una imagen profesional y fácilmente reconocible.

Más que un nombre para un proyecto académico, **Law.m** fue concebido como una marca con potencial de crecimiento. Desde el inicio, la intención fue desarrollar una plataforma que pudiera evolucionar con el tiempo y convertirse en un sistema cada vez más completo para la administración de despachos jurídicos.

La elección del nombre también refleja mi deseo de construir un proyecto propio que trascienda el curso CS50x. Conforme adquiera nuevos conocimientos y experiencia en el desarrollo de software y en el ámbito jurídico, Law.m continuará incorporando nuevas funcionalidades y mejorando su arquitectura con el objetivo de ofrecer una solución tecnológica útil para abogados y profesionales del Derecho.

En ese sentido, Law.m representa no solo un proyecto universitario, sino el inicio de una iniciativa personal con una visión de largo plazo, en la que cada nueva versión contribuirá a consolidarlo como un sistema profesional para la gestión jurídica.