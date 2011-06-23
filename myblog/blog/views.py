from django.template import Context, loader
from django.http import HttpResponse
from django.forms import ModelForm  					#LAB06
from models import Blog, Comment
from django.views.decorators.csrf import csrf_exempt 			#LAB06

# For templates lab
from django.shortcuts import *
 

def blog_list(request):
    blog_list = Blog.objects.all()
    for blog in blog_list:
    	print blog.id, blog.title
    t = loader.get_template('blog/list.html')
    c = Context({'blog_list':blog_list})
    return HttpResponse(t.render(c))
#    return HttpResponse('going to give a list')

class CommentForm(ModelForm):						#LAB06
    class Meta:
        model = Comment
        exclude=['post', 'author']

@csrf_exempt
def blog_detail(request, id, showComments=False):
    blog = Blog.objects.get(pk=id)
    print blog.id, blog.title, blog.body
    if showComments:
        comments = Comment.objects.filter(post__pk=id)
        print comments

    if request.method == 'POST':					#LAB06
        comment = Comment(post=blog, author=request.user.username)
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
    	form = CommentForm()						#END LAB06
    t = loader.get_template('blog/detail.html')
    c = Context({'blog':blog, 'comments':comments, 'form':form.as_p(), 'request':request})	#LAB06
    return HttpResponse(t.render(c))
    #return HttpResponse('gets the specific details page')

@csrf_exempt
def comment_edit(request,id):
    comment = Comment.objects.get(pk=id)
    if not request.user.username == comment.author:
	return HttpResponse('no permissions to do this')
    if request.method == 'POST':					
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/detail/'+str(comment.post.id)+'/True')
    else:
    	form = CommentForm(instance=comment)	
    t = loader.get_template('blog/editcomment.html')
    c = Context({'form':form.as_p()})
    return HttpResponse(t.render(c))


def blog_search(request, term):
    blog_list = Blog.objects.filter(title__icontains=term)
    for blog in blog_list:
        print blog.id, blog.title
    t = loader.get_template('blog/search.html')
    c = Context({'blog_list':blog_list, 'term':term})
    return HttpResponse(t.render(c))
    #return HttpResponse('done searching')

def home(request):
    print 'we are working'
    t = loader.get_template('blog/base.html')
    c = Context(dict())
    return HttpResponse(t.render(c))
    #return HttpResponse('hello worldoo')

