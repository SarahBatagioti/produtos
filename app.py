from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'fastfood'
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produto")
    produto = cur.fetchall()
    cur.close()
    return render_template('index.html', produto=produto)

@app.route('/add', methods=['POST'])
def add_produto():
    if request.method == 'POST':
        nomeProduto = request.form['nomeProduto']
        descricaoProduto = request.form['descricaoProduto']
        imagemProduto = request.form['imagemProduto']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO produto (nomeProduto, descricaoProduto, imagemProduto) VALUES (%s, %s, %s)", (nomeProduto, descricaoProduto, imagemProduto))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
