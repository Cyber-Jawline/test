from flask import Flask, render_template, redirect, request, url_for, make_response
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods= ["POST", "GET"])
def home():
    if request.method == "POST":
        if 'getstarted' in request.form:
            return redirect('/choose')
    return render_template('home.html')

@app.route('/choose', methods = ["POST", "GET"])
def choose():
    if request.method == "POST":
        return redirect(url_for((list(request.form))[0]))
    return render_template('choose.html')

@app.route('/businesst', methods = ["POST", "GET"]) 
def businesst():
    if request.method == "POST":
        if 'add' in request.form:
            with open('templates/business.html', 'r') as f:
                contents = f.read()

            soup = BeautifulSoup(contents, 'html.parser')

            table = soup.find('table')

            new_row = soup.new_tag('tr')

            cells = ['<input type = "checkbox">', '<input type = "text">', '<input type = "datetime-local">', '<input type = "datetime-local">', '<input type="text">', '<select><option>High</option><option>Medium</option><option>Low</option></select>']
            for cell_content in cells:
                cell = soup.new_tag('td')
                cell.append(BeautifulSoup(cell_content, 'html.parser'))
                new_row.append(cell)

            # Append the new row to the table
            table.append(new_row)

            with open('templates/business.html', 'w') as f:  # Write changes to 'business.html'
                f.write(str(soup))

            # Set a cookie
            resp = make_response(render_template('business.html'))
            resp.set_cookie('table_updated', 'true')
            return resp

    return render_template('business.html')

@app.route('/schoolt')
def schoolt():
    pass

app.run(debug=True)
