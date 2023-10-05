from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def about(request):
    return HttpResponse("about krishna runwal")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc' , 'off')
    Capatalize = request.POST.get('Capatalize','off')
    newline = request.POST.get('newline','off')
    spaceremove = request.POST.get('spaceremove','off')
    countcharecters = request.POST.get('countcharecters','off')
    if removepunc == "on":
        punctuations = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char 
        params = {'purpose':'Removing Punctuations' , 'analyzed_text': analyzed}
        djtext = analyzed
        
    if(Capatalize == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Capatalizing the strings' , 'analyzed_text': analyzed}
        #Analize the text
        djtext = analyzed

    if(newline == "on"):
        analyzed = ""
        for char in djtext:
            if (char!="\n" and char!="\r"):

                analyzed = analyzed + char 
        params = {'purpose':'Removing the newlines from the strings' , 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(spaceremove == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " or djtext[index+1] == " " or djtext[index+2] == " "):
                analyzed = analyzed + char
        
        params = {'purpose':'Space is removed from the strings' , 'analyzed_text': analyzed}
        djtext = analyzed
        
    if(countcharecters == "on"):
        count = 0
        for c in djtext:
            count = count + 1
        params = {'purpose' : 'Coutning the characters of the strings' , 'analyzed_text': count }
        
    if(removepunc !="on" and spaceremove !="on" and countcharecters !="on" and newline !="on" and Capatalize !="on"):
        return HttpResponse("Please Click that checkboxes to perform the actions ..!")   
    
    return render(request , 'analyze.html', params)

    
   

























