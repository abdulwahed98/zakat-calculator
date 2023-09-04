from flask import Flask

app = Flask(__name__)

@app.route("/")
def calculate_zakat(cash_at_home, balance_in_bank, gold_value, silver_value, property_value, number_of_goats):
    total_wealth = cash_at_home + balance_in_bank + gold_value + silver_value + property_value
    zakat = 0
    
    if total_wealth >= 786000:  # Nisab value in INR
        zakat = total_wealth * 0.025  # Zakat is 2.5% of total wealth
        
    zakat_goats = number_of_goats // 40
    
    return zakat, zakat_goats

def main():
    cash_at_home = float(input("Enter cash at home (INR): "))
    balance_in_bank = float(input("Enter balance held in bank accounts (INR): "))
    gold_value = float(input("Enter gold value (INR): "))
    silver_value = float(input("Enter silver value (INR): "))
    property_value = float(input("Enter current value of property held as an investment (INR): "))
    number_of_goats = int(input("Enter number of goats/sheep: "))

    zakat, zakat_goats = calculate_zakat(cash_at_home, balance_in_bank, gold_value, silver_value, property_value, number_of_goats)

    print("Zakat amount: {:.2f} INR".format(zakat))
    print("Zakat on goats/sheep: {} goats/sheep".format(zakat_goats))

if __name__ == "__main__":
    main()