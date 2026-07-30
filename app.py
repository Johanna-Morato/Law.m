from flask import Flask, render_template, request, redirect, session, flash, url_for
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps


def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if session.get("user_id") is None:
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return decorated_function


app = Flask(__name__)
app.secret_key = "lawm"

db = SQL("sqlite:///lawm.db")


@app.route("/")
def inicio():

    return render_template("inicio.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        correo = request.form.get("correo")
        contraseña = request.form.get("contraseña")

        if not correo:

            return render_template(
                "login.html",
                mensaje="Debes escribir un correo"
            )

        if not contraseña:

            return render_template(
                "login.html",
                mensaje="Debes escribir una contraseña"
            )


        usuario = db.execute(
            "SELECT * FROM usuarios WHERE correo = ?",
            correo
        )


        if len(usuario) == 0:

            return render_template(
                "login.html",
                mensaje="Correo no registrado."
            )


        if not check_password_hash(usuario[0]["hash"], contraseña):

            return render_template(
                "login.html",
                mensaje="Contraseña incorrecta."
            )


        session["user_id"] = usuario[0]["id"]

        return redirect(url_for("dashboard"))


    return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        password = request.form.get("password")
        confirmacion = request.form.get("confirmacion")


        if not nombre:

            return render_template(
                "register.html",
                mensaje="Ingresa tu nombre."
            )


        if not correo:

            return render_template(
                "register.html",
                mensaje="Ingresa tu correo."
            )


        if not password:

            return render_template(
                "register.html",
                mensaje="Ingresa una contraseña."
            )


        if password != confirmacion:

            return render_template(
                "register.html",
                mensaje="Las contraseñas no coinciden."
            )


        usuario = db.execute(
            "SELECT * FROM usuarios WHERE correo = ?",
            correo
        )


        if len(usuario) != 0:

            return render_template(
                "register.html",
                mensaje="Ese correo ya existe."
            )


        hash = generate_password_hash(password)


        db.execute(
            """
            INSERT INTO usuarios (nombre, correo, hash)
            VALUES (?, ?, ?)
            """,
            nombre,
            correo,
            hash
        )


        return redirect(url_for("login"))


    return render_template("register.html")



@app.route("/dashboard")
@login_required
def dashboard():

    return render_template("dashboard.html")

@app.route("/clientes")
@login_required
def clientes():

    clientes = db.execute(
        "SELECT * FROM clientes ORDER BY nombre"
    )


    return render_template(
        "clientes.html",
        clientes=clientes
    )



@app.route("/clientes/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_cliente():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        correo = request.form.get("correo")
        direccion = request.form.get("direccion")
        observaciones = request.form.get("observaciones")


        if not nombre:

            return render_template(
                "nuevo_cliente.html",
                mensaje="Inserte el nombre."
            )


        db.execute(
            """
            INSERT INTO clientes
            (nombre, telefono, correo, direccion, observaciones)

            VALUES (?, ?, ?, ?, ?)
            """,
            nombre,
            telefono,
            correo,
            direccion,
            observaciones
        )


        flash(
            "Cliente registrado correctamente.",
            "success"
        )


        return redirect(url_for("clientes"))


    return render_template("nuevo_cliente.html")



@app.route("/clientes/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_cliente(id):

    if request.method == "POST":

        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        correo = request.form.get("correo")
        direccion = request.form.get("direccion")
        observaciones = request.form.get("observaciones")


        if not nombre:

            cliente = db.execute(
                "SELECT * FROM clientes WHERE id = ?",
                id
            )[0]


            return render_template(
                "editar_cliente.html",
                mensaje="Debes escribir el nombre.",
                cliente=cliente
            )


        db.execute(
            """
            UPDATE clientes
            SET nombre = ?,
                telefono = ?,
                correo = ?,
                direccion = ?,
                observaciones = ?
            WHERE id = ?
            """,
            nombre,
            telefono,
            correo,
            direccion,
            observaciones,
            id
        )


        flash(
            "Cliente actualizado correctamente.",
            "success"
        )


        return redirect(url_for("clientes"))



    cliente = db.execute(
        "SELECT * FROM clientes WHERE id = ?",
        id
    )


    if len(cliente) == 0:

        return redirect(url_for("clientes"))


    return render_template(
        "editar_cliente.html",
        cliente=cliente[0]
    )



@app.route("/clientes/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_cliente(id):

    db.execute(
        "DELETE FROM clientes WHERE id = ?",
        id
    )


    flash(
        "Cliente eliminado correctamente.",
        "success"
    )


    return redirect(url_for("clientes"))



@app.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect(url_for("login"))



if __name__ == "__main__":

    app.run(debug=True, port=5001)