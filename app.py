from flask import Flask, render_template

app = Flask(__name__)


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

@app.route('/contato/')
def contato():
    return render_template('contato.html')




if __name__ == '__main__':
    app.run()
