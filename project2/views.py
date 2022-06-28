from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    # Check the checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcapitalize = request.POST.get('fullcapitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which chechbox is on
    purpose=""
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed
        purpose+='Remove Punctuations'

    if fullcapitalize=='on':
        analyzed = djtext.upper()
        djtext=analyzed
        purpose+=' | Full Capitalized'
        
    if newlineremove=='on':
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        djtext=analyzed
        purpose+=' | New Line Removed'
        
    if extraspaceremove=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==' ' and djtext[index+1] ==' '):
                analyzed=analyzed+char
        djtext = analyzed
        purpose+=' | Extra Space Removed'
        
    if charcount=='on':
        analyzed = 0
        for char in djtext:
            analyzed +=1
        djtext += f"\nNumber of characters are: {analyzed}"
        purpose+=' | Number of characters'
        
    params = {'pose':  purpose, 'analyzed_text': djtext}

    if charcount=='on' or extraspaceremove=='on' or newlineremove=='on' or fullcapitalize=='on' or removepunc=='on':
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')
