from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
from flask import send_file
from flask_material import Material 



import user_analysis_report as report1


app = Flask(__name__)
Material(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thank-you')
def thank_you():
    path =request.args.get('path')

    return send_file(path, as_attachment=True)


# Simple form handling using raw HTML forms
@app.route('/report1', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        Okta_tenant = request.form['okta_tenantname']
        API_token = request.form['APITokenname']

        # Validate form data
        if len(Okta_tenant) == 0 or len(API_token) == 0:
            # Form data failed validation; try again
            error = "Please supply both Okta tenant URL and token value"
        else:
            t = report1.main(Okta_tenant,API_token)
            path=t
            return redirect(url_for('thank_you',path=path))



    # Render the sign-up page
    return render_template('sign-up.html', message=error)

# More powerful approach using WTForms

# Run the application
app.run(port=5000,debug=True)
