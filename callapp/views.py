from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from .models import CallLog
from django.contrib import messages
import datetime


# Create your views here.

# this view rendering home page
def home_page(request):
    return render(request,"callapp/make_call.html")

# this view save call in database table, CallLog
def intiate_call(request):
    if request.method == 'POST':
        from_number = request.POST.get('from')
        to_number = request.POST.get('to')
        if from_number!=to_number:# both number are different
            submission_time=datetime.datetime.now()
            CallLog(from_number=from_number,to_number=to_number,calling_time=submission_time).save()
            messages.success(request, "Call successfulil made!." )
        else:                    # both number are same
            messages.error(request, "You can't make call to same numbers!" )
    return render(request, 'callapp/make_call.html')
    
# this view collect all call detail for particular number 
def call_report(request):
    number=request.GET['phone']    
    calls=CallLog.objects.all()
    lst=[]                         # empty list is created
    for call in calls:
        if call.from_number==number or call.to_number==number:
            lst.append(call)       # appending only those call , which contain this number

    paginator = Paginator(lst, 11) # paginator object created for 10 calls
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
                                
    return render(request,"callapp/call_detail.html",{"calls":page_obj,'number':number})
                                
# delete the particular call with id(primary key)       
def delete_call(request,id,number):
    obj_to_delete = CallLog.objects.get(id=id)
    obj_to_delete.delete()                        
    url = '/call-report/?phone={}'.format(number) # build the new URL with the variable as a parameter
    return redirect(url)     # redirect to the new URL


