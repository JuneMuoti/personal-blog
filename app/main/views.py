from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,login_user,logout_user,current_user
from ..models import Posts,Comments
from .forms import PostForm,CommentForm


@main.route('/')
def index():
    title = 'Home'

    posts = Posts.get_posts()
    comments=Comments.get_comments()


    return render_template('index.html' ,title=title, posts=posts,comments=comments)

@main.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form= PostForm()
    if form.validate_on_submit():
        body=form.body.data

        post = Posts(body=form.body.data,author=current_user._get_current_object())

        new_post=Posts(body=body,)
        new_post.save_post()
        return redirect(url_for('.index'))


    title= 'Posts'
    return render_template('new_post.html',posts_form=form)

@main.route('/comment/new/', methods=['GET','POST'])
@login_required
def new_comment():

    '''
    View new commet route function that returns a page with a form to create a blogs post
    '''
    comments = Comments.query.all()
    form =CommentForm()
    if form.validate_on_submit():
        name=form.name.data
        new_comment=Comments(name=name)
        new_comment.save_comment()

        return redirect(url_for('.index'))

    title = "New Comment"
    return render_template('new_comment.html', title=title, form=form,comments=comments)
