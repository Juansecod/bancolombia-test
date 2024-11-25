from django.shortcuts import render
import pandas as pd
from .utils import generate_plots, train_model

def home(request):
    """
    The `home` function processes a file uploaded through a web request, reads the data from the file
    either as a CSV or Excel file, trains a model on the data, generates forecasts, and returns the
    predictions and plots to be displayed on a webpage.
    
    :param request: The `request` parameter in the `home` function is typically an object that contains
    information about the current HTTP request. It includes details such as the request method (GET,
    POST, etc.), any data sent with the request (such as form data or files), and other metadata related
    to the request
    :return: The `home` function returns a rendered HTML template named "index.html" with the context
    data that includes the title "Prediccion TMR", predictions data, and plots data. The function first
    checks if the request method is POST, reads the uploaded file (either CSV or Excel), trains a model
    using the data, generates predictions, and plots based on the forecast data. The predictions are
    then
    """
    context = {
        "title":"Prediccion TMR", 
    }
    
    if request.method == "POST":
        file = request.FILES.get('file')
        if file.content_type == "text/csv":
            df = pd.read_csv(file)
        elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(file)

        forecast = train_model(df)
        forecast["yhat"] = round(forecast["yhat"], 2)
        context["predicts"] = forecast.tail(30).to_dict('records')
        context["plots"] = generate_plots(forecast)
    
    return render(request,"index.html",context)
