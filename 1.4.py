from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def start():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!1"


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства.',
           'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
           'Присоединяйся!']
    return '</br>'.join(lst)


@app.route('/image_mars')
def image():
    img = f'''<img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title> Марс!</title>
                  </head>
                  <body>
                    <h1> Жди нас, Марс! <h1>
                    <h1> {img} </h1>
                  </body>
                </html>"""

@app.route('/promotion_image')
def bootstrap():
    img = f'''<img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">'''
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства
                    </div>
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
