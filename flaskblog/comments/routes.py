from flaskblog.models import Post, User, Comment
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.comments.forms import CommentForm

comments = Blueprint('comments', __name__)


@comments.route('/comments/<id>')
@login_required
def comment(id):
    comments =Comment.get_comments(id)
    print(comment)
    title = 'comments'
    return render_template('comments.html',comments = comments,title = title)

@comments.route('/comment/<int:posts_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(posts_id):
    posts = Post.query.filter_by(id = posts_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment_content=comment,user_id=current_user.id, posts_id=posts_id)

        new_comment.save_comment()

        return redirect(url_for('comments.index'))
    title='New Comment'
    return render_template('new_comment.html',title=title,comment_form = form,posts_id=posts_id)

@comments.route('/post_comments/<int:posts_id>' ,methods=['GET', 'POST'])
@login_required

def posts_comments(post_id):

    post = Post.query.filter_by(id=post_id).one()
    # comments=Comment.get_comments(post_id)
    comments=Comment.get_comments(post_id)


    return render_template('post_comments.html', post=post, comments=comments, post_id=post.id)

