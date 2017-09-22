from django.shortcuts import render, redirect

from .models import Test

'''
context = {
	'name': 'michael',
	'age': 62
}
'''

# Create your views here.
def index(request):

	all_test_data = Test.objects.all()[:10]

	context = {
		'test_data': all_test_data
	}
	
	return render(request, 'index.html', context)
	
	
	
def details(request, id):
	test = Test.objects.get(id=id)
	
	test_data = test

	context = {
		'test_data': test_data
	}
	
	return render(request, 'details.html', context)
	
	
def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']
		
		test = Test(title=title, text=text)
		test.save()
		
		return redirect('/home')
	else:
		return render(request, 'add.html')
