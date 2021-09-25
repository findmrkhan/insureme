from django.db import transaction
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer
from .models import (Quote, Policy, PolicyHistory, PolicyMaster, QuoteStatusMaster, PolicyStatusMaster
                    ,CurrencyMaster)
from .serializers import (QuoteSerializer, PolicySerializer, PolicyHistorySerializer)
from .serializers import CustomerSerializer

import datetime


class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PolicyListView(ListAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class PolicyDetailView(RetrieveAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class PolicyHistoryView(ListCreateAPIView):
    queryset = PolicyHistory.objects.all()
    serializer_class = PolicyHistorySerializer

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return PolicyHistory.objects.filter(policyid=pk)
    #     # return PolicyHistory.objects.all()

# class QuoteUpdateView(UpdateAPIView):
#     queryset = Quote.objects.all()
#     serializer_class = QuoteSerializer


class QuoteUpdateView(APIView):

    def put(self, request, *args, **kwargs):
        quote_serializer = QuoteSerializer(data=request.data)
        policy = Policy.objects.filter(id=request.data.get('id')).first()
        change_status = ''
        if request.data.get('quote_status') == '2':
            change_status = 'BOUNDED'
        elif request.data.get('quote_status') == '3':
            change_status = 'EXPIRED'
        else:
            change_status = 'QUOTED'

        policy.policy_status = PolicyStatusMaster.objects.filter(policy_status=change_status).first()

        if quote_serializer.is_valid():
            with transaction.atomic():
                policy.save()
                # quote_serializer.pk = thePolicy.pk
                quote_serializer.save()
                return Response(quote_serializer.data)

        return Response(quote_serializer.errors)


class QuoteCreateView(APIView):

    def logic_for_premium(self, p):
        return 12345

    def logic_for_max_insured_amount(self, p):
        return 55555

    def post(self, request, *args, **kwargs):

        quote_serializer = QuoteSerializer(data=request.data)
        quote_status = QuoteStatusMaster.objects.filter(quote_status="QUOTED").first()
        customer = Customer.objects.filter(pk=request.data.get('customer')).first()
        policy_master = PolicyMaster.objects.filter(policytype=request.data.get('policytype')).first()
        psm = PolicyStatusMaster.objects.filter(policy_status="QUOTED").first()
        # currency = CurrencyMaster.objects.filter(currency="AED").first()

        quote_serializer.quote_status   = quote_status
        quote_serializer.customer       = customer


        thePolicy = Policy(
                        policy_status=psm,
                        customer=customer,
                        policy_master=policy_master,
                        effective_date=datetime.datetime.now(),
                        expiry_date=datetime.datetime.now(),
                    )

        if quote_serializer.is_valid():
            with transaction.atomic():
                thePolicy.save()

            quote_serializer.policy = thePolicy
            policy_hist = PolicyHistory(
                policy_status="QUOTED",
                policyid=thePolicy.id,
                timestamp=datetime.datetime.now()
            )
            with transaction.atomic():
                quote_serializer.save()
                policy_hist.save()
            return Response(quote_serializer.data)

        return Response(quote_serializer.errors)


# class QuoteListView(ListAPIView):
#     queryset = Quote.objects.all()
#     serializer_class = QuoteSerializer
#
#
# class PolicyCreateView(CreateAPIView):
#     queryset = Policy.objects.all()
#     serializer_class = PolicySerializer
#
#
# class PolicyListView(ListAPIView):
#     queryset = Policy.objects.all()
#     serializer_class = PolicySerializer

