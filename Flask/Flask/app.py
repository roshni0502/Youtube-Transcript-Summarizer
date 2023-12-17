from flask import Flask,render_template,request,send_from_directory,send_file
from YouTubeTranscript import getSummary,hinditranslate,englishtranslate,mrathitranslate
import os
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')
@app.route("/", methods=['POSt',"GET"])

def index():    
    if request.method == 'POST':
        
        if request.form.get('action1') == 'VALUE1':
            output=request.form.to_dict()
            link=output['link']
            t1=getSummary(link)
            
            return render_template("index.html",t1=t1)
        elif request.form.get('hindi') == 'hindi':
            
            t1=hinditranslate()
            return render_template("index.html",t1=t1)
        elif request.form.get('english') == 'english':
            
            t2=englishtranslate()
            return render_template("index.html",t1=t2)
        elif request.form.get('marathi') == 'marathi':
            
            t3=mrathitranslate()
            return render_template("index.html",t1=t3)
        elif request.form.get('download') == 'download':
            
            return send_file(
        'summary.txt',
        mimetype='text/csv',
        download_name='summa.txt',
        as_attachment=True
    )
    return render_template("index.html",t1='ss')
    

if __name__=='__main__':
    app.run(debug=True,port=5001)