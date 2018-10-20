from django.shortcuts import render, redirect, HttpResponse
from app01 import models

# Create your views here.


# 出版社列表
def publisher_list(request):
    res = models.Publisher.objects.all()
    return render(request, "publisher_list.html", {"publisher_list": res})


# 添加出版社
def add_publisher(request):
    err_msg = ""
    if request.method == "POST":
        new_name = request.POST.get("publisher", None)
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect("/publisher_list")
        else:
            err_msg = "出版社名不能为空！"
    return render(request, "add_publisher.html", {"err_msg": err_msg})


# 删除出版社
def delete_publisher(request):
    print(request.GET)
    # request.GET 获得的是一个字典。<QueryDict: {'id': ['8']}>
    # 字典的两种访问方式，   d["id"]若id不存在则报错       d.get("id", None)若id不存在则为None,None可以指定为其他内容。
    del_id = request.GET.get("id", None)    # 字典取值，取不到默认为None
    if del_id:
        # 删除记录的两种方式
        # models.Publisher.objects.get(id=del_id).delete()
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的数据不存在!")


# 编辑出版社
def edit_publisher(request):
    if request.method == "POST":
        edit_id = request.POST.get("id", None)
        new_publisher_name = request.POST.get("new_publisher_name", None)
        edit_obj = models.Publisher.objects.get(id=edit_id)
        edit_obj.name = new_publisher_name
        edit_obj.save()
        return redirect("/publisher_list")
    edit_id = request.GET.get("id", None)
    if edit_id:
        edit_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"publisher": edit_obj})
    else:
        return HttpResponse("编辑的出版社不存在！")


# 书籍列表
def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {"all_book": all_book})


# 添加书籍
def add_book(request):
    if request.method == "POST":
        new_book_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher_id")
        models.Book.objects.create(
            title=new_book_title,
            publisher_id=new_publisher_id)
        return redirect("/book_list/")
    all_publisher = models.Publisher.objects.all()
    return render(request, "add_book.html", {"all_publisher": all_publisher})


# 删除书籍
def delete_book(request):
    delete_id = request.GET.get("id")
    models.Book.objects.get(id=delete_id).delete()
    return redirect("/book_list/")


# 编辑书籍
def edit_book(request):
    if request.method == "POST":
        edit_id = request.POST.get("edit_id")
        edit_obj = models.Book.objects.get(id=edit_id)
        new_book_title = request.POST.get("new_book_title")
        new_publisher_id = request.POST.get("new_publisher_id")
        edit_obj.title = new_book_title
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return redirect("/book_list/")
    edit_id = request.GET.get("id")
    edit_obj = models.Book.objects.get(id=edit_id)
    all_publisher = models.Publisher.objects.all()
    return render(request, "edit_book.html",
                  {"edit_book": edit_obj, "all_publisher": all_publisher})


# 作者列表
def author_list(request):
    all_author = models.Author.objects.all()
    return render(request, "author_list.html", {"author_list": all_author, })


# 添加作者
def add_author(request):
    if request.method == "POST":
        new_author = request.POST.get("author_name")
        # post提交的数据是多个值的时候一定会要用getlist, 如多选的checkbox和多选的select
        books = request.POST.getlist("books_id")
        # 创建新作者
        author_obj = models.Author.objects.create(name=new_author)
        # 把新作者和书籍建立对应关系
        author_obj.book.set(books)
        return redirect("/author_list/")
    all_book = models.Book.objects.all()
    return render(request, "add_author.html", {"book_list": all_book})


# 删除作者
def delete_author(request):
    del_author_id = request.GET.get("id")
    models.Author.objects.get(id=del_author_id).delete()
    return redirect("/author_list/")


# 编辑作者
def edit_author(request):
    if request.method == "POST":
        edit_author_id = request.POST.get("author_id")
        new_author_name = request.POST.get("author_name")
        new_books = request.POST.getlist("books_id")
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books)
        edit_author_obj.save()
        return redirect("/author_list/")
    edit_author_id = request.GET.get("id")
    edit_author_obj = models.Author.objects.get(id=edit_author_id)
    all_book = models.Book.objects.all()
    return render(request, "edit_author.html", {"edit_author": edit_author_obj, "book_list": all_book})
    pass
