from flask import Flask, render_template
from flask_cors import CORS
from forms import JobDescriptionAndResumeForm
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
model.max_seq_length = 512


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'e6502c8f42a79f8f58848be53054b174'


def analyze(model, form_data):
    embeddings = model.encode([form_data['responsibilities'], form_data['requirements'],
                               form_data['experience'], form_data['education'],
                               form_data['skills']])
    scores1, scores2 = [], []
    for i in range(2, 5):
        scores1.append(round(cosine_similarity(embeddings[0].reshape(1, -1), embeddings[i].reshape(1, -1))[0][0]*100, 2))
        scores2.append(round(cosine_similarity(embeddings[1].reshape(1, -1), embeddings[i].reshape(1, -1))[0][0]*100, 2))
    
    avg_score = round(np.mean(scores1, scores2), 2)
    
    return avg_score


@app.route('/', methods=['GET', 'POST'])
def home():
    form = JobDescriptionAndResumeForm()
    
    if form.is_submitted():
        #print('submitted...')
        #print(form.data)
        score = analyze(model, form.data)
        #score = 90.87
        #print(score)
        return render_template('home.html', form=form, score=f'Score: {score}%')
    
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run()