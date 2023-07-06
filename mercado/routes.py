from mercado import app
from flask import render_template, redirect, url_for, flash
from mercado.models import Item, User
from mercado.forms import Cadastroform, Loginform
from mercado import db
from flask_login import login_user

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)

@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = Cadastroform()
    if form.validate_on_submit():
        usuario = User(
            usuario=form.usuario.data,
            email=form.email.data,
            senhacrip = form.senhal.data
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produto'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário {err}", category="danger")
    return render_template("cadastro.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = Loginform()
    if form.validate_on_submit():
        usuario_logado = User.query.filter_by(usuario=form.usuario.data).first()
        if usuario_logado and usuario_logado.converte_senha(senha_texto_claro=form.senha.data):
            login_user(usuario_logado)
            flash(f'Sucesso! seu login é: {usuario.logado.usuario}', category="success")
            return redirect(url_for('page_produto'))
        else:
            flash(f"Usuário ou senha incorretos! Tente novamente", category="danger")
    return render_template("login.html", form=form)