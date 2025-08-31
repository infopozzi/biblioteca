from flask import Blueprint, render_template, request, session, redirect, flash

login_route = Blueprint('login', __name__)

@login_route.route('/')
def login():
    return render_template('login.html')

@login_route.route('/entrar', methods=["POST"])
def entrar():
    login = request.form['login']
    senha = request.form['senha']
    session['usuario'] = login

    flash('usuario invalido')
    return redirect('/login')
    
    
@login_route.route('/logout')
def logout():
    session['usuario'] = None
    return redirect('/login')