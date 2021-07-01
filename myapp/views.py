from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Topic, Course, Student, Order

# Create your views here.
def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    # response = HttpResponse()
    # heading1 = '<b><p>' + 'List of topics: ' + '</p></b>'
    # response.write(heading1)
    # for topic in top_list:
    #     para = '<p>'+ str(topic.id) + ': ' + str(topic) + '</p>'
    #     response.write(para)
    #
    # course_list = Course.objects.all().order_by('-title')[:5]
    #
    # response.write('<b><p>' + 'List of Courses: ' + '</p></b>')
    # for course in course_list:
    #     para = '<p>'+  str(course.title) + '  ' + str(course.price)+' </p>'
    #     response.write(para)
    #
    # return response
    return render(request, 'myapp/index0.html', {'top_list': top_list})

def about(request):
    # return HttpResponse('This is an E-learning Website! Search our Topics to find all available Courses.')
    return render(request, 'myapp/about0.html')

def details(request, topic_id):
    # response = HttpResponse()
    topic = get_object_or_404(Topic, id=topic_id)


        # response.write('<p>Topic : '+topic.name.upper()+'</p>')
        # response.write('<p>Length : '+ str(topic.length)+'</p>')
        # response.write('<b><p>' + 'List of Courses: ' + '</p></b>')
    courses = Course.objects.filter(topic=topic.id)

        # for course in courses:
        #     para = '<p>' + str(course.id) + '  ' + str(course.title) + ' </p>'
        #     response.write(para)


    return render(request, 'myapp/detail0.html', {'topic':topic, 'courses':courses} )

    # return response

