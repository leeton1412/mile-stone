from django.http import HttpResponse


class StripeWH_Handler:
    """ This Handles Stripe Webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook Recieved {event[type]}',
            status=200)

    def handle_payment_event_succeeded(self, event):
        return HttpResponse(
            content=f'Webhook Recieved {event[type]}',
            status=200)

    def handle_payment_event_failed(self, event):
        return HttpResponse(
            content=f'Webhook Recieved {event[type]}',
            status=200)