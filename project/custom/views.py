import urllib

from django.shortcuts import get_object_or_404, render, redirect

from custom.forms import ShareImageForm
from custom.models import ShareImage


def homepage(request):
    form = ShareImageForm()
    dict_context = {'form': form}

    return render(request, 'homepage.html', dict_context)


def share_image(request):
    if request.method == 'POST':
        form = ShareImageForm(request.POST, request.FILES)
        if form.is_valid():
            share_image = ShareImage(
                image=form.cleaned_data.get('image'),
                remote_addr=request.META.get('REMOTE_ADDR', None),
            )
            share_image.save()
            share_image.image_overlay(form.cleaned_data.get('word'))
            return redirect('share_image_detail', pk=share_image.pk)
    else:
        form = ShareImageForm()

    dict_context = {'form': form}

    return render(request, 'custom/share-image.html', dict_context)


def share_image_detail(request, pk=None):
    share_image = get_object_or_404(ShareImage, pk=pk, published=True)
    share_image_url = "http://www.waterday.org%s" % share_image.get_absolute_url()
    share_image_url_encode = urllib.quote_plus(share_image_url)

    twitter_share_text = "Water gives hope, health, and opportunity. Celebrate @water every day at Water.org. #watergives"
    twitter_share_text_encode = urllib.quote_plus(twitter_share_text)

    dict_context = {
        'share_image': share_image,
        'share_image_url_encode': share_image_url_encode,
        'twitter_share_text_encode': twitter_share_text_encode,
    }

    return render(request, 'custom/share-image-detail.html', dict_context)
