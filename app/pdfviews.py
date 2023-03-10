
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template

from xhtml2pdf import pisa
from datetime import datetime

from django.views.generic import View
from .models import Students


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hod_template/pdf.html')
        students = Students.objects.all()
        myDate = datetime.now()
        formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
        
        context={'students':students,'myDate':formatedDate}
       
        html = template.render(context)
        pdf = render_to_pdf('hod_template/pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341232")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        
        return HttpResponse("Not found")