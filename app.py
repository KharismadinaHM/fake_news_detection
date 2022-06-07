from flask  import Flask , render_template , request
import pickle
import warnings
warnings.filterwarnings('ignore')

tfidf = pickle.load(open('tfidf.pkl', 'rb'))
model = pickle.load(open("final_model_rfc.pkl", 'rb'))

app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def pred():
    # HTML -> .py
    if request.method == "POST":
        news = request.form["news"]
        
    #.p -> HTML
        predict = model.predict(tfidf.transform([news]))
        
        if predict == 0:
            return render_template("index.html", prediction = 'Narasi tersebut Hoax , Mohon untuk tidak membagikan lagi ke Internet.')
        elif predict == 1:
            return render_template("index.html", prediction = 'Narasi tersebut Real')
        #return render_template("index.html", prediction_text = 
        #"Jawabannya {}".format(predict))

    else:
        return render_template("index.html")

if __name__ == "__main__" :
    app.run(debug=True)
