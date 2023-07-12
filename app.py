from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_profits(data):
    money = int(data['money'])
    gold_bars = int(data['gold_bars'])
    diamonds = int(data['diamonds'])
    cookies = int(data['cookies'])
    energy_drinks = int(data['energy_drinks'])
    jewelry = int(data['jewelry'])
    bombs_bought = int(data['bombs_bought'])

    gold_value = gold_bars * 1000
    diamonds_value = diamonds * 1800
    bombs_cost = bombs_bought * 1800
    cookies_value = cookies * 450
    energy_drinks_value = energy_drinks * 400
    jewelry_value = jewelry * 400
    profits = (gold_value + diamonds_value + money + cookies_value + energy_drinks_value + jewelry_value) - bombs_cost

    return profits, gold_value, diamonds_value, cookies_value, energy_drinks_value, jewelry_value, -bombs_cost

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = {
            'money': request.form['money'],
            'gold_bars': request.form['gold_bars'],
            'diamonds': request.form['diamonds'],
            'cookies': request.form['cookies'],
            'energy_drinks': request.form['energy_drinks'],
            'jewelry': request.form['jewelry'],
            'bombs_bought': request.form['bombs_bought']
        }
        profits, gold_value, diamonds_value, cookies_value, energy_drinks_value, jewelry_value, bombs_cost = calculate_profits(data)

        return render_template('result.html', profits=profits, gold_value=gold_value, diamonds_value=diamonds_value,
                               cookies_value=cookies_value, energy_drinks_value=energy_drinks_value,
                               jewelry_value=jewelry_value, bombs_cost=bombs_cost)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
