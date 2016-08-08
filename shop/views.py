from django.shortcuts import render_to_response
from django import http
from django.core import paginator
from django.contrib import auth
from django.contrib.auth import forms
from django.contrib.auth.models import User, Group
from django.core.context_processors import csrf
from datetime import datetime
import json
from shop import models
from shop import shop_forms
from my_cms import cms_models


def user_info(request):
    args = {}
    args["auth_user"] = request.user.is_authenticated()
    args["user"] = request.user

    if request.user.is_staff:
        staff_user = True
    else:
        staff_user = False
    args["staff_user"] = staff_user

    return args


def check_user(request):
    user_login = request.POST.get("login")
    user_password = request.POST.get("password")

    if user_login and user_password:
        user = auth.authenticate(username=user_login, password=user_password)
    else:
        return "Заполните все поля!"

    if user and user.is_active:
        auth.login(request, user)
        return True
    else:
        return "Не верный логин или пароль!"


def create_news(news=True):
    args = {}
    if news:
        all_news = models.News.objects.all()
    else:
        all_news = models.News.objects.all()[:2]

    news_dict = {}
    for n in all_news:
        news_dict[n] = n.images.all()

    args["news_dict"] = news_dict
    return args


def create_pagination(list_item, page=1):
    page_list = paginator.Paginator(list_item, 6)
    try:
        choose_page = page_list.page(page)
    except:
        choose_page = page_list.page(1)

    if page_list.num_pages > 1:
        show_pagination = True
    else:
        show_pagination = False

    return (page_list, choose_page, show_pagination)


def navigation():
    args = {}
    navigation = cms_models.Navigation.objects.all()
    args["navigation"] = navigation
    return args


def contact_info():
    args = {}
    try:
        contact_info = cms_models.ContactInfo.objects.all()[0]
    except IndexError:
        contact_info = ""
    args["contact_info"] = contact_info
    return args
# =================================================================================


def index(request):
    args = navigation()
    args.update(create_news(news=False))
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))

    description = cms_models.Description.objects.all()

    form = shop_forms.RecordForm()
    args["form"] = form
    all_photos = models.PhotoGallery.objects.all()
    photo_gallery = []
    for photo in all_photos:
        photo_gallery.append(photo.img.url)

    args["photo_gallery"] = photo_gallery

    args["description"] = description
    args["show_logo"] = True
    args["url"] = '/'

    if request.method == 'POST':
        post_name = request.POST.get("post_name")
        if post_name == "login":
            result = check_user(request)
            if result is True:
                # args.update(user_info(request))
                if request.is_ajax():
                    return http.HttpResponse("ok", content_type="text/html")
                else:
                    return http.HttpResponseRedirect("/")
            else:
                args["error"] = result
                if request.is_ajax():
                    return http.HttpResponse(result, content_type="text/html")
                else:
                    return render_to_response("Index.html", args)
        elif post_name == "record":
            form = shop_forms.RecordForm(request.POST)
            args["form"] = form
            if form.is_valid():
                tel_number = form.cleaned_data["tel_number"]
                if not tel_number.isdigit():
                    args["error"] = "Номер телефона должен содержать только цифры!"
                    return render_to_response("Index.html", args)

                name = form.cleaned_data["name"]
                time = form.cleaned_data["time"]
                date = form.cleaned_data["date"]
                if request.user.is_authenticated():
                    models.Record.objects.create(user_key=request.user, name=name, tel_number=tel_number,
                                                 time=time, date=date)
                else:
                    models.Record.objects.create(name=name, tel_number=tel_number, time=time, date=date)
                # args["record_successful"] = "True"
                return http.HttpResponseRedirect("/?record_successful=True")
    else:
        args["record_successful"] = request.GET.get("record_successful")

    return render_to_response("Index.html", args)


def product(request):
    args = navigation()
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))

    prod_name = request.GET.get("prod_name")
    if prod_name is None:
        return http.HttpResponseRedirect("/shop/")

    product = models.Product.objects.filter(product_name=prod_name)
    if product:
        product = product[0]
    else:
        return http.HttpResponseRedirect("/shop/")

    images = product.images.all()
    if product.in_kit:
        in_kit = product.in_kit.split(',')
        in_kit[:] = [item.strip() for item in in_kit]
        product.in_kit = in_kit
    else:
        product.in_kit = False
    args["product"] = product
    args["images"] = images
    args["url"] = "/shop/product/?prod_name={0}".format(prod_name)

    if request.method == 'POST':
        result = check_user(request)
        if result is True:
            args.update(user_info(request))
            return render_to_response("Product.html", args)
            # return http.HttpResponseRedirect("/shop/product/?prod_name={0}".format(prod_name))
        else:
            args["error"] = result
            return render_to_response("Product.html", args)
    return render_to_response("Product.html", args)


def order(request):
    args = navigation()
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))

    prod_name = request.GET.get("prod_name")

    if prod_name is None:
        return http.HttpResponseRedirect("/shop/")

    products = models.Product.objects.filter(product_name=prod_name)
    if products:
        price = products[0].price
    else:
        return http.HttpResponseRedirect("/shop/")

    form = shop_forms.OrderForm()

    args["order_successful"] = request.GET.get("order_successful")
    args["form"] = form
    args["prod_name"] = prod_name
    args["price"] = price
    args["url"] = "/order/?prod_name={0}".format(prod_name)

    if request.method == 'POST':
        post_name = request.POST.get("post_name")
        if post_name == "order":
            form = shop_forms.OrderForm(request.POST)
            if form.is_valid():
                tel_number = form.cleaned_data["tel_number"]
                if not tel_number.isdigit():
                    args["error"] = "Номер телефона должен содержать только цифры!"
                    args["form"] = form
                    args["prod_name"] = prod_name
                    args["price"] = price
                    return render_to_response("Order.html", args)

                full_name = form.cleaned_data["full_name"]
                address = form.cleaned_data["address"]
                if request.user.is_authenticated():
                    models.Order.objects.create(user_key=request.user, full_name=full_name, address=address, tel_number=tel_number,
                                                product_name=prod_name, price=price, order_date=datetime.now())
                else:
                    models.Order.objects.create(full_name=full_name, address=address, tel_number=tel_number,
                                                product_name=prod_name, price=price, order_date=datetime.now())

                return http.HttpResponseRedirect("/order/?order_successful=True&prod_name={0}".format(prod_name))
            else:
                args["form"] = form
                args["prod_name"] = prod_name
                args["price"] = price
                return render_to_response("Order.html", args)

        elif post_name == "login":
            result = check_user(request)
            if result is True:
                args.update(user_info(request))
                return render_to_response("Order.html", args)
                # return http.HttpResponseRedirect("/shop/product/?prod_name={0}".format(prod_name))
                # return http.HttpResponseRedirect("/shop/product/?prod_name={0}".format(prod_name))
            else:
                args["error"] = result
                return render_to_response("Order.html", args)

    return render_to_response("Order.html", args)


def price_list(request):
    args = navigation()
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))
    manufacturers = cms_models.ManufacturerList.objects.all()
    price_services = cms_models.PriceTable.objects.all()
    about_us = cms_models.AboutUs.objects.all()

    args["manufacturers"] = manufacturers[:4]
    args["price_services"] = price_services
    args["about_us"] = about_us
    args["url"] = "/price_list/"

    if request.method == 'POST':
        result = check_user(request)
        if result is True:
            return http.HttpResponseRedirect("/price_list/")
        else:
            args["error"] = result
            return render_to_response("Price-list.html", args)

    return render_to_response("Price-list.html", args)


def shop(request):
    args = navigation()
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))
    manufacturers = cms_models.ManufacturerList.objects.all()
    groups = cms_models.ProductGroup.objects.all()
    args["manufacturers"] = manufacturers
    args["groups"] = groups
    args["url"] = "/shop/"

    if request.method == 'GET':
        all_products = models.Product.objects.all()
        for product in all_products:
            product.in_kit_list = product.in_kit.split(',')
            product.in_kit_list[:] = [kit_item.strip() for kit_item in product.in_kit_list]
            prod_images = product.images.all()
            if prod_images:
                product.image = prod_images[0]

        page = request.GET.get("page")
        page_list, prod_page, show_pagination = create_pagination(all_products, page)

        if request.GET.get("error"):
            args['error'] = request.GET.get("error")
        args["products"] = all_products
        args["page_list"] = page_list
        args["prod_page"] = prod_page
        args["show_pagination"] = show_pagination
    else:
        post_name = request.POST.get("post_name")
        if post_name == "login":
            result = check_user(request)
            if result is True:
                http.HttpResponseRedirect("/shop/")
            else:
                return http.HttpResponseRedirect("/shop/?error={0}".format(result))

        manufacturers = request.POST.getlist('manufacturers')
        group = request.POST.get("group")

        if not manufacturers and not group:
            return http.HttpResponseRedirect("/shop/")
        manufacturers_list = []

        if not manufacturers:
            group_obj = cms_models.ProductGroup.objects.get(name=group)
            products = models.Product.objects.filter(group=group_obj.id)
            print(products)
            for prod in products:
                prod.image = prod.images.all()[0]
            page_list, prod_page, show_pagination = create_pagination(products)

            args["page_list"] = page_list
            args["prod_page"] = prod_page
            args["show_pagination"] = show_pagination
            return render_to_response("Shop.html", args)

        elif not group:
            for manufacturer in manufacturers:
                manufacturer_obj = cms_models.ManufacturerList.objects.get(name=manufacturer)
                products = models.Product.objects.filter(manufacturer=manufacturer_obj.id)
                for prod in products:
                    prod.image = prod.images.all()[0]
                manufacturers_list.extend(products)

            page_list, prod_page, show_pagination = create_pagination(manufacturers_list)

            args["page_list"] = page_list
            args["prod_page"] = prod_page
            args["show_pagination"] = show_pagination
            return render_to_response("Shop.html", args)

        for manufacturer in manufacturers:
            manufacturer_obj = cms_models.ManufacturerList.objects.get(name=manufacturer)
            group_obj = cms_models.ProductGroup.objects.get(name=group)
            products = models.Product.objects.filter(manufacturer=manufacturer_obj.id, group=group_obj.id)
            for prod in products:
                prod.image = prod.images.all()[0]
            manufacturers_list.extend(products)

        page_list, prod_page, show_pagination = create_pagination(manufacturers_list)

        args["page_list"] = page_list
        args["prod_page"] = prod_page
        args["show_pagination"] = show_pagination

    return render_to_response("Shop.html", args)


def news(request):
    args = navigation()
    args.update(create_news())
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))
    args["url"] = "/news/"

    if request.method == 'POST':
        result = check_user(request)
        if result is True:
            return http.HttpResponseRedirect("/news/")
        else:
            args["error"] = result

    return render_to_response("News.html", args)


def logout(request):
    auth.logout(request)
    page = request.GET.get("page")
    if page:
        return http.HttpResponseRedirect(page)
    else:
        return http.HttpResponseRedirect("/")


def registration(request):
    args = navigation()
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))
    args["url"] = "/registration/"

    if request.method == 'POST':
        post_name = request.POST.get("post_name")
        if post_name == "login":
            result = check_user(request)
            if result is True:
                return http.HttpResponseRedirect("/registration/")
            else:
                args["reg_form"] = forms.UserCreationForm()
                args["error"] = result
                return render_to_response("Registration.html", args)
        elif post_name == "registration":
            reg_form = forms.UserCreationForm(request.POST)
            args["reg_form"] = reg_form

            if reg_form.is_valid():
                user_password = request.POST.get("password1")
                user_login = request.POST.get("username")
                full_name = request.POST.get("full_name")

                user = User.objects.create_user(user_login, None, user_password)

                User.objects.filter(username=user_login).update(first_name=full_name)
                group = Group.objects.get(name="Зарегистрированные пользователи")
                user.groups.add(group)

                user = auth.authenticate(username=user_login, password=user_password)
                auth.login(request, user)
                if request.is_ajax():
                    return http.HttpResponse("ok", content_type="text/html")
                else:
                    return http.HttpResponseRedirect("/private_office/")
            else:
                errors = {}
                errors["username"] = reg_form.errors.get("username")
                errors["password1"] = reg_form.errors.get("password1")
                errors["password2"] = reg_form.errors.get("password2")
                args["errors"] = errors
                json_errors = json.dumps(errors)
                if request.is_ajax():
                    return http.HttpResponse(json_errors, content_type="application/json")
                else:
                    return render_to_response("Registration.html", args)
    else:
        args["reg_form"] = forms.UserCreationForm()
    return render_to_response("Registration.html", args)


def private_office(request):
    args = navigation()
    args.update(contact_info())
    args.update(user_info(request))
    args.update(csrf(request))
    if request.user.is_authenticated():
        orders = request.user.orders.all()
        records = request.user.records.all()
        args["orders"] = orders
        args["records"] = records
    else:
        return http.HttpResponseRedirect("/")

    return render_to_response("Private-office.html", args)
