from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
from flask import send_file
from flask_material import Material 



import user_analysis_report as report1
#import list_apps as report2
import user_schema as process_schema


app = Flask(__name__)
Material(app)
properties = []

@app.route('/logs')
def logs():
    return render_template('temp_logs.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thank-you1')
def thank_you1():
    path =request.args.get('path')
    if(len(path)>0):
        return send_file(path, as_attachment=True)
    return render_template('report.html', message=error)


@app.route('/thank-you',methods=['GET', 'POST'])
def thank_you():
    error=""
    #path=request.args.get('path')
    schema_attributes = properties[2]
    if request.method == 'POST':
            # Form being submitted; grab data from form.
            choices = request.form.getlist("chosen_attr")
            print("CHOICESS:",choices)
            if len(choices) == 0:
                # Form data failed validation; try again
                error = "Please supply atleast one value you would like to be represented in the excel sheet"
            else:
                print(choices)
                attribute_inputs = report1.main(properties[0],properties[1],choices)
                path = attribute_inputs
                return redirect(url_for('thank_you1',path=path))

    return render_template('thank-you.html', message=error)


def get_properties():
    temp_list = properties[2]
    n = 4 
    final = [temp_list[i * n:(i + 1) * n] for i in range((len(temp_list) + n - 1) // n )]
    print("FINALLL",final)
    return final;


            
def get_file():
    return file

@app.context_processor
def context_processor():
    return dict(get_properties=get_properties)


@app.route('/report1', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        Okta_tenant = request.form['okta_tenantname']
        API_token = request.form['APITokenname']

        # Validate form data
        if len(Okta_tenant) == 0 or len(API_token) == 0:
            error = "Please supply both Okta tenant URL and token value"
        else:
            attribute_inputs = process_schema.main(Okta_tenant,API_token)
            properties.append(Okta_tenant)
            properties.append(API_token)
            properties.append(attribute_inputs)
            return redirect(url_for('thank_you'))

    # Render the sign-up page
    return render_template('sign-up.html', message=error)



@app.route('/report2', methods=['GET', 'POST'])
def know_your_applications():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        Okta_tenant = request.form['okta_tenantname']
        API_token = request.form['APITokenname']

        # Validate form data
        if len(Okta_tenant) == 0 or len(API_token) == 0:
            error = "Please supply both Okta tenant URL and token value"
        else:
            result = report2.main(Okta_tenant,API_token)
            #return redirect(url_for('applications'))
       
    # Render the sign-up page
    return render_template('sign-up.html', message=error)


# Run the application
app.run(host='0.0.0.0', port=5000,debug=True)
