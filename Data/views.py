from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from .models import FileUpload
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from django.shortcuts import render, get_object_or_404



def First(request):
     return render(request,'First.html')

def index(request):
     return render(request,'index.html')


def second(request):
     return render(request,'Second.html')


def three(request):
     return render(request,'third.html')


def upload(request):
     if request.method == 'POST':
          file2 = request.FILES.get('fileInput')
          document = FileUpload.objects.create(file = file2)
          document.save()
          return render(request,'index.html')

     else:
          return render(request,'First.html')   
     

import pandas as pd
from django.shortcuts import render
from .models import FileUpload

def analysis(request):
    latest_file = FileUpload.objects.latest('uploaded_at')
    file_path = latest_file.file.path
    
    
    df = pd.read_csv(file_path)
    
    
    summary_statistics = df.describe().to_dict()
    
    
    null_values = df.isnull().sum().to_dict()
    
    
    first_three_rows = df.head(3).to_html(classes='table table-bordered', index=False)
    
    context = {
        'summary_statistics': summary_statistics,
        'null_values': null_values,
        'first_three_rows': first_three_rows,
    }
    
    return render(request, 'second.html', context)


     

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import FileUpload


import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import FileUpload

def display(request):
    try:
        latest_file = FileUpload.objects.latest('uploaded_at')
        file_path = latest_file.file.path
        
      
        df = pd.read_csv(file_path)
        
        
        columns = df.columns.tolist()
        
        
        first_three_rows = df.head(3).to_html(classes='table table-bordered', index=False)
        
        
       
        context = {
            'columns': columns,
            'first_three_rows': first_three_rows,
            
        }

        return render(request, 'Three.html', context)
    
    except FileUpload.DoesNotExist:
        return render(request, 'Three.html', {'error_message': 'No files uploaded yet.'})
    except Exception as e:
        return render(request, 'Three.html', {'error_message': f'Error: {e}'})



import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO
from django.shortcuts import render
from .models import FileUpload

def visualizations(request):
    try:
        # Fetching the latest uploaded file based on timestamp, assuming there is at least one file
        latest_file = FileUpload.objects.latest('uploaded_at')
        file_path = latest_file.file.path

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Initialize plots list to store base64 images
        plots = []

        # Histogram
        plt.figure()
        df.hist(figsize=(10, 8), color='skyblue', edgecolor='black')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        plots.append(image_base64)

        # Line Plot
        plt.figure()
        df.plot(figsize=(10, 8))
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        plots.append(image_base64)

        # Pie Chart (using the first categorical column)
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns
        if not categorical_columns.empty:
            plt.figure()
            df[categorical_columns[0]].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, figsize=(8, 8))
            buf = BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            plots.append(image_base64)

        context = {
            'plots': plots,
        }

        return render(request, 'Four.html', context)

    except FileUpload.DoesNotExist:
        return render(request, 'Four.html', {'error_message': 'No files uploaded yet.'})
    except Exception as e:
        return render(request, 'Four.html', {'error_message': f'Error: {e}'})








