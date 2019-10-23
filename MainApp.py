from flask import Flask, render_template

from forms import CreateAccount

#change link before uploading at 2 places createpage and linkpage

def generate_link(sender='', reciever='To Everyone'):
    sender = str(sender).lower().replace(" ", "-").strip()
    if reciever == "To everyone":
        return sender
    reciever = str(reciever).lower().replace(" ", "-").strip()
    return str(sender + "_" + reciever)


def to_and_from_selector(stringline):
    index = str(stringline).count("_")
    stringline = str(stringline).upper().replace("-", " ")
    if index == 0:
        return [str(stringline), "To everyone"]
    stringlist = str(stringline).split("_")
    return stringlist


def person_visited(stringname):
    with open("visited.txt", "a") as file:
        file.writelines("\n+1 " + str(stringname))


app = Flask(__name__)
app.config['SECRET_KEY'] = '8584dd1fff743cf1c9a5a1c70276c3ef'


@app.route("/<pagename>")
def mainpage(pagename):
    person_visited(pagename)
    person_list = to_and_from_selector(pagename)
    return render_template("mainapp-en.html", pgname="Happy Diwali - " + person_list[0], s_name=person_list[0],
                           r_name=person_list[1])


@app.route('/', methods=['GET', 'POST'])
@app.route('/create', methods=['GET', 'POST'])
def createpage():
    form_ca = CreateAccount()
    if form_ca.is_submitted():
        data = generate_link(form_ca.s_username.data, form_ca.r_username.data)
        greeting = "Hey,I have sent you a greeting card, check it out ! -> "
        return render_template("display_link.html", pgname="Share Link", link=greeting + "http://127.0.0.1:5000/"+data)
    return render_template("createdual.html", pgname="Create Card", form=form_ca)


@app.route('/about')
def aboutpage():
    return render_template("about.html", pgname="About Us")


@app.route('/link')
def linkpage(link = "http://127.0.0.1:5000/"):
    return render_template("display_link.html", pgname="Share Link" , link = link)


if __name__ == '__main__':
    app.run(debug=True)
