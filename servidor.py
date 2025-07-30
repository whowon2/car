from flask import Flask, request, send_file
import serial

app = Flask(__name__)
# arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
arduino = serial.Serial('COM3', 9600, timeout=1)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/comando')
def comando():
    acao = request.args.get('acao')
    if acao in ['frente', 're', 'direita', 'esquerda', 'parar']:
        arduino.write((acao + '\n').encode())
        return f"Comando enviado: {acao}"
    return "Comando inválido"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
