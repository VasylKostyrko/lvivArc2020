from django.shortcuts import render
from .models import ArcType
from .models import ArcObj
from django.shortcuts import get_object_or_404


def index(request):
    typelist = ArcType.objects.all()
    context = {
        'typelist': typelist,
    }
    template = 'index.html'
    return render(request, template, context)


# from django.shortcuts import render

# def index(request):
#     typelist = ["Церкви та монастирі", "Оборонні споруди", "Цивільна архітектура"]
#     context = {"typelist": typelist}
#     return render(request, 'index.html', context)

# def arcobj(request):
#     type = {"typeName": "Церкви та монастирі"}
#     obj = {
#         "descr": """
#         Церква Святого Миколая — памʼятка архітектури національного значення, один із найдавніших храмів Львова.
#         Знаходиться під горою Будельницею на вул. Богдана Хмельницького, 28 г (колишній Волинський тракт).
#         Храм збудований імовірно між 1264 і 1340 роками. Пам'ятка не зберегла свого первозданного вигляду.
#         Від первісної церкви залишилися тільки фрагменти стін. Її змінили ґрунтовні перебудови після пожеж 1623 та 1800 рр.,
#         коли згоріли криті ґонтом дахи, купол і вежа-дзвіниця над бабинцем. Церква являє собою своєрідну хрещату
#         в плані споруду з квадратною навою, навколо якої групуються об'єми вівтаря з півкруглою апсидою,
#         прямокутного бабинця і бічних каплиць, також з півкруглими апсидами. Нава і вівтарна частина завершені типовими
#         для української архітектури банями з ліхтарями. Обʼємно-планувальна композиція Миколаївської церкви зближує її
#         з храмами Київської Русі, а також має аналоги в архітектурі південних словʼян.
#         Від будівлі XIII ст. залишилися план, нижня частина камʼяних стін і відкриті з-під тиньку апсиди,
#         вимурувані з тесаних блоків білого вапняку.
#         """,
#         "objName": "Церква святого Миколая",
#         "image": "Church of St.Nicholas.png",
#         "curAddress": "вул. Богдана Хмельницького, 28А.",
#     }
#
#     context = {
#         'type': type,
#         'obj': obj,
#     }
#     template = 'arcobj.html'
#     return render(request, template, context)


def arcobj(request, obj_id):
    obj = get_object_or_404(ArcObj, id=obj_id)
# def arcobj(request):
#     obj = get_object_or_404(ArcObj, id=1)

    objType = obj.objType
    context = {
        'type': objType,
        'obj': obj,
    }
    template = 'arcobj.html'
    return render(request, template, context)

def listobj(request, type_id):
    type = get_object_or_404(ArcType, id=type_id)
    list = type.arcobj_set.all()
    context = {
        'type': type,
        'list': list,
    }
    template = 'listobj.html'
    return render(request, template, context)