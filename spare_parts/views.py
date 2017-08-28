from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

def test_home(request):

	html_ = """

<html lang="en-US">
<head>   
<title>Bhutan Power Corporation Limited</title>
</head>

<body class="home page-template page-template-page-home page-template-page-home-php page page-id-6 group-blog">

    
        
</body>
</html>

"""
	return HttpResponse(html_)

def home(request):

	return render(request, "base.html", {"value", True})

class ContactView(View):
	def get(self, request, *args, **kwargs):
		
		context = []
		return render(request, "contact.html", context)
