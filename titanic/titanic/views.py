from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request,"index.html")

def result(request):
    age = int(request.GET["age"])
    pclass = int(request.GET["pclass"])
    embarked = int(request.GET["embarked"])
    sex = int(request.GET["sex"])
    fare = int(request.GET["fare"])
    parch = int(request.GET["parch"])
    title = int(request.GET["title"])
    sibsp = int(request.GET["sibsp"])
    prediction = ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request,"result.html",{"prediction" : prediction})
