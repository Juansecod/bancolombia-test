from django.shortcuts import render
import pandas as pd
from .utils import generate_plots, train_model

def home(request):
    """
    The `home` function in Python processes a POST request to read a CSV or Excel file, train a model,
    generate forecasts, and display the results on a webpage.
    
    :param request: The `request` parameter in the `home` function is typically an object that contains
    information about the current HTTP request. It includes details such as the request method (GET,
    POST, etc.), any data sent in the request (such as form data or files), and other metadata related
    to the request
    :return: The `home` function is returning a rendered HTML template named "index.html" with the
    context data that includes the title, predicts, plots, and error messages based on the logic and
    exceptions handled within the function.
    """
    context = {
        "title":"Prediccion TMR", 
    }
    try:
        if request.method == "POST":
            freq = int(request.POST["freq"])
            file = request.FILES.get('file')
            if file.content_type == "text/csv":
                df = pd.read_csv(file)
            elif file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(file)

            forecast = train_model(df, freq)
            forecast["yhat"] = round(forecast["yhat"], 2)
            context["predicts"] = forecast.tail(freq).to_dict('records')
            context["plots"] = generate_plots(forecast)
    except KeyError:
        context['error'] = "Ups, algo no ha funcionado bien. Intenta verificar si el dataset usado tiene los campos necesarios."
    except AttributeError:
        context['error'] = "Ups, parece que se te ha olvidado algo. Recuerda subir el dataset"
    except Exception:
        context['error'] = "Ups, parece algo salio mal"
    
    return render(request,"index.html",context)
