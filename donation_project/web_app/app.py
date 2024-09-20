```python
# web_app/app.py
from flask import Flask, render_template, request, redirect, url_for
from donation_app.donor import save_donor
from donation_app.donation import save_donation, get_donations

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        save_donor(name, email, password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implementar lógica de login
    return render_template('login.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        donor_id = request.form['donor_id']
        donation_type = request.form['donation_type']
        address = request.form['address']
        amount = request.form['amount']
        payment_method = request.form['payment_method']
        save_donation(donor_id, donation_type, address, amount, payment_method)
        return redirect(url_for('donation_list'))
    return render_template('donate.html')

@app.route('/donations')
def donation_list():
    donations = get_donations()
    return render_template('donation_list.html', donations=donations)

if __name__ == '__main__':
    app.run(debug=True)
```



