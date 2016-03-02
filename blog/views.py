from django.shortcuts import render
from django.http import HttpResponse


def list_posts(request):
    text = '''
    <strong>화면 떴다</strong>

    <p>이상한 html 문서 구조이지만. 됨</p>
    '''
    return HttpResponse(text)

