import flask
import glob
import os
import subprocess
from flask import request
from flask import send_file
from datetime import datetime
import time

permitted_models = {'herolte', 'beyond0lte'}

LOG_PATH = "/root/logs" # "/home/adhoms/lineageos/volumes/logs"
ZIP_PATH = "/root/zips" # "/home/adhoms/lineageos/volumes/zips"

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def get_logfile_path(model):
    list_of_files = glob.glob(f'{LOG_PATH}/herolte/lineage-19.1-*-UNOFFICIAL-{model}.log')
    latest_file = max(list_of_files, key=os.path.getctime)
    return str(latest_file), os.path.getctime(latest_file)

def get_zip_path(model):
    list_of_files = glob.glob(f'{ZIP_PATH}/herolte/lineage-19.1-*{model}*zip')
    latest_file = max(list_of_files, key=os.path.getctime)
    return str(latest_file)

def get_logfile_tail(n=10, model='herolte'):
    logfile_path, filetime = get_logfile_path(model)
    result = subprocess.run(['tail', f'-n{n}', logfile_path], stdout=subprocess.PIPE)
    s = result.stdout.decode('utf-8')
    return s, filetime

@app.route('/download', methods=['GET'])
def download():
    args = request.args.to_dict() if request.args else dict()
    model = args.get('model', 'herolte')
    if model not in permitted_models: return 'bye'
    filepath = get_zip_path(model)
    return send_file(filepath, as_attachment=True)

@app.route('/', methods=['GET'])
def home():
    try:
        args = request.args.to_dict() if request.args else dict()
        print(args)
        n = int(args.get('n',10))
        model = args.get('model', 'herolte')
        if model not in permitted_models: raise Exception()
        print(n)
    except:
        return 'bye'
    newl = "<br>"
    tail, filetime = get_logfile_tail(n=n, model=model)
    tail = tail.split("\n")
    #tail = tail[::-1]
    tail = newl.join(tail)
    #tail = tail.replace("\n",newl)
    tail = f"Tail:{newl}{tail}{newl}"
    diff = int(time.time() - filetime)
    filetime = datetime.utcfromtimestamp(filetime).strftime('%Y-%m-%d %H:%M:%S')
    last_updated = f"Last updated {diff} seconds ago, @ {filetime}{newl}"
    download_href = f"<a href='/download?model={model}'>Download for '{model}'</a>" + newl
    index_href = "View logs for: " + (" | ".join([f"<a href='/?model={model_}'>{model_}</a>" for model_ in permitted_models])) + newl
    return last_updated \
            + newl \
            + download_href \
            + index_href \
            + newl \
            + tail

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
