from django.shortcuts import render

# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse
import smtplib

# Create your views here.
import datetime
import os

from customer.models import UserLogin,spare_part,supplier,customer, order, payment, shipping
from shop.settings import BASE_DIR


def index(request):
    return render(request, 'index.html')

def qrimg(request):
    return render(request, 'qrcode.html')


def logcheck(request):
    if request.method == "POST":
        username = request.POST.get('t1', '')
        password = request.POST.get('t2', '')
        request.session['username'] = username
        # if username=="admin" and password=="admin":
        checklogin = UserLogin.objects.filter(username=username).values()
        for a in checklogin:
            utype = a['utype']
            upass = a['password']
            if (upass == password):
                if (utype == "admin"):
                    return render(request, 'admin_home.html', context={'msg': 'welcome to owner'})
                if (utype == "customer"):
                    return render(request, 'customer_home.html', context={'msg': 'welcome to owner'})

            else:
                return render(request, 'login.html', context={'msg': 'fail'})

    return render(request, 'login.html')


def achangepassword(request):
    uname = request.session['username']
    if request.method == 'POST':
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = UserLogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    UserLogin.objects.filter(username=uname).update(password=newpass)
                    base_url = reverse('logcheck')
                    msg = 'password has been changed successfully'
                    return redirect(base_url, msg=msg)
                else:
                    return render(request, 'changepassword.html',
                                  {'msg': 'both the usename and password are incorrect'})
            else:
                return render(request, 'changepassword.html', {'msg': 'invalid username'})
    return render(request, 'changepassword.html')


def insertsparepartdetails(request):
    if request.method == "POST" and request.FILES['myfile']:

        s1 = request.POST.get('t1', '')
        s2 = request.POST.get('t2', '')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')
        s6 = request.POST.get('t6', '')
        s7 = request.POST.get('t7', '')
        s8 = request.POST.get('t8', '')
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        spare_part.objects.create(spare_part_id=s1, name=s2, number=s3, description=s4, quantity_available=s5, supplier_id=s6,
                          price=s7, company=s8, photo=myfile)
        return render(request, 'sparepart.html')
    return render(request, "sparepart.html")


def insertsupplier(request):
    if request.method == "POST":
        s1 = request.POST.get('t1', '')
        s2 = request.POST.get('t2', '')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')
        s6 = request.POST.get('t6', '')

        supplier.objects.create(id=s1, name=s2, contact=s3, address=s4, spare_part_name=s5, company=s6)
        return render(request, 'supplier.html')
    return render(request, "supplier.html")


def insertCustomer(request):
    if request.method == "POST":
        s1 = request.POST.get('t1', '')
        s2 = request.POST.get('t2', '')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')

        user = customer.objects.filter(email=s3).count()
        if user >= 1:
            return render(request, 'customer.html', {'msg': 'user is already exist'})
        else:

            customer.objects.create(cid=s1, name=s2, email=s3, password=s4, address=s5)
            UserLogin.objects.create(username=s3, password=s5, utype='customer')
            base_url = reverse('logcheck')
            return  redirect(base_url)
    return render(request, "customer.html")


def insertOrder(request):
    if request.method == "POST":
        s1 = request.POST.get('t1', '')
        s2 = request.POST.get('t2', '')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')
        s6 = request.POST.get('t6', '')

        order.objects.create(id=s1, date=s2, status=s3, address=s4, spare_part_id=s5, quantity=s6)
        return render(request, 'order.html')
    return render(request, "order.html")


def newinsertOrder(request):

    if request.method == "POST":
        s1 = request.POST.get('t1', '')
        s2 = request.POST.get('t2', '')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')
        s6 = request.POST.get('t6', '')

        order.objects.create(id=s1, date=s2, status=s3, address=s4, spare_part_id=s5, quantity=s6)
        base_url = reverse('insertpayment')
        return redirect(base_url)
    return render(request, 'insertordernew.html')


def insertpayment(request):
    if request.method == "POST":
        s1 = request.POST.get('t1', '')
        s2 = request.POST.get('t2', '')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')

        payment.objects.create(id=s1, ord_id=s2, date=s3, payment_method=s4, amount=s5)

        base_url = reverse('qrimg')
        return redirect(base_url)
    return render(request, "payment.html")


def insertShipping(request):
    if request.method == "POST":
        s1 = request.POST.get('t1', '')
        s2 = request.POST.get('t2', '')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')

        shipping.objects.create(id=s1, ord_id=s2, shipping_date=s3, estimated_delivery_date=s4, shipping_address=s5)

        return render(request, 'shipping.html')
    return render(request, "shipping.html")

def customerview(request):
    userdict=customer.objects.all()
    return render(request,'viewcustomer.html',{'userdict':userdict})

def UserLoginview(request):
    userdict=UserLogin.objects.all()
    return render(request,'viewUserLogin.html',{'userdict' : userdict})


def supplierview(request):
    userdict=supplier.objects.all()
    return render(request,'viewsupplier.html',{'userdict' : userdict})

def spare_partview(request):
    userdict=spare_part.objects.all()
    return render(request,'viewspare_part.html',{'userdict' : userdict})

def adminspare_partview(request):
    userdict=spare_part.objects.all()
    return render(request,'aviewspare_part.html',{'userdict' : userdict})

def orderview(request):
    userdict=order.objects.all()
    return render(request,'vieworder.html',{'userdict' : userdict})



def paymentsview(request):
    userdict=payment.objects.all()
    return render(request,'viewpayment.html',{'userdict' : userdict})

def shippingview(request):
    userdict=shipping.objects.all()
    return render(request,'viewshipping.html',{'userdict' : userdict})





def forgotpassword(request):
    if request.method=="POST":
        uname = request.POST.get('t1', '')
        user = UserLogin.objects.filter(username=uname).count()
        if user >= 1:
            userlog = UserLogin.objects.filter(username=uname).values()
            for u in userlog:
                upass= u['password']
                content = upass
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('jaisiaram1975@gmail.com', 'slgvpjtkzwyqvvzn')
                mail.sendmail('jaisiaram1975@gmail.com', uname , content)
                mail.close()
                return render(request,'login.html', {'msg': 'Your password has been sent to your E-mail'})
        else:
            return render(request,'forgotpassword.html', {'msg': 'Enter a valid username'})
    return render(request,'forgotpassword.html')