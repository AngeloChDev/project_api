from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .defaultauto import defaultload, Autos
from django.http import HttpResponseRedirect
#from .models import Autos
# Create your views here.

class AutoShop(TemplateView):
      template_name = "auto_shop.html"
      def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            autos=Autos.objects.all()
            context= {'list_autos':autos}
            return context
      

class Login(TemplateView):
      template_name = "login_page.html"
      


def loadauto(request, *arg, **kwargs):
      #defaultload()

      return HttpResponseRedirect('shop_page')
