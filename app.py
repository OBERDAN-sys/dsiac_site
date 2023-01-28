import os
from flask import Flask, render_template, request
from forms import ContactForm
from flask_mail import Mail, Message



app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# Bootstrap(app)
# csrf.init_app(app)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sc.oberdan@gmail.com'
app.config['MAIL_PASSWORD'] = '922$Lenha'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre/')
def sobre():  # put application's code here
    return render_template('sobre.html')

@app.route('/solucao_item1/')
def solucao_item1():  # put application's code here
    return render_template('solucao_item1.html')

@app.route('/solucao_item2/')
def solucao_item2():  # put application's code here
    return render_template('solucao_item2.html')

@app.route('/solucao_item3/')
def solucao_item3():  # put application's code here
    return render_template('solucao_item3.html')

@app.route('/solucao_item4/')
def solucao_item4():  # put application's code here
    return render_template('solucao_item4.html')

@app.route('/segmentos_item1/')
def segmentos_item1():  # put application's code here
    return render_template('segmentos_item1.html')

@app.route('/segmentos_item2/')
def segmentos_item2():  # put application's code here
    return render_template('segmentos_item2.html')

@app.route('/segmentos_item3/')
def segmentos_item3():  # put application's code here
    return render_template('segmentos_item3.html')

@app.route('/segmentos_item4/')
def segmentos_item4():  # put application's code here
    return render_template('segmentos_item4.html')

@app.route('/segmentos_item5/')
def segmentos_item5():  # put application's code here
    return render_template('segmentos_item5.html')


@app.route('/tecnologias/')
def tecnologias():  # put application's code here
    return render_template('tecnologias.html')

@app.route('/contatos', methods=["GET", "POST"])
def get_contato():
    cform = ContactForm()
    if request.method == "POST":
        name = request.form["Nome"]
        email = request.form["Email"]
        subject = request.form["Assunto"]
        message = request.form["Mensagem"]

    return render_template('contato.html', form=cform)

def send_message(message1):

    msg = Message(subject=(f"{message1.get('Email')} quero contactar com vc desde app"),
                  sender=message1.get('Email'),
                  recipients=['sc.oberdan@gmail.com'], body=message1.get('Mensagem')
                  )
    mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
