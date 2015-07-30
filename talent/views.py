from django.shortcuts import render
# import dlya responsa
from django.http.response import HttpResponse, Http404
# otvechaet za poluchenie shablona
from django.template.loader import get_template
# otvechaet za hranenie teh peremennih, kotorie budut otpravleni v shablon
from django.template import Context
# shtob' ispolzovat render_to_response
from django.shortcuts import render_to_response, redirect
# importiruem modeli dlya zaprosov k BD
from talent.models import Talent
from comments.models import Comments
from news.models import News
# dlya oshibki zapros k objectu BD
from django.core.exceptions import ObjectDoesNotExist
# import dlya formi
from comments.forms import CommentForm
from talent.forms import TalentForm
# dlya zaschiti ot csrf atak
from django.core.context_processors import csrf
from django.contrib import auth
# dlya paginatsii
from django.core.paginator import Paginator





# Create your views here.
# funktsiya kogda vizov basic_one
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


# funktsiya kogda vizov template_two
def template_two(request):
    view = "template_two"
    # v t kladem nash shablon
    t = get_template('myview.html')
    # smotrim shto u nas hranitsya v name, i vstavlyaem v html
    html = t.render(Context({'name': view}))
    # otpravim v brauzer
    return HttpResponse(html)


def template_three_simple(request):
    view = "template_three"
    # uproschenniy sposob dlya template_two
    return render_to_response('myview.html', {'name': view})


# vivodit vse statyi
def talents(request, page_number=1):
    all_talents = Talent.objects.all()
    current_page = Paginator(all_talents, 2)
    talent_form = TalentForm
    args = {}
    args.update(csrf(request))
    args['form_talent'] = talent_form
    args['talents'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    # beret is Talent vse danniye
    return render_to_response('talents.html', args)


# dlya vivoda odnoy statti
def talent(request, talent_id=1, page_number=1):
    # dobavim vozmozhnost' poluchit' kommenti
    comment_form = CommentForm
    # sozdaem pustoj slovar', v kotorij zapishem parametri, peredavaemie shablonu
    args = {}
    # zaschita ot csrf atak
    args.update(csrf(request))
    all_comments = Comments.objects.filter(comments_talent_id=talent_id)
    current_page = Paginator(all_comments, 2)
    args['talent'] = Talent.objects.get(id=talent_id)
    args['comments'] = current_page.page(page_number)
    # peredaem formu
    args['form_comment'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('talent.html', args)


def talent_news(request):
    # v t kladem nash shablon
    t = get_template('talents.html')
    # smotrim shto u nas hranitsya v name, i vstavlyaem v html
    html_talent = t.render(Context({'talents': Talent.objects.all()}))
    # v r kladem nash shablon
    r = get_template('news.html')
    # smotrim shto u nas hranitsya v name, i vstavlyaem v html
    html_news = r.render(Context({'news': News.objects.all()}))
    # otpravim v brauzer
    return HttpResponse(html_news + html_talent)


def addlike(request, talent_id):
    bacl_url = request.META.get('HTTP_REFERER')
    try:
        if talent_id in request.COOKIES:
            redirect(bacl_url)
        else:
            # dostaem talant is BD
            talent = Talent.objects.get(id=talent_id)
            # like ++
            talent.talent_likes += 1
            # sohranyaem
            talent.save()
            # sozdaem i vozvraschaem cookie
            response = redirect(bacl_url)
            response.set_cookie(talent_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(bacl_url)


def addcomment(request, talent_id):
    if request.POST and ("pause" not in request.session):
        # sozdaem formu-->raznosim v nee dannie is post zaprosa
        form = CommentForm(request.POST)
        # esli forma validna
        if form.is_valid():
            # zapret auti sohraneniya formi
            comment = form.save(commit=False)
            # nahodim, k kakomu talantu sohranit'
            comment.comments_talent = Talent.objects.get(id=talent_id)
            comment.comments_from = request.user
            form.save()
        # request.session.set_expiry(60)
        # request.session['pause'] = True
    return redirect('/talents/get/%s/' % talent_id)


def addtalent(request):
    if request.POST and ("pause" not in request.session):
        # sozdaem formu-->raznosim v nee dannie is post zaprosa
        form = TalentForm(request.POST)
        # esli forma validna
        if form.is_valid():
            # zapret auti sohraneniya formi
            talent = form.save(commit=False)
            # nahodim, k kakomu talantu sohranit'
            talent.taleny_from = request.user
            form.save()
        # request.session.set_expiry(60)
        # request.session['pause'] = True
    return redirect('/talents/')



