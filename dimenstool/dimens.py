from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from dimenstool.dimen import Transfer


@csrf_exempt
def converter(request):
    density = request.POST.get("density", None)
    scale_density = request.POST.get("scale_density", None)
    xdpi = request.POST.get("xdpi", None)
    dimens_content = request.POST.get("dimens_content", None)
    transfer = Transfer.Transfer(density, scale_density, xdpi, dimens_content)
    dimens_new_content = transfer.generator()
    return render_to_response("dimens.html", {"data": dimens_new_content}, RequestContext(request), )
