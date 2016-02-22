from django.shortcuts import render, redirect

from custom.forms import ShareImageForm
from custom.models import ShareImage


def share_image_process(request):
    if request.method == 'POST':
        form = ShareImageForm(request.POST, request.FILES)
        if form.is_valid():
            # TODO image processing

            return redirect('share_image_detail', pk=share_image.pk)
    else:
        form = ShareImageForm()

    dict_context = {'form': form}

    return render(request, 'custom/share-image.html', dict_context)


def share_image_detail(request, pk=None):
    share_image = ShareImage.objects.get_object_or_404(pk=pk)

    dict_context = {
        'share_image': share_image,
    }

    return render(request, 'custom/share-image-detail.html', dict_context)
