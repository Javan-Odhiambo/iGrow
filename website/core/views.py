from django.shortcuts import render
from .forms import CropRecommendationForm, DiseasePredictionForm, PestIdentificationForm


# Create your views here.
def home(request):
    user = request.user
    context = {
        "title": "Home",
        "content": "Welcome to the home page!",
        "user": user,
    }

    return render(request, "core/index.html", context=context)


def disease(request):

    context = {
        "current_page": "disease",
    }
    if request.method == "POST":
        form = DiseasePredictionForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            image = form.cleaned_data["image"]

            # Make a prediction
            prediction_result = "apple scab"
            confidence = 80

            # Save the result (optional)
            # PredictionResult.objects.create(
            #     result_type='disease',
            #     result=prediction_result,
            #     confidence=confidence
            # )

            context.update(
                {
                    "predicted_result": {
                        "result": prediction_result,
                        "confidence": confidence,
                    },
                }
            )

    else:
        form = DiseasePredictionForm()

    context.update({"form": form})

    return render(request, "core/disease.html", context=context)


def crop_recommendation(request):

    context = {
        "current_page": "crop_recommendation",
    }
    if request.method == "POST":
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            # Process the form data
            nitrogen = form.cleaned_data["nitrogen"]
            phosphorus = form.cleaned_data["phosphorus"]
            potassium = form.cleaned_data["potassium"]
            temperature = form.cleaned_data["temperature"]
            humidity = form.cleaned_data["humidity"]
            ph = form.cleaned_data["ph"]
            soil_moisture = form.cleaned_data["soil_moisture"]

            if nitrogen > 100:
                prediction_result = "maize"
                confidence = 80

            else:
                prediction_result = "wheat"
                confidence = 90

            # Save the result (optional)
            # PredictionResult.objects.create(
            #     result_type='disease',
            #     result=prediction_result,
            #     confidence=confidence
            # )

            context.update(
                {
                    "form": form,
                    "predicted_result": {
                        "result": prediction_result,
                        "confidence": confidence,
                    },
                }
            )
    else:
        form = CropRecommendationForm()
        context.update({"form": form})

    return render(request, "core/crop-recommendation.html", context=context)


def pest(request):

    context = {
        "current_page": "pest_identification",
    }
    if request.method == "POST":
        form = PestIdentificationForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            image = form.cleaned_data["image"]

            # Make a prediction
            prediction_result = "apple scab"
            confidence = 80

            # Save the result (optional)
            # PredictionResult.objects.create(
            #     result_type='disease',
            #     result=prediction_result,
            #     confidence=confidence
            # )

            context.update(
                {
                    "form": form,
                    "predicted_result": {
                        "result": prediction_result,
                        "confidence": confidence,
                    },
                }
            )

    else:
        form = PestIdentificationForm()
        context.update({"form": form})

    return render(request, "core/pest.html", context=context)


def weather_forecast(request):

    user = request.user
    context = {
        "title": "Home",
        "content": "Welcome to the home page!",
        "user": user,
        "current_page": "weather_forecast",
    }

    return render(request, "core/weather-forcast.html", context=context)
