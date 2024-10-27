from django.shortcuts import render
import os
import joblib
from django.shortcuts import render
from django.conf import settings


MODEL_PATH = os.path.join(settings.BASE_DIR,'spam_app', 'static', 'Nave_Bayes.pkl')
VECTORIZER_PATH = os.path.join(settings.BASE_DIR,'spam_app', 'static', 'Vec_log_regr.pkl')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_email(request):
    prediction = None
    if request.method == 'POST':
        email_content = request.POST.get('email_content')
        if email_content:
            email_vector = vectorizer.transform([email_content])
            is_spam = model.predict(email_vector)[0]
            prediction = "Spam" if is_spam else "Not Spam"
    
    return render(request, 'predict.html', {'prediction': prediction})