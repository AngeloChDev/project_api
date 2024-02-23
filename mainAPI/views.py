from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .defaultauto import defaultload, Autos
from django.http import HttpResponseRedirect

# Create your views here.

class AutoShop(TemplateView):
      template_name = "auto_shop.html"
      def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            autos=Autos.objects.all()
            context= {'list_autos':autos}
            return context
      

class Login(TemplateView):
      template_name = "login_page.html"
      

class AutoData(TemplateView):
      template_name = "auto_data.html"

      def get_context_data(self, auto_id, **kwargs: Any) -> dict[str, Any]:
            auto = Autos.objects.get(id=auto_id)
            context = {"auto":auto}
            return context
      
      def get(self, request, auto_id, *arg, **kwargs):
            context = self.get_context_data(auto_id)
            return render(request, self.template_name, context)

      

def loadauto(request, *arg, **kwargs):
      #defaultload()

      return HttpResponseRedirect('shop_page')
