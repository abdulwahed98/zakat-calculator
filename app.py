from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_zakat', methods=['POST'])
def calculate_zakat():
    cash_at_home = float(request.form['cash_at_home'])
    bank_balance = float(request.form['bank_balance'])
    gold_value = float(request.form['gold_value'])
    silver_value = float(request.form['silver_value'])
    property_value = float(request.form['property_value'])
    num_goats_sheep = int(request.form['num_goats_sheep'])

    total_wealth = cash_at_home + bank_balance + gold_value + silver_value + property_value
    zakat_owed = 0

    if total_wealth >= 20 * 3.75:  # Nisab for gold is 7.5 tola
        zakat_owed = (total_wealth * 0.025)  # 2.5% of total wealth

    zakat_owed += num_goats_sheep // 40  # Zakat for goats/sheep

    return render_template('result.html', zakat_owed=zakat_owed)

if __name__ == '__main__':
    app.run(debug=True)
