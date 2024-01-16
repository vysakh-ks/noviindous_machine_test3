from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    node = Bynary_tree.objects.all()
    context = {'node':node}
    return render(request,'index.html',context)

def add_node(request):
    if request.method =='POST':
        parent = request.POST['parent']
        name= request.POST['name']
        position = request.POST['position']

        if Bynary_tree.objects.filter(parent=parent, node=position).exists():
            return HttpResponse("Already a node in this position try another position")
        else:

            node = Bynary_tree.objects.create(parent=parent,name=name,node=position)
            node.save()
            return HttpResponse("Node added successfully")

    else:
        return HttpResponse("Invalid request")
    
def search_parent(name,position):

    node = Bynary_tree.objects.filter(parent = name, node=position).first()
    try:
        Bynary_tree.objects.filter(parent=node.name,node=position).exists()
        search_parent(node.name,position)
    except Bynary_tree.DoesNotExist:
        return node




def search_node(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        try:
            result_node = Bynary_tree.objects.filter(parent = name, node=position).first()
            print(result_node.name)
        except:
            return HttpResponse("Invalid input")
        
        try:    
            Bynary_tree.objects.filter(parent=result_node.name,node=position).exists()

            result_node = search_parent(result_node.name,position)
        except Bynary_tree.DoesNotExist:
            pass

        context = {'node':result_node}
        return render(request,'view_node.html',context)
        
    else:
        return HttpResponse('Invalid input')
    



    
    







