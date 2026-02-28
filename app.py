from flask import Flask, render_template, request

app = Flask(__name__)

ZAKAT_RATE = 0.025  # 2.5%

@app.route("/", methods=["GET", "POST"])
def home():
    # default values (so page never blank)
    cash = 0.0
    metals = 0.0
    debts = 0.0
    nisab = 0.0
    net_assets = 0.0
    zakat = None
    eligible = False

    if request.method == "POST":
        cash = float(request.form.get("cash", 0) or 0)
        metals = float(request.form.get("metals", 0) or 0)
        debts = float(request.form.get("debts", 0) or 0)
        nisab = float(request.form.get("nisab", 0) or 0)

        net_assets = max(0.0, cash + metals - debts)
        eligible = net_assets >= nisab

        zakat = net_assets * ZAKAT_RATE if eligible else 0.0

    return render_template(
        "index.html",
        cash=cash,
        metals=metals,
        debts=debts,
        nisab=nisab,
        net_assets=net_assets,
        zakat=zakat,
        eligible=eligible,
    )

if __name__ == "__main__":
    app.run(debug=True)