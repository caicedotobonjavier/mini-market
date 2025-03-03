from io import BytesIO
#
from django.template.loader import get_template
#
from django.http import HttpResponse
#
from xhtml2pdf import pisa
#


#generador del pdf
def factura_pdf(template_src, context={}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    
    return None