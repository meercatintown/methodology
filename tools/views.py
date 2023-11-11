from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from base.models import *

# Create your views here.

def tools(request):
    tools = Tool.objects.all()
    topics = ToolTopic.objects.all()
    step = Step.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        related_step = request.POST.get('related_step')
        topic_name = request.POST.get('topic')
        description = request.POST.get('description')

        if Step.objects.filter(step_number=related_step).exists():
            step = Step.objects.get(step_number=related_step)

        if ToolTopic.objects.filter(title=topic_name).exists():
            topic = ToolTopic.objects.get(title=topic_name)
        else:
            topic = ToolTopic.objects.create(title=topic_name)
        if title:
            tool = Tool.objects.create(title=title, topic=topic, step=step, description=description)
            
            return redirect('tools')
    context = {'tools':tools}
    return render(request, 'tools/tools.html', context)


def tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    context = {'tool':tool}
    return render(request, 'tools/tool.html', context)

def add_tool(request):
    tool = Tool.objects.all()
    steps = Step.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        related_step = request.POST.get('related_step')
        description = request.POST.get('description')

        if Step.objects.filter(step_number=related_step).exists():
            step = Step.objects.get(step_number=related_step)

        tool = Tool.objects.create(title=title, topic=topic, step=step, description=description)
        return redirect('tools/tools.html')
    
    context = {'tool':tool, 'steps':steps}
    return render(request, 'tools/add_tool.html', context)

def edit_tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    step = Step.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        related_step = request.POST.get('related_step')
        description = request.POST.get('description')

        if Step.objects.filter(step_number=related_step).exists():
            step = Step.objects.get(step_number=related_step)

        if title:
            tool.title = title
            tool.description = description
            tool.save()

        return redirect('tools')
    return render(request, 'tools/edit_tool.html', {'tool':tool})

def delete_tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)

    if request.method == 'POST':
        tool.delete()
        return redirect('/tools')
    
    return render(request, 'tools/delete_tool.html', {'tool':tool})