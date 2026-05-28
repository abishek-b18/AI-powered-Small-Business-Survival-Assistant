from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('models/business_risk_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():

    business = request.form['business']
    sales = float(request.form['sales'])
    expenses = float(request.form['expenses'])
    customers = float(request.form['customers'])
    profit = float(request.form['profit'])

    prediction = model.predict([[sales, expenses, customers, profit]])

    if prediction[0] == 1:
        result = "High Business Risk Detected"
    else:
        result = "Business is Performing Well"

    return render_template(
        'dashboard.html',
        business=business,
        result=result,
        sales=sales,
        expenses=expenses,
        customers=customers,
        profit=profit
    )

if __name__ == '__main__':
    app.run(debug=True)