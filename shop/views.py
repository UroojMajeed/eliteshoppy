from django.shortcuts import render
from django.views import View
from  .models import product,arrivals,sale,trending,discount,shoppy,members,exclusive,exclusiveW,sign_up,contact,information,foot,carts,Customer,Placed,reqq
from .forms import *
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from decimal import *
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Max
from cart.cart import Cart
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template, RequestContext

def home(request):
    return render(request,'shop/index.html')
def about(request):
    return render(request,'shop/about.html')
#def contact(request):
   # return render(request,'shop/contact.html')
def mens(request):
    return render(request,'shop/mens.html')
def womens(request):
    return render(request,'shop/womens.html')
def login(request):
    return render(request,'shop/login.html')
#def single(request):
    #return render(request,'shop/single.html')
@ login_required
def checkout(request):
    user=request.user
    product_id = request.GET.get('prod_id')
    Product = product.objects.get(id=product_id)
    carts(user=user, product=Product).save()
    return redirect('/cart') 
@ login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = carts.objects.filter(user=user)
        #print(cart)
        amount = 0
        shipping_amount = 1
        total_amount = 0
        cart_product = [p for p in carts.objects.all() if p.user == user]
        #print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.product_price)
                amount += tempamount
                totalamount = amount+shipping_amount
            return render(request,'shop/checkout.html', {'cart':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render (request,'shop/emptycart.html')
def index1(request):
    qs= sign_up.objects.all()
    print(qs)    
    
    return render(request, 'shop/index1.html', {'dat':qs})


class ProductView(View):
    def get(self, request):
        mens=product.objects.filter(category='M')
        womens=product.objects.filter(category='W')
        bags=product.objects.filter(category='B')
        footwear=product.objects.filter(category='F')
        a= arrivals.objects.all()
        b= sale.objects.all()
        c= trending.objects.all()
        d= discount.objects.all()
        h=information.objects.all()
        l=foot.objects.all()
        form = CustomerRegistraionForm()
        return render(request, 'shop/index.html', {'MENS':mens,'WOMENS':womens,'BAGS':bags,'FOOTWEARS':footwear,'A':a,'B':b,'C':c,'D':d, 'H':h,'L':l,'form':form})
    def post(self, request):
        mens=product.objects.filter(category='M')
        womens=product.objects.filter(category='W')
        bags=product.objects.filter(category='B')
        footwear=product.objects.filter(category='F')
        a= arrivals.objects.all()
        b= sale.objects.all()
        c= trending.objects.all()
        d= discount.objects.all()
        h=information.objects.all()
        l=foot.objects.all()
        form = CustomerRegistraionForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully')
            form.save()
        return render(request, 'shop/index.html',{'MENS':mens,'WOMENS':womens,'BAGS':bags,'FOOTWEARS':footwear,'A':a,'B':b,'C':c,'D':d, 'H':h,'L':l,'form':form})
        
class ProductView1(View):
    def get(self, request):
        mens=product.objects.filter(category='M')
        g= exclusive.objects.all()
        h=information.objects.all()
        l=foot.objects.all()
       
        return render(request, 'shop/mens.html', {'MENS':mens,'G':g,'H':h,'L':l})
class ProductView2(View):
    def get(self, request):
        womens=product.objects.filter(category='W')
        h= exclusiveW.objects.all() 
        l=information.objects.all()
        j=foot.objects.all()
      
        return render(request, 'shop/womens.html', {'WOMENS':womens,'H':h,'L':l,'J':j})
    
class ProductView3(View):
    def get(self, request):
        a= arrivals.objects.all() 
        b= sale.objects.all()
        c= trending.objects.all()
        d= discount.objects.all()
        e= shoppy.objects.all()
        f= members.objects.all()
        h=information.objects.all()
        l=foot.objects.all()
      
        return render(request, 'shop/about.html', {'A':a,'B':b,'C':c,'D':d,'E':e,'F':f,'H':h,'L':l})
    
def saveproduct(request):
    form = addproduct()
    if request.method == 'POST':
        form = addproduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form.errors    
    context ={'form':form}
    return render(request,'shop/product.html',context)
def edit_data(request, pk):
    form1= product.objects.get(id=pk)
    print(form1)
    form=addproduct(instance=form1)
    if request.method == 'POST':
         form = addproduct(request.POST, instance=form1)
         if form.is_valid():
            form.save()
            return redirect('/')
         else:
             form.errors       
    context ={'form':form}
    return render(request,'shop/product.html',context)
def del_product(request, id):
    f= product.objects.get(pk=id)
    
    f.delete()
    return redirect('/')

class productdetailview(View):
    def get(self, request, pk):
     p= product.objects.get(pk=pk)
     form = CustomerRegistraionForm()
     return render(request,'shop/single.html', {'P':p,'form':form})
    def post(self, request, pk):
        p= product.objects.get(pk=pk)
        form = CustomerRegistraionForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully')
            form.save()
        return render(request, 'shop/single.html',{'P':p,'form':form})


def savecontact1(request):
    form = addcontact()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        form= contact(name=name,email=email,subject=subject,message=message)
        form.save()
        print(form)
         
    else:
        HttpResponse('no data')
    j=contact.objects.all()
    h=information.objects.all()
    l=foot.objects.all()
    form = CustomerRegistraionForm()
    context ={'form':form,'J':j,'H':h,'L':l}
    
    return render(request,'shop/contact.html',context)

def edit_contact(request, pk):
    form1= contact.objects.get(id=pk)
    print(form1)
    form=addcontact1(instance=form1)
    if request.method == 'POST':
         form = addcontact1(request.POST, instance=form1)
         if form.is_valid():
            form.save()
            return redirect('/contact')
         else:
             form.errors       
    context ={'form':form}
    return render(request,'shop/contact1.html',context)
def del_contact(request, id):
    f= contact.objects.get(pk=id)
    
    f.delete()
    
    return redirect('/contact')
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
       
        c = carts.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0
        shipping_amount = 1
        cart_product = [p for p in carts.objects.all() if p.user == request.user]
        for p in cart_product:
           tempamount = (p.quantity * p.product.product_price)
           amount += tempamount

        data = {
             'quantity' : c.quantity,
             'amount' : amount,
             'totalamount' : amount + shipping_amount
         }
        return JsonResponse(data) 
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
       
        c = carts.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0
        shipping_amount = 1
        cart_product = [p for p in carts.objects.all() if p.user == request.user]
        for p in cart_product:
           tempamount = (p.quantity * p.product.product_price)
           amount += tempamount

        data = {
             'quantity' : c.quantity,
             'amount' : amount,
             'totalamount' : amount + shipping_amount
         }
        return JsonResponse(data) 
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
       
        c = carts.objects.get(Q(product=prod_id) & Q(user=request.user))
       
        c.delete()
        amount = 0
        shipping_amount = 1
        cart_product = [p for p in carts.objects.all() if p.user == request.user]
        for p in cart_product:
           tempamount = (p.quantity * p.product.product_price)
           amount += tempamount

        data = {
            
             'amount' : amount,
             'totalamount' : amount + shipping_amount
         }
        return JsonResponse(data) 
def emptycart(request):
    
    h=information.objects.all()
    l=foot.objects.all()
    return render(request,'shop/emptycart.html',{'H':h,'L':l})
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):

        form =  CustomerProfileForm()
        return render(request,'shop/profile.html',{'form':form})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
          usr = request.user
          name = form.cleaned_data['name']
          phone = form.cleaned_data['phone']
          email = form.cleaned_data['email']
          address = form.cleaned_data['address']
          city = form.cleaned_data['city']
          postal_code = form.cleaned_data['postal_code'] 
          state = form.cleaned_data['state']
          reg = Customer(user=usr,name=name,phone=phone,email=email,address=address,city=city,postal_code=postal_code,state=state)
          reg.save()
        return render(request, 'shop/profile.html',{'form':form})

@ login_required
def placeorder(request):
    h=information.objects.all()
    l=foot.objects.all()
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = carts.objects.filter(user=user)
    amount = 0
    shipping_amount = 1
    totalamount = 0
    cart_product = [p for p in carts.objects.all() if p.user == request.user]
    if cart_product:
      for p in cart_product:
        tempamount = (p.quantity * p.product.product_price)
        amount += tempamount
      totalamount = amount + shipping_amount
        
    return render(request,'shop/placeorder.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items,'H':h,'L':l})
@ login_required  
def payment_done(request):
    
    user = request.user
    reqq.objects.create()
    max_val=reqq.objects.latest('id')
    print(max_val)
    custid = request.GET.get('custid') 
    customer = Customer.objects.get(id=custid)
    cart = carts.objects.filter(user=user)
    user = request.user

    cart_items = carts.objects.filter(user=user)
    amount = 0
    shipping_amount = 1
    totalamount = 0
    cart_product = [p for p in carts.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.product_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    msg_plain = render_to_string('email.txt')
    context = {'cart_items':cart_items,'totalamount':totalamount}
    msg_html = render_to_string('email.html', context)
    #recipient =  request.user.email
    send_mail("Your order has been placed", msg_plain, settings.EMAIL_HOST_USER,
              [user.email], html_message = msg_html)
    
    for c in cart:
        Placed.objects.create(order=max_val, Product=c.product, quantity=c.quantity,Customer=customer,user=user)
       
        c.delete()
    
    return render(request, 'shop/order_complete.html', {'cart_items':cart_items, 'totalamount':totalamount})
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
       return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
class ViewPDF(View):
    
    def get(self, request , *args, **kwargs):
        user = request.user

        cart_items = carts.objects.filter(user=user)
        amount = 0
        shipping_amount = 1
        totalamount = 0
        cart_product = [p for p in carts.objects.all() if p.user == request.user]
        if cart_product:
           for p in cart_product:
              tempamount = (p.quantity * p.product.product_price)
              amount += tempamount
           totalamount = amount + shipping_amount
        context = {'cart_items':cart_items,'totalamount':totalamount}
        pdf = render_to_pdf('shop/pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
class DownloadPDF(View):
    	def get(self, request, *args, **kwargs):
            user = request.user

            cart_items = carts.objects.filter(user=user)
            amount = 0
            shipping_amount = 1
            totalamount = 0
            cart_product = [p for p in carts.objects.all() if p.user == request.user]
            if cart_product:
               for p in cart_product:
                   tempamount = (p.quantity * p.product.product_price)
                   amount += tempamount
               totalamount = amount + shipping_amount
            context = {'cart_items':cart_items,'totalamount':totalamount}
            pdf = render_to_pdf('shop/pdf.html', context)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
def reset(request):
    form = MyPasswordResetForm()
    if request.method == 'POST':
        form = MyPasswordResetForm(request.POST)
        if form.is_valid():
            subject = 'Reset Password'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
               settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('password_reset')
    return render(request, 'shop/index.html', {'form': form})
def order_complete(request):
    return render(request,'shop/order_complete.html')
