from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.template import Context
import os
from io import BytesIO
from xhtml2pdf import pisa
from invitations.utils import render_to_pdf
from .models import Attendee
def home(request):
    return render(request, 'website/index.html')


def save_pdf(file, filename):
    with open(settings.MEDIA_ROOT + '/' + filename, 'wb+') as destination:
        destination.write(file)

def register(request):
    context = {'spinner': 'true'}
    if request.method == 'POST':
        email = request.POST.get('e')
        name = request.POST.get('name')
        rollNo = request.POST.get('rollNo')
        phone = request.POST.get('phone')
        coming = request.POST.get('coming')

        Attendee.objects.create(
            name=name,
            email=email,
            rollNo=rollNo,
            phone=phone,
            coming=coming
        )

        htmly = get_template('website/mailtemplate.html')
        d = { 'name': name }

        # pdf = render_to_pdf('website/pdftemplate.html', { 'name': name })
        # pdf_bytes = pdf.content
        # save_pdf(pdf_bytes, f'{name}{rollNo}.pdf')

        subject, from_email, to = 'Invitation Abhyuday\'s Coordie ATM 2021', 'abhyudayinvite@gmail.com', email
        text_content = 'You are invited'
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        # msg.attach_file(os.path.join(settings.MEDIA_ROOT, f'{name}{rollNo}.pdf'))
        msg.send()
        context = {'message': "check your mail for invitation card!!", 'spinner': 'false'}


    return render(request, 'website/register.html', context=context)