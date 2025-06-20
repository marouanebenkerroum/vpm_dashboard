from django.shortcuts import render
import requests
from .models import PredictionLog

MODEL_API_URL = "http://localhost:8001/predict/"

def home(request):
    if request.method == "POST":
        input_data = request.POST.get("features")
        features = list(map(float, input_data.split(",")))

        response = requests.post(MODEL_API_URL, json={"features": features})
        print("Status code:", response.status_code)
        print("Response text:", response.text)

        prediction = None
        try:
            prediction = response.json().get("prediction")
        except ValueError:
            print("Response is not valid JSON")

        if prediction is not None:
            PredictionLog.objects.create(input_data=input_data, prediction=prediction)
            return render(request, "predictor/result.html", {"prediction": prediction})
        else:
            return render(request, "predictor/home.html", {"error": "Failed to get prediction from model API."})

    return render(request, "predictor/home.html")


def logs(request):
    logs = PredictionLog.objects.all().order_by("-timestamp")
    return render(request, "predictor/logs.html", {"logs": logs})