from django.shortcuts import render, redirect
from .models import Contact
# from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['listing_id']
        user_id = request.POST['user_id']
        realtor_email = request.POST.get('realtor_email', False)

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an enquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # send email
        '''
        send_mail(
            'Property Listing Enquiry',
            'There has been an enquiry for ' + listing +
            '. Sign into the admin panel for more info.',
            'upworkabrar@gmail.com',
            [realtor_email, 'abrar.stonesour@gmail.com'],
            fail_silently=False
        )
        '''

        messages.success(
            request, 'Your message has been submitted successfully. A realtor will contact you soon!')
        return redirect('/listings/'+listing_id)
