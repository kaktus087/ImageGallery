from django.shortcuts import render, redirect,get_object_or_404
from .models import ImageModel
from .forms import ImageForm

from django.http import HttpResponse

def view_image_by_filename(request, image_filename):
    image = get_object_or_404(ImageModel, image__icontains=image_filename)
    
    response = HttpResponse(image.image, content_type='image/png')  # Измените тип контента, если это не PNG
    return response

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():

            #image_instance = form.save()
            #image_id = image_instance.id
            image_instance = form.save(commit=False)
            image_instance.title = "123"
            image_instance.image.name = image_instance.name + image_instance.image.name[-4:]  # Здесь устанавливаем желаемое имя файла
            image_instance.save()
            
            return redirect('image_list')
            
    else:
        form = ImageForm()
    #return render(request, 'upload_image.html', {'form': form})
    return render(request, 'images/upload_image.html', {'form': form})

def image_list(request):
    images = ImageModel.objects.all()
    return render(request, 'images/image_list.html', {'images': images})

def view_image(request, image_id):
    image = get_object_or_404(ImageModel, id=image_id)
    
    # Отправляем изображение как HTTP-ответ с нужными заголовками
    response = HttpResponse(image.image, content_type='image/png')  # Измените тип контента, если это не PNG
    return response