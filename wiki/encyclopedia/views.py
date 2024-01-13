from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import random, re

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, entry):
    if util.get_entry(entry) is None:
        return render(request, "encyclopedia/error.html")
    else:
        markdown = util.get_entry(entry)
        #convert headers

        markdown = re.sub(r'# (.*?)\n', r'<h1>\1</h1>\n', markdown)
        
        #convertlists

        markdown = re.sub(r'\n\*(.*)' , r'\n<li>\1</li>', markdown)

        #convert bold text

        markdown = re.sub(r'\*\*(\S.*?\S)\*\*', r'<strong>\1</strong>', markdown)

        #convert italic text

        markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)

        #convert links

        markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)


        html = markdown

        html_content = "<html><body>" + html + "</body></html>"


        return render (request, "encyclopedia/page.html", {
            "title_content": html_content,
            'title': entry
        })
    

def search(request):
    entry_list = util.list_entries()
    search_list = []
    if request.method == "POST":
        q = request.POST['q']
        for i in entry_list:
            if q.lower() == i.lower():
                return redirect('encyclopedia:page', entry=i)
        else:
            for i in entry_list:
                if q.lower() in i.lower():
                    search_list.append(i)
            return render(request, "encyclopedia/search.html", {
                "search_list":search_list
            })

def newpage(request):
    
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if title or content is not None:
            if title in util.list_entries():
                return render(request, "encyclopedia/error.html")
            
        util.save_entry(title,content)
        

    return render(request, 'encyclopedia/newpage.html')

def edit(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title,content)
        return HttpResponseRedirect(reverse("encyclopedia:page", args=[title]))
    else:
        return render(request, 'encyclopedia/edit.html', {
            'Content':util.get_entry(title),
            'title':title
        })

def random_entry(request):
    random_entry = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("encyclopedia:page", args=[random_entry]))