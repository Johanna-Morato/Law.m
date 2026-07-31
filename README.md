# Law.m

## Legal Management Web Application

### Demo
[Watch the project demonstration](https://youtu.be/pnKx7h8LpEU)

## Overview

Law.m is a web application designed to help legal professionals organize and manage client information through a simple, secure, and intuitive platform.

The project was created to address a common challenge in small and medium-sized law firms: managing client information through spreadsheets, documents, or physical records, which can make organization and information retrieval difficult.

Law.m centralizes client management into a web application, providing a foundation for a future legal practice management system that can include additional modules such as cases, documents, hearings, and scheduling.

This project was initially developed as the final project for **Harvard University's CS50x: Introduction to Computer Science**, and it continues as a personal software project within my development portfolio.

## Features

Current functionality includes:

- User registration.
- Secure user authentication.
- Password hashing with Werkzeug Security.
- Protected routes.
- Dashboard interface.
- Client registration.
- Client listing.
- Client editing.
- Client deletion with confirmation messages.
- Responsive interface using Bootstrap 5.

The current architecture was designed with future expansion in mind, including modules for cases, documents, hearings, and other legal workflow tools.

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Werkzeug Security

## Project Structure

The main structure of the application is:

```text
Law.m/
│
├── app.py
├── create_db.py
├── schema.sql
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── clients.html
│   ├── new_client.html
│   └── edit_client.html
│
└── static/
    └── styles.css

```

## Database

Law.m uses SQLite as its database solution.

The database structure is defined in `schema.sql`, which contains the required tables for user authentication and client management.

A database creation script is included to simplify the setup process.


## Design Decisions

### Why Flask?

Flask was selected because of its lightweight architecture, flexibility, and strong integration with Python. It provides a simple but powerful foundation for building scalable web applications.

### Why SQLite?

SQLite was chosen because it is easy to configure and maintain, making it ideal for the initial version of this application.

Future versions may migrate to larger database systems such as PostgreSQL or MySQL depending on project requirements.

### Why Authentication?

Since legal information can contain sensitive data, authentication was implemented with password hashing and protected routes to improve application security.

### Why Start with Client Management?

Instead of creating multiple incomplete modules, development focused first on building a complete and functional client management system. This approach creates a stronger foundation for future features.


## Challenges and Learning

Developing Law.m helped strengthen my knowledge of:

- Backend development with Flask.
- Database design and SQL.
- Authentication systems.
- Template organization with Jinja2.
- Debugging web applications.
- Building complete applications from concept to implementation.


## Future Improvements

Planned improvements include:

- Case management.
- Document management.
- PDF uploads.
- Hearing scheduling.
- Legal calendar.
- Notifications and reminders.
- User roles and permissions.
- Advanced search.
- Reporting tools.
- Cloud integration.
- Additional security improvements.


## Project Vision

Law.m represents the beginning of a long-term project focused on combining software development and legal knowledge to create practical technological solutions for legal professionals.

The goal is to continue evolving this platform into a complete legal practice management system capable of improving organization, efficiency, and accessibility within law firms.


## Name Origin

The name **Law.m** combines the purpose of the application with a personal identity.

"Law" represents the legal field, while ".m" references my surname, **Morato**, giving the project a distinctive and personal brand.

Law.m is not only a completed academic project, but the foundation of a software product that I intend to continue developing.
