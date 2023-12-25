from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import get_template

from .models import Participant
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



# function to send event notifications to selected participants
def send_notification(modeladmin, request, queryset, scenario):
    subject = f'Dash Event ({scenario.capitalize()})'
    from_email = 'gip.dash.event@gmail.com'  

    # loop through selected participants and send notifications
    for participant in queryset:
        template_name = f'emails/{scenario}_email.html'
        template = get_template(template_name)
        # message = template.render()
        recipient =participant.email
        welcome_message = "Welcome "+ participant.name+ " " +"!"
        link_app = "http://localhost:8000"
        context = {
            "welcome_message": welcome_message, 
            "link_app": link_app
        }
        print(recipient)
        html_message = render_to_string( template_name , context=context)
        plain_message = strip_tags(html_message)
        message = EmailMultiAlternatives(
            subject =subject, 
            body = plain_message,
            from_email = from_email,
            to= [recipient]
        )

        message.attach_alternative(html_message, "text/html")
        message.send()

        # send_mail(subject, message, from_email, [participant.email])


    modeladmin.message_user(request, f'Notifications sent for {len(queryset)} participants ({scenario}).')

send_notification.short_description = 'Send event notification to selected participants'

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','discord_id','organization')

    def acceptance_notification(self, request, queryset):
        send_notification(self, request, queryset, 'acceptance')

    def reminder_notification(self, request, queryset):
        send_notification(self, request, queryset, 'reminder')

    def update_notification(self, request, queryset):
        send_notification(self, request, queryset, 'update')

    actions = [acceptance_notification, reminder_notification, update_notification]

admin.site.register(Participant, ParticipantAdmin)