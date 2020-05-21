from flask import Flask, render_template, url_for, redirect, request
from model_synthesis import make_predictions

app = Flask(__name__)
#static_folder = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predictonImage():
    if request.method == 'POST':
        f = request.files["xray"]
        if (f.filename == ""):
            return redirect('/')
        name = (f.filename).split(".")
        if (len(name) == 2 and (name[1] == "jpg" or name[1] == "png" or name[1] == "jpeg")):
            path = "./static/savedImgs/image.jpg"
            f.save(path)
            res = make_predictions(path)
            if res < 0.5:
                ans = "Covid Postive with a {:.1f}% probabality".format(
                    (1 - res)*100)
            else:
                ans = "Perfectly Normal and Fine"
            result_dic = {
                'image': path,
                'res': ans
            }
            return render_template('index.html', my_result=result_dic)
        else:
            res = "not an image file. Allowed extensions( .jpg, .jpeg, .png). Please submit again."
            return render_template('index.html', result=res)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
