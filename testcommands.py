from news.models import *


User.objects.create_user(username='Vitya', password='001')
User.objects.create_user(username='Kolya', password='002')


Author.objects.create(authorUser=user_1)
Author.objects.create(authorUser=user_2)


Category.objects.create(name='category 1')
Category.objects.create(name='category 2')
Category.objects.create(name='category 3')
Category.objects.create(name='category 4')


Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Vitya')), categoryType='AR', title='title1AR', text='text1')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Vitya')), categoryType='AR', title='title2AR', text='text2')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Kolya')), categoryType='NW', title='title3NW', text='text3')

p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(title='title2AR')
p3 = Post.objects.get(categoryType='NW')

c1 = Category.objects.get(name='category 1')
c2 = Category.objects.get(name='category 2')
c3 = Category.objects.get(name='category 3')
c4 = Category.objects.get(name='category 4')

p1.postCategory.add(c1)
p2.postCategory.add(c1, c2)
p3.postCategory.add(c1, c3, c4)

Comment.objects.create(commentUser=User.objects.get(username='Vitya'), commentPost=Post.objects.get(pk=1), text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='Vitya'), commentPost=Post.objects.get(pk=2), text='comment text2')
Comment.objects.create(commentUser=User.objects.get(username='Kolya'), commentPost=Post.objects.get(pk=3), text='comment text3')
Comment.objects.create(commentUser=User.objects.get(username='Kolya'), commentPost=Post.objects.get(pk=1), text='comment text3_1')

Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=1).dislike()
Post.objects.get(pk=2).dislike()

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).dislike()

Author.objects.get(authorUser=User.objects.get(username='Vitya')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Kolya')).update_rating()

a = Author.objects.get(authorUser=User.objects.get(username='Kolya'))
a.ratingAuthor
b = Author.objects.get(authorUser=User.objects.get(username='Vitya'))
b.ratingAuthor

bestAuthor = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]

print(bestAuthor)




#Вывести дату добавления,  автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
Post.objects.all().order_by('-rating').values('dateCreation',  'author', 'rating', 'title',)[0]
Post.objects.get(pk=1).preview()

#Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(commentPost=1).values('dateCreation', 'commentUser', 'rating', 'text')






