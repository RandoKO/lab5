from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/name/<name>', methods=['GET'])
def ejemplo(name):
    return f"Hola, {name}"

@app.route('/palindromo/<palabra>', methods=['GET'])
def ejercicio1(palabra):
    if palabra == palabra[::-1]:
        return("Es palindroma")
    else:
        return("No es palindroma")

@app.route('/operaciones/<num1>/<num2>', methods=['GET'])
def ejercicio2(num1, num2):
    resultado = int(num1) + int(num2)
    resultado2 = int(num1) - int(num2)
    resultado3 = int(num1) * int(num2)
    resultado4 = int(num1) / int(num2)
    return "Suma: " + str(resultado) + ", Resta: " +str(resultado2) + ", Multiplicación: " + str(resultado3) + ", División: "+ str(resultado4)

@app.route('/ordenar/<a>/<b>/<c>', methods=['GET'])
def ejercicio3(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return str(numbers)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
