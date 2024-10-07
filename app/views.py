from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def Basic_Form(request):
    if request.method =='POST':
        un=request.POST['usn']
        ps=request.POST['psw']
        print(un)
        print(ps)
        return HttpResponse('Data is stored in the Database')
    return render(request,'Basic_Form.html')

def Customer_form(request):
    if request.method=='POST':
        ID=request.POST['c_id']
        NAME=request.POST['c_n']
        ADDRESS=request.POST['c_add']
        obj1=Customer_Details.objects.create(Customer_Id=ID,Customer_Name=NAME,Customer_Address=ADDRESS)
        obj1.save()
        return HttpResponse('Customer data is inserted successfully')
    return render(request,'Customer.html')

def Product_Form(request):
    if request.method=='POST':
        id=request.POST['p_id']
        cu_id=request.POST['c_id']
        product_name=request.POST['p_n']

        if Customer_Details.objects.filter(Customer_Id=cu_id).exists():
            obj1=Customer_Details.objects.get(Customer_Id=cu_id)
            obj2=Product_Details.objects.create(Product_Id=id,Customer_Id=obj1,Product_Name=product_name)
            obj2.save()
            return HttpResponse('Product Details inserted Successfully')
        else:
            return HttpResponse('Customer is present in the data pls first add the customer')
    return render(request,'Product.html')

def Display_Customer_Details(request):
    QST=Customer_Details.objects.all()
    data={'Customer_Details':QST}
    return render(request,'Display_Cus_Details.html',data)

def Display_Product_Deatils(request):
    QST=Product_Details.objects.all()
    data={'Product_Details':QST}
    return render(request,'Display_Product_Details.html',data)



