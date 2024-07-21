from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


CROP_CHOICES = [
    ("tea", "Tea"),
    ("coffee", "Coffee"),
    ("maize", "Maize"),
    ("wheat", "Wheat"),
    ("beans", "Beans"),
]


class DiseasePredictionForm(forms.Form):
    image = forms.ImageField(label="Upload an image of the plant")
    crop = forms.ChoiceField(label="Crop Name", choices=CROP_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("crop", css_class="mb-4"),
            Field("image", css_class="mb-4"),
            Submit(
                "submit",
                "Classify",
                css_class="""
                    bg-teal-500 hover:bg-teal-700 text-white
                    font-bold py-2 px-4 rounded focus:outline-none
                    focus:shadow-outline
                """,
            ),
        )


class PestIdentificationForm(forms.Form):
    image = forms.ImageField(label="Upload an image of the plant")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("image", css_class="mb-4"),
            Submit(
                "submit",
                "Classify",
                css_class="""
                    bg-teal-500 hover:bg-teal-700 text-white
                    font-bold py-2 px-4 rounded focus:outline-none
                    focus:shadow-outline
                """,
            ),
        )


class CropRecommendationForm(forms.Form):
    nitrogen = forms.FloatField(label="Nitrogen content in soil")
    phosphorus = forms.FloatField(label="Phosphorus content in soil")
    potassium = forms.FloatField(label="Potassium content in soil")
    temperature = forms.FloatField(label="Temperature (°C)")
    humidity = forms.FloatField(label="Humidity (%)", max_value=100, min_value=0)
    ph = forms.FloatField(label="pH of soil", max_value=14, min_value=0)
    soil_moisture = forms.FloatField(label="Soil Moisture ")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("nitrogen", css_class="mb-4"),
            Field("phosphorus", css_class="mb-4"),
            Field("potassium", css_class="mb-4"),
            Field("temperature", css_class="mb-4"),
            Field("humidity", css_class="mb-4"),
            Field("ph", css_class="mb-4"),
            Field("soil_moisture", css_class="mb-4"),
            Submit(
                "submit",
                "Get Recommendation",
                css_class="""
                    bg-teal-500 hover:bg-teal-700 text-white
                    font-bold py-2 px-4 rounded focus:outline-none
                    focus:shadow-outline
                """,
            ),
        )
