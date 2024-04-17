from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import get_image_url, collect_categories


def main(request):
    categories_list = collect_categories('data.csv')
    context = {"categories": categories_list}

    return render(request, "main/index.html", context)


def test_api(request):

    categories_to_search = request.GET.getlist('category[]', [])
    image_url = get_image_url("data.csv", categories_to_search)
    print("image_url: ", image_url)



    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Изображение</title>
    </head>
    <body>
        <img src="{image_url}" alt="Изображение">
    </body>
    </html>
    """

    return HttpResponse(html_content)

