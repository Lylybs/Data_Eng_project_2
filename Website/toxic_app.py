from flask import Flask, request, render_template


import detoxify
from detoxify import Detoxify
from collections import defaultdict
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from prometheus_flask_exporter import PrometheusMetrics

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Here we collect the sentence entered by the user on the web interface
def input_sent():
        input = request.form['sentence']
        return input

    #tokenize sentences : split input sentence into words
def sent_tokenized(input):
        data_clean_sent_tokenized = sent_tokenize(input)
        data_clean_word_sent_tokenized = [word_tokenize(sentence) for sentence in data_clean_sent_tokenized]
        return data_clean_word_sent_tokenized

    #lower text
def lower_sent(token):
        stc_token_lower=[]
        for i in range(len(token)):
            stc_token_lower.append([word.lower() for word in token[i]])
        return stc_token_lower

    #Lemmatize : etablish relationships between words and remove stopwords
def lemmatize(lower_sent):
        stopWords = stopwords.words('english')
        word_lemmatizer = WordNetLemmatizer()
        final_sent = []
        for sent in lower_sent:
            for word in sent:
                if word not in stopWords:
                    final_sent.append(word_lemmatizer.lemmatize(word))
        final_input = ' '.join(final_sent)
        return final_input

#methods which return the result and stats
def analysis(lemmatize_token):
        analyser = detoxify.Detoxify('original')
        stat= analyser.predict(lemmatize_token)
        maxToxic = max(stat['toxicity'], stat['severe_toxicity'], stat['obscene'], stat['threat'],stat['insult'], stat['identity_attack'])
        res= ""
        if maxToxic >= 0.50 :
            res="toxic"
        elif maxToxic < 0.40 :
            res="not toxic"
        else:
            res="error"
        return res, stat

#flask app definition
def createapp():
        app = Flask(__name__)

        metrics = PrometheusMetrics(app, group_by='endpoint')
        metrics.info('app_info', 'Application info', version='1.0.3')

        metrics.start_http_server(5099)
        
        @app.route('/')
        def my_form():
            return render_template('website.html')


        @app.route('/', methods=['POST'])

        def final_function():
            input = input_sent()
            data_clean_word_sent_tokenized = sent_tokenized(input)
            stc_token_lower= lower_sent(data_clean_word_sent_tokenized)
            final_input = lemmatize(stc_token_lower)
            res, stat = analysis(final_input)
            print(stat),
            res_final= res+ "\n\n" +str(stat)
            #res=result(score)
            return render_template('website.html', final = res, final2 = stat)


        if __name__ == "__main__":
            app.run(debug=True, host="0.0.0.0", port=5000)

        return app

#run app
createapp()

