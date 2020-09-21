"""remove category column

Revision ID: 8d348474ba67
Revises: ee8cdfa865f9
Create Date: 2019-06-30 21:46:04.511610

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8d348474ba67'
down_revision = 'ee8cdfa865f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_content', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    op.drop_constraint('comments_post_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'post', ['pitch_id'], ['id'])
    op.drop_column('comments', 'body')
    op.drop_column('comments', 'published_at')
    op.drop_column('comments', 'post_id')
    op.add_column('post', sa.Column('content', sa.Text(), nullable=False))
    op.add_column('post', sa.Column('date_posted', sa.DateTime(), nullable=False))
    op.add_column('post', sa.Column('likes', sa.Integer(), nullable=True))
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('post', 'author')
    op.drop_column('post', 'upvote')
    op.drop_column('post', 'post_content')
    op.drop_column('post', 'published_at')
    op.drop_column('post', 'downvote')
    op.add_column('user', sa.Column('image_file', sa.String(length=20), nullable=False))
    op.add_column('user', sa.Column('password', sa.String(length=60), nullable=False))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.create_unique_constraint(None, 'user', ['email'])
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'profile_pic_path')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_column('user', 'password')
    op.drop_column('user', 'image_file')
    op.add_column('post', sa.Column('downvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('published_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('post_content', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('author', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_column('post', 'likes')
    op.drop_column('post', 'date_posted')
    op.drop_column('post', 'content')
    op.add_column('comments', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('published_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('body', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_post_id_fkey', 'comments', 'post', ['post_id'], ['id'])
    op.drop_column('comments', 'posted')
    op.drop_column('comments', 'pitch_id')
    op.drop_column('comments', 'comment_content')
    # ### end Alembic commands ###
