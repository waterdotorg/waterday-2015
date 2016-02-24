from django.shortcuts import get_object_or_404, render, redirect

from custom.forms import ShareImageForm
from custom.models import ShareImage


def share_image(request):
    if request.method == 'POST':
        form = ShareImageForm(request.POST, request.FILES)
        if form.is_valid():
            share_image = ShareImage(
                image=form.cleaned_data.get('image')
            )
            share_image.save()
            # TODO pass in image to overlay
            share_image.image_overlay()
            return redirect('share_image_detail', pk=share_image.pk)
    else:
        form = ShareImageForm()

    dict_context = {'form': form}

    return render(request, 'custom/share-image.html', dict_context)


def share_image_detail(request, pk=None):
    share_image = get_object_or_404(ShareImage, pk=pk, published=True)

    dict_context = {
        'share_image': share_image,
    }

    return render(request, 'custom/share-image-detail.html', dict_context)
