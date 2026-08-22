from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("mapa.html")


@app.route("/ubicacion", methods=["POST"])
def recibir_ubicacion():

    datos = request.get_json()

    print("📍 Ubicación recibida:")
    print(datos)

    return jsonify({
        "ok": True,
        "mensaje": "Ubicación recibida correctamente"
    })


if __name__ == "__main__":
    app.run(debug=True)