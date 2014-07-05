
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import etag
from django.shortcuts import render
from django import forms
from PIL import Image, ImageDraw


class CadiForm(forms.Form):
    """ validator """

    height = forms.IntegerField(required=True, min_value=1, max_value=1500)
    width = forms.IntegerField(required=True, min_value=1, max_value=1500)


def generate_etag(request, width, height):
    return 'cadi: {0}x{1}'.format(width, height)


@etag(generate_etag)
def cadi(request, width, height):
    form = CadiForm({'height': height, 'width': width})
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        text = '{0} X {1}'.format(width, height)
        textwidth, textheight = draw.textsize(text)
        if textwidth < width and textheight < height:
            texttop = (height - textheight) // 2
            textleft = (width - textwidth) // 2
            draw.text((textleft, texttop), text, fill=(255, 255, 255))
        response = HttpResponse(content_type='image/png')
        image.save(response, 'PNG')
        return response
    else:
        return HttpResponseBadRequest('Invalid cadi request')
