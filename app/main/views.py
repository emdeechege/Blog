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
    blogs = Blogs.query.order_by(Blogs.date.desc()).all()


    title= "Emdee's Blog"
    return render_template('index.html',title=title, blogs=blogs)

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

        return redirect(url_for('main.single_blog',id=blogpost.id))

    return render_template('blog.html',blogpost_form= form)

#ability to view single blog addition
@main.route('/blog/<int:id>')
def single_blog(id):

    blogpost = Blogs.query.get(id)

    return render_template('oneblogpost.html',blogpost=blogpost)

@main.route('/blogposts')
def blogpost_list():
    # Function that renders all blogposts and its content

    blogposts = Blogs.query.all()


    return render_template('blogposts.html', blogposts=blogposts)


# viewing comments and respective posts
@main.route('/blog/new/<int:blogs_id>/',methods=["GET","POST"])
@login_required
def blogpost(blogs_id):
    blogpost = Blogs.query.filter_by(id=blogs_id).first()
    form = CommentForm()
    if form.validate_on_submit():

        comment = form.comment.data
        new_blogpost_comment = Comments(comment=comment,blogs_id=blogs_id,user_id=current_user.id)

        db.session.add(new_blogpost_comment)
        db.session.commit()

    comments = Comments.get_comment(blogs_id)

    return render_template('blogcommentlink.html',blogpost=blogpost,blogpost_form=form,comments=comments)



@main.route('/blog/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blog(id):
    """
    Delete a blogpost from the database
    """
    if not current_user.is_admin:
        abort(403)

    blogpost = Blogs.query.filter_by(id=id).first()
    
    db.session.delete(blogpost)
    db.session.commit()


    # redirect to the departments page
    # return redirect(url_for('main.admin_dashboard'))

    return render_template('main.index', title="Dashboard")
