from flask import render_template, flash, redirect, url_for
from app.auth import auth
from app.auth.forms import LoginForm


# TODO login route register blueprint 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user is None or not user.check_password(form.password.data): # where does the check_password() come from
            flash(_('Incorrect password or email')) # why do we use _ here?
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', form=form)
        

#TODO logout route
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# TODO registration route 




# #TODO login form to be created
# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data.lower()).first()
#         if user is not None and user.verify_password(form.password.data):
#             login_user(user)
#             next = request.args.get('next')
#             if next is None or not next.startswith('/'):
#                 next = url_for('main.index')
#             return redirect(next)
#         flash('Invalid username or password.')
#     return render_template('auth/login.html', form=form)


# @auth.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
#     logout_user()
#     flash('you are no longer logged in')
#     return redirect(url_for('main.index'))


# #TODO register form to be created
# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         pass
#         return redirect(url_for('main.index'))
#     return render_template('auth/register.html', form=form)

# #TODO add User profile page use user.html file for tha