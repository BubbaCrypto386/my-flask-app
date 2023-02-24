from flask import Flask, render_template, request

app = Flask(__name__)

# A dictionary of menu items and their corresponding URLs
menu_items = {
    "AirBnb": "/airbnb",
    "Turo": "/turo",
    "Instagram Reels": "/reels",
    "YT Shorts": "/shorts",
    "Youtube Videos": "/videos",
    "Amazon KDP": "/kdp",
    "Wholesale": "/wholesale",
    "SaaS": "/saas",
    "Real Estate": "/realestate",
    "Snapchat": "/snapchat",
    "Consulting": "/consulting",
    "Lead Generation": "/leadgen",
    "Crypto": "/crypto",
    "Apps": "/apps"
}

@app.route("/")
def index():
    return render_template("index.html", menu_items=menu_items)

@app.route("/airbnb")
def airbnb():
    return render_template("airbnb.html", menu_items=menu_items)

@app.route("/turo")
def turo():
    return render_template("turo.html", menu_items=menu_items)

@app.route("/reels")
def reels():
    return render_template("reels.html", menu_items=menu_items)

@app.route("/shorts")
def shorts():
    return render_template("shorts.html", menu_items=menu_items)

@app.route("/videos")
def videos():
    return render_template("videos.html", menu_items=menu_items)

@app.route("/kdp")
def kdp():
    return render_template("kdp.html", menu_items=menu_items)

@app.route("/wholesale")
def wholesale():
    return render_template("wholesale.html", menu_items=menu_items)

@app.route("/saas")
def saas():
    return render_template("saas.html", menu_items=menu_items)

@app.route("/realestate")
def realestate():
    return render_template("realestate.html", menu_items=menu_items)

@app.route("/snapchat")
def snapchat():
    return render_template("snapchat.html", menu_items=menu_items)

@app.route("/consulting")
def consulting():
    return render_template("consulting.html", menu_items=menu_items)

@app.route("/leadgen")
def leadgen():
    return render_template("leadgen.html", menu_items=menu_items)

@app.route("/crypto")
def crypto():
    return render_template("crypto.html", menu_items=menu_items)

@app.route("/apps")
def apps():
    return render_template("apps.html", menu_items=menu_items)

if __name__ == "__main__":
    app.run(debug=True)
