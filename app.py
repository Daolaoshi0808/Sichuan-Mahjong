from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from mahjong_utils import recognize_tiles
from mahjong_predict import consolidate_mahjong_code
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'mahjong'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['ALLOWED_EXTENSIONS'] = {'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        is_menqing = 'is_menqing' in request.form
        if is_menqing:
            return handle_menqing(request)
        else:
            return handle_not_menqing(request)

    return render_template('index.html')

def handle_menqing(request):
    file = request.files['file']
    converted_list = recognize_tiles(file)
    best_move = consolidate_mahjong_code(converted_list)
    return f"File uploaded successfully! Recommended Next Move: {best_move}"

def handle_not_menqing(request):
    if 'file_id' in session:
        return render_template('not_menqing.html')

    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['file_id'] = filename
            return render_template('not_menqing.html')
    
    return "Error: File not found or invalid file type."

@app.route('/select_tiles', methods=['POST'])
def select_tiles():
    if request.method == 'POST':
        peng = int(request.form.get('peng', 0))
        gang = int(request.form.get('gang', 0))
        peng_selections = []
        gang_selections = []
        for i in range(peng):
            print(logging.debug("debug"))
            peng_tile = request.form.get(f'peng_{i+1}')
            peng_selections.append(peng_tile)
        for i in range(gang):
            gang_tile = request.form.get(f'gang_{i+1}')
            gang_selections.append(gang_tile)

        # Store the values in the session
        session['peng'] = peng
        session['gang'] = gang
        session['peng_selections'] = peng_selections
        session['gang_selections'] = gang_selections

        return render_template('select_tiles.html',
                               peng=peng,
                               gang=gang,
                               peng_selections=peng_selections, 
                               gang_selections=gang_selections)

@app.route('/display_result', methods=['GET', 'POST'])
def display_result():
    peng = session.get('peng', 0)
    gang = session.get('gang', 0)
    peng_selections = session.get('peng_selections', [])
    gang_selections = session.get('gang_selections', [])

    converted_list = process_not_menqing_form(peng, gang, peng_selections, gang_selections)

    # Use consolidate_mahjong_code to process the converted_list
    #best_move = consolidate_mahjong_code(converted_list)

    return render_template('display_result.html', converted_list=converted_list)

def process_not_menqing_form(peng, gang, peng_selections, gang_selections):
    # 识别剩余手牌
    file_id = session.get('file_id')
    if file_id:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id)
        file = open(file_path, 'rb')
        num = peng + gang
        converted_list = recognize_tiles(file, peng=num)
        converted_list.extend(peng_selections)
        converted_list.extend(gang_selections)
    else:
        return "Error: File not found."

    return converted_list

if __name__ == '__main__':
    app.run(debug=True)
