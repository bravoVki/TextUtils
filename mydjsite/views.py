#i have created this views.py file

from string import punctuation
from django.http import HttpResponse #to return http response
from django.shortcuts import render

#code to develop website to learn templates
def index(request):
    return render (request,'index.html')    #this function renders home page 

def analyze(request):             #analyzer function that contains all tasks
    # get the text
    djtext=(request.POST.get("text","default"))   #BY DEFAULT FORM METHOD IS GET BUT WE USE POST 
    #SO THAT OUR URL WILL BE SHOWN IN COMPACT MANNER RAHTER THAN ALL TEXTS

    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newLineRemover=request.POST.get('newLineRemover','off')
    extraSpaceRemover=request.POST.get('extraSpaceRemover','off')
    charCounter=request.POST.get('charCounter','off')

    punctuation='''@!#$%^&*(){}"';:?></.,`~'''
    if removepunc =="on":
            analyzed=''
        
            for char in djtext:
                if char not in punctuation:
                    analyzed=analyzed+char
            params={'purpose':'removed punctuations','analyzed_text':analyzed}
            djtext=analyzed

    if capitalize=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'capitalize','analyzed_text':analyzed}
        djtext=analyzed

    if (newLineRemover=='on'):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":   #char!="\r" checks the carriage return  
                analyzed=analyzed+char
        params={'purpose':'newLineRemove','analyzed_text':analyzed}
        djtext=analyzed

    if extraSpaceRemover=='on':
        analyzed=''
        for i,char in enumerate(djtext):
            if not (djtext[i]==" " and djtext[i+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'extraSpaceRemove','analyzed_text':analyzed}
        djtext=analyzed

    if charCounter=='on':
        count=0
        for index,char in enumerate(djtext):
            count =count+1

        result='The total char in sentence is '+ str(count)

        params={"purpose":"charCount","analyzed_text":result,'text':djtext}
        
    if (charCounter !='on' and extraSpaceRemover !='on' and newLineRemover !='on' and capitalize !='on' and removepunc !="on"):
        return HttpResponse("Error 404 not found")

    return render(request,'text.html',params)
   