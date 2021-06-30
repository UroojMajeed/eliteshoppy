from django.db import models
from django.contrib.auth.models import User

class sign_up(models.Model):
    us_first_name=models.CharField(max_length=30)
    us_last_name=models.CharField(max_length=30)
    us_email=models.CharField(max_length=50)
    us_password=models.CharField(max_length=20)
    us_phone=models.CharField(max_length=15, null=True)
    us_DOB=models.DateField(max_length=20)
    us_date=models.DateField(max_length=20)
    us_time=models.TimeField(max_length=15)

    def __str__(self):
     return self.us_first_name
    
class userlogin(models.Model):
    u_name=models.CharField(max_length=30)
    u_password=models.CharField(max_length=30)
    u_date=models.DateField(max_length=20)
    u_time=models.TimeField(max_length=15)
    sign_up=models.ForeignKey(sign_up, on_delete=models.CASCADE)

    def __str__(self):
        return self.u_name

class employee_login(models.Model):
    el_name=models.CharField(max_length=30)
    el_password=models.CharField(max_length=20)
    el_date=models.DateField(max_length=20)
    el_time=models.TimeField(max_length=15)
    user_login=models.ForeignKey(userlogin, on_delete=models.CASCADE)

    def __str__(self):
        return self.el_name

class employee_personal(models.Model):
    e_name=models.CharField(max_length=15)
    e_fathername=models.CharField(max_length=15)
    e_CNIC=models.CharField(max_length=15)
    e_DOB=models.CharField(max_length=30)
    e_gender=models.CharField(max_length=20, null=True)
    e_address=models.CharField(max_length=50)
    e_city=models.CharField(max_length=15)
    e_postal_code=models.CharField(max_length=10, null=True)
    e_date=models.DateField(max_length=20)
    e_time=models.TimeField(max_length=15)

    def __str__(self):
        return self.e_name

class employee_qualification(models.Model):
    eq_qualification=models.CharField(max_length=20)
    eq_institute=models.CharField(max_length=50)
    eq_marks_or_CGPA=models.CharField(max_length=10)
    eq_subject=models.CharField(max_length=20)
    eq_board=models.CharField(max_length=20)
    eq_percentage=models.CharField(max_length=510)
    eq_reg_no=models.CharField(max_length=20)
    eq_year=models.CharField(max_length=10)
    eq_date=models.DateField(max_length=20)
    eq_time=models.TimeField(max_length=15)
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE)

    def __str__(self):
        return self.eq_qualification

class employee_skills(models.Model):
    es_skills=models.CharField(max_length=30)
    es_certification=models.CharField(max_length=20)
    es_organization=models.CharField(max_length=50)
    es_year=models.CharField(max_length=10)
    es_date=models.DateField(max_length=20)
    es_time=models.TimeField(max_length=15)
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE)

    def __str__(self):
        return self.es_skills

class employee_contact(models.Model):
    ec_phone=models.CharField(max_length=12)
    ec_email=models.CharField(max_length=30)
    ec_date=models.DateField(max_length=20)
    ec_time=models.TimeField(max_length=15)
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return self.ec_phone

class employee_experience(models.Model):
    ee_fresh_or_experienced=models.CharField(max_length=15)
    ee_designation=models.CharField(max_length=20)
    ee_organization=models.CharField(max_length=50)
    ee_joining_date=models.DateField(max_length=20)
    ee_leaving_date=models.DateField(max_length=20)
    ee_NOC=models.CharField(max_length=20)
    ee_leaving_reason=models.CharField(max_length=50)
    ee_date=models.DateField(max_length=20)
    ee_time=models.TimeField(max_length=15)
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE)  

    def __str__(self):
        return self.ee_fresh_or_experienced

class employee_duty_timing(models.Model):
    ed_department=models.CharField(max_length=30)
    ed_designation=models.CharField(max_length=30)
    ed_salary=models.IntegerField()
    ed_shift=models.CharField(max_length=15)
    ed_duty_time=models.CharField(max_length=30)
    ed_vacations=models.CharField(max_length=10)
    ed_bonus=models.IntegerField()
    ed_date=models.DateField(max_length=20)
    ed_time=models.TimeField(max_length=15)
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return self.ed_department

class distributer_personal(models.Model):
    d_name=models.CharField(max_length=20)
    d_address=models.CharField(max_length=50)
    d_city=models.CharField(max_length=15)
    d_reg_no=models.CharField(max_length=20)
    d_fax_no=models.CharField(max_length=20)
    d_toll_free_no=models.CharField(max_length=20)
    d_ISO_no=models.CharField(max_length=20)
    d_postalcode=models.CharField(max_length=10)
    d_type=models.CharField(max_length=10)

    def __str__(self):
        return self.d_name

class distributer_contact(models.Model):
    dc_phone=models.CharField(max_length=20)
    dc_email=models.CharField(max_length=50)
    dc_date=models.DateField(max_length=20)
    dc_time=models.TimeField(max_length=15)
    distributer_name=models.ForeignKey(distributer_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return self.dc_phone

class distributer_brand(models.Model):
    dbr_name=models.CharField(max_length=20)
    dbr_type=models.CharField(max_length=15)
    dbr_description=models.CharField(max_length=50)
    dbr_manufacturing_detail=models.CharField(max_length=30)
    dbr_date=models.DateField(max_length=20)
    dbr_time=models.TimeField(max_length=15)
    distributer_name=models.ForeignKey(distributer_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return self.dbr_name

class distributer_professional(models.Model):
    dpr_category=models.CharField(max_length=30)
    dpr_date=models.DateField(max_length=20)
    dpr_time=models.TimeField(max_length=15)
    distributer_name=models.ForeignKey(distributer_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return self.dpr_category

class distributer_representator(models.Model):
    dr_name=models.CharField(max_length=30)
    dr_father_name=models.CharField(max_length=30, null=True)
    dr_designation=models.CharField(max_length=20)
    dr_phone=models.CharField(max_length=15)
    dr_email=models.CharField(max_length=50)
    dr_date=models.DateField(max_length=20)
    dr_time=models.TimeField(max_length=15)
    distributer_name=models.ForeignKey(distributer_personal, on_delete=models.CASCADE)  

    def __str__(self):
        return self.dr_name

class product_personal(models.Model):
    p_name=models.CharField(max_length=30)
    p_quality=models.CharField(max_length=20)
    p_color=models.CharField(max_length=20)
    p_size=models.CharField(max_length=20)
    p_stuff=models.CharField(max_length=20)
    brand_name=models.ForeignKey(distributer_brand, on_delete=models.CASCADE)  

    def __str__(self):
        return self.p_name

class product_professional(models.Model):
    pr_purchase_unit_price=models.IntegerField()
    pr_purchase_bulk_price=models.IntegerField()   
    pr_sale_unit_price=models.IntegerField()
    pr_sale_bulk_price=models.IntegerField()
    pr_bulk_quantity=models.CharField(max_length=20)
    pr_date=models.DateField(max_length=20)
    pr_time=models.TimeField(max_length=15)
    product_name=models.ForeignKey(product_personal, on_delete=models.CASCADE)  

    def __str__(self):
        return str(self.pr_purchase_unit_price)


class stock_order_booking(models.Model):
    sob_invoice_no=models.CharField(max_length=20)
    sob_total_bill=models.IntegerField()
    sob_booking_date=models.DateField(max_length=20)
    sob_delivery_date=models.DateField(max_length=20)
    sob_date=models.DateField(max_length=20)
    sob_time=models.TimeField(max_length=15)
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE)  
    distributer_name=models.ForeignKey(distributer_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return self.sob_invoice_no

class current_stock(models.Model):
    cs_product_name=models.CharField(max_length=20)
    cs_quantity=models.CharField(max_length=30)
    cs_unit_price=models.IntegerField()
    cs_date=models.DateField(max_length=20)
    cs_time=models.TimeField(max_length=15)

    def __str__(self):
        return self.cs_product_name

class stock_order_detail(models.Model):
    sod_quantity=models.CharField(max_length=30)
    sod_unit_price=models.IntegerField()
    sod_bulk_price=models.IntegerField()
    sod_packing_detail=models.CharField(max_length=30)
    sod_status=models.CharField(max_length=20)
    product_name=models.ForeignKey(product_personal, on_delete=models.CASCADE)  
    product_purchase_unitprice=models.ForeignKey(product_professional, on_delete=models.CASCADE) 
    stock_invoice=models.ForeignKey(stock_order_booking, on_delete=models.CASCADE) 
    currentstock_product=models.ForeignKey(current_stock, on_delete=models.CASCADE) 

    def __str__(self):
        return self.sod_quantity  

class stock_order_payment(models.Model):
    sop_payment=models.IntegerField()
    sop_medium=models.CharField(max_length=20)
    sop_date=models.DateField(max_length=20)
    sop_time=models.TimeField(max_length=15)
    stock_total_bill=models.ForeignKey(stock_order_booking, on_delete=models.CASCADE)   
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.sop_payment)

class customer_personal(models.Model):
    c_name=models.CharField(max_length=30)
    c_phone=models.CharField(max_length=15, null=True)
    c_CNIC=models.CharField(max_length=15)
    c_email=models.CharField(max_length=20)
    c_address=models.CharField(max_length=50)
    c_city=models.CharField(max_length=20)
    c_postal_code=models.CharField(max_length=20)
    c_date=models.DateField(max_length=20)
    c_time=models.TimeField(max_length=15)  

    def __str__(self):
        return self.c_name

class customer_order_booking(models.Model):
    cob_total_bill=models.IntegerField()
    cob_total_product=models.CharField(max_length=20)
    cob_invoice_no=models.CharField(max_length=30)
    cob_booking_date=models.DateField(max_length=20)
    cob_delivery_date=models.DateField(max_length=20)
    cob_date=models.DateField(max_length=20)
    cob_time=models.TimeField(max_length=15)
    customer_name=models.ForeignKey(customer_personal, on_delete=models.CASCADE)  
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE)  

    def __str__(self):
        return self.cob_invoice_no

class customer_order_detail(models.Model):
    cod_product_name=models.CharField(max_length=30)
    cod_quantity=models.CharField(max_length=30)
    cod_sale_unit_price=models.IntegerField()
    cod_sale_bulk_price=models.IntegerField()
    customer_name=models.ForeignKey(customer_personal, on_delete=models.CASCADE) 
    product_name=models.ForeignKey(product_personal, on_delete=models.CASCADE)  
    product_sale_unitprice=models.ForeignKey(product_professional, on_delete=models.CASCADE) 
    currentstock_product=models.ForeignKey(current_stock, on_delete=models.CASCADE) 

    def __str__(self):
        return self.cod_product_name

class customer_order_payment(models.Model):
    cop_amount=models.IntegerField()
    cop_date=models.DateField(max_length=20)
    cop_time=models.TimeField(max_length=15)
    total_bill=models.ForeignKey(customer_order_booking, on_delete=models.CASCADE)  
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return str (self.cop_amount)

class expenditure(models.Model):
    ex_type=models.CharField(max_length=30)
    ex_description=models.CharField(max_length=60)
    ex_amount=models.IntegerField()
    ex_receipt=models.ImageField()
    ex_date=models.DateField(max_length=20)
    ex_time=models.TimeField(max_length=15)  
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE) 

    def __str__(self):
        return self.ex_type

class net_income(models.Model):
    n_starting_date=models.DateField(max_length=20)
    n_ending_date=models.DateField(max_length=20)
    n_amount_paid=models.IntegerField()
    n_amount_received=models.IntegerField()
    n_amount_due=models.IntegerField()
    employee_name=models.ForeignKey(employee_personal, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.n_starting_date)

CATEGORY_CHOICES=[
    ('M', 'MENS'),
    ('W', 'WOMENS'),
    ('B', 'BAGS'),
    ('F', 'FOOTWEARS'),
    
]

class product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.DecimalField(max_digits=5, decimal_places=2)
    product_image_front=models.ImageField(upload_to='images')
    product_image_back=models.ImageField(upload_to='images')
    product_spects=models.CharField(max_length=200)
    product_date=models.DateField(auto_now=True)
    category = models.CharField(max_length=1,
    choices=CATEGORY_CHOICES, default='Pending')
    def __str__(self):
        return str (self.product_name)

class arrivals(models.Model):
    Season=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    date=models.DateField(auto_now=True)

class sale(models.Model):
       
    s_save=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='images')
    description=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
class trending(models.Model):
       
    w_sale=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='images')
    w_description=models.CharField(max_length=100)
    m_sale=models.CharField(max_length=100)
    image2=models.ImageField(upload_to='images')
    m_description=models.CharField(max_length=100)
    f_sale=models.CharField(max_length=100)
    image3=models.ImageField(upload_to='images')
    f_description=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
class discount(models.Model):
       
    w_sale=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='images')
    m_sale=models.CharField(max_length=100)
    image2=models.ImageField(upload_to='images')
    date=models.DateField(auto_now=True)
class shoppy(models.Model):
       
    about=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='images')
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)
class members(models.Model):
       
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)
class exclusive(models.Model):
       
    ex_men=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)
class exclusiveW(models.Model):
       
    ex_women=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)
class excl(models.Model):
       
    ex_women=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)
class contact(models.Model):
       
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)
class information(models.Model):
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    phone1=models.CharField(max_length=30)
    phone2=models.CharField(max_length=50)
    email1=models.CharField(max_length=20)
    email2=models.CharField(max_length=20)
    date=models.DateField(auto_now=True)
class foot(models.Model):
    shipping=models.CharField(max_length=100)
    support=models.CharField(max_length=100)
    money=models.CharField(max_length=100)
    coupons=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
class carts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(product, on_delete=models.CASCADE)       
    quantity=models.IntegerField(default='1')
    
    def __str__(self):
        return str (self.user)
    @property
    def total_cost(self):
        return self.quantity * self.product.product_price
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15, null=True)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    postal_code=models.IntegerField()
    state=models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class reqq(models.Model):
   
    def __str__(self):
        return str(self.id)

class Placed(models.Model):
    order = models.ForeignKey(reqq, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product = models.ForeignKey(product, on_delete=models.CASCADE)   
    quantity=models.IntegerField(default='1')
    
    def __str__(self):
        return str(self.order)