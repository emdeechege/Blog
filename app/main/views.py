from flask import render_template
from flask import render_template,request,redirect,url_for,abort, flash
from flask_login import login_required,current_user
from ..models import *
from . import main
from .. import db,photos
from .forms import *

@main.route('/')
def index():
    '''
    my index page
    return
    '''


    title= "Emdee's Blog"
    return render_template('index.html',title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

# add admin dashboard view
@main.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('admin_dashboard.html', title="Dashboard")

@main.route('/blog/', methods = ['GET','POST'])
@login_required
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():

        topic = form.topic.data
        content= form.content.data
        title=form.title.data

        # Updated bloginstance
        blogpost = Blogs(title=title,topic= topic,content= content,user_id=current_user.id)
        db.session.add(blogpost)
        db.session.commit()

        title='New Blog'

        # new_blog.save_blog()
        print('meeee')

        return redirect(url_for('main.single_blog',id=blogpost.id))

    return render_template('blog.html',blogpost_form= form)

#ability to view single blog posts
@main.route('/blog/<int:id>')
def single_blog(id):

    blogpost = Blogs.query.get(id)

    return render_template('oneblogpost.html',blogpost=blogpost)

@main.route('/allblogposts')
def blogpost_list():
    # Function that renders the business category blogpost and its content

    blogposts = Blogpost.query.all()

    return render_template('blogposts.html', blogposts=blogposts)


# VIEWING A blogpost WITH COMMENTS AND COMMENTFORM
@main.route('/blog/<int:id>/',methods=["GET","POST"])
def blogpost(id):
    blogpost = Blogs.query.get(id)
    form = CommentForm()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_blogpost_comment = Comments(comment=comment,blogs=blogs_id,user=current_user.id)
        # new_post_comment.save_post_comments()
        db.session.add(new_blogpost_comment)
        db.session.commit()
    comments = Comment.query.all()
    return render_template('blogview.html',title=blogpost.title,blogpost=blogpost,blogpost_form=form,comments=comments)

# ADDING A NEW COMMENT TO A blogpost
@main.route('/blog/comment/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    view category that returns a form to create a new comment
    '''
    form = CommentForm()
    blogpost = Blogs.query.filter_by(id = id).first()

    if form.validate_on_submit():

        comment = form.comment.data

        # comment instance
        new_comment = Comment(blogpost_id = blogpost.id, post_comment = comment,user = current_user.id)

        # save comment
        new_comment.save_comment()

        return redirect(url_for('.blog', id = blogpost.id ))

    title = f'{blogpost.title} comment'
    return render_template('newcomment.html', title = title, comment_form = form, blogpost = blogpost, )
