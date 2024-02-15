#!/usr/bin/env python3

from lib import Article, Author, Magazine
           
author1 = Author("Julius")
author2 = Author("Mary")
author3 = Author("CS Student")

magazine1 =  Magazine("Python", "Coding")
magazine2 =  Magazine("Ruby", "Coding")
magazine3 =  Magazine("Investing", "Finance")
magazine4 =  Magazine("Genesis", "Bible")

article1 = Article(author3, magazine1, "Introduction to python")
article2 = Article(author3, magazine2, "Introduction to Ruby")
article3 = Article(author3, magazine2, "Active Records")
article4 = Article(author2, magazine1, "Django ORM")
article5 = Article(author2, magazine3, "Investment Banking")
article6 = Article(author2, magazine3, "Money market")
article7 = Article(author1, magazine4, "The creation story")
article8 = Article(author1, magazine4, "The Fall")

all_articles = [article1, article2, article3, 
                article4, article5, article6, article7, article8]

class TestAuthor:
    '''Author exists'''
    
    def test_has_name_attribute(self):
        '''Author instance should have name attribute'''
        assert(hasattr(author1, "name"))
    
    def test_value_of_name_should_not_change(self):
        '''Value of name attribute of the Author instance should not be changed'''
        try:
            author1.name = "Another name"
        except AttributeError:
            pass
        
        assert(author1.name == "Julius")
        
    def test_author_has_articles_attributes_and_returns_all_author_articles(self):
        '''author has articles attributes and returns all author articles'''
        assert(hasattr(author3, "articles") and author3.articles == [article1, article2, article3])
    
    def test_author_has_magazines_attributes_and_returns_all_author_magazines(self):
        '''author has magazines attributes and returns all author magazines'''
        assert(hasattr(author2, "magazines") and author2.magazines == [magazine1, magazine3])
        
    def test_author_can_add_article(self):
        global all_articles
        '''author instance can add article'''
        assert(callable(author3.add_article))
        author3.add_article(magazine4, "ML")
        all_articles.append(author3.articles[-1])
        assert(author3.magazines == [magazine1, magazine2, magazine4])
        
    def test_author_has_topic_areas_and_returns_magazines_categories(self):
        '''author instance contains topic_areas and returns magazine categories'''
        assert(callable(author2.topic_areas) and author2.topic_areas() == ["Coding", "Finance"])

class TestMagazine:
    def test_magazine_has_name_category_attributes(self):
        '''Magazine instance should have name and category attributes'''
        assert(hasattr(magazine1, "name") and hasattr(magazine1, "category"))
        
    def test_name_category_can_be_changed(self):
        '''name and category value of the Magazine instance can be changed'''
        magazine1.name = "Something else"
        magazine1.category = "Another category"
        assert(magazine1.name == "Something else" and magazine1.category == "Another category")
        
    def test_all_class_method(self):
        '''Magazine should have all class method'''
        assert(hasattr(Magazine, "all") and callable(Magazine, all))
        
    def test_all_class_method(self):
        '''Magazine.all has all the magazines'''
        assert(len(Magazine.all()) > 0 and [magazine1, magazine2, magazine3, magazine4] == Magazine.all())
        
    def test_magazine_has_contributors_and_returns_authors(self):
        '''magazine instance has contributos and returns authors'''
        assert(hasattr(magazine3, "contributors") and \
            callable(magazine3.contributors) and \
            magazine3.contributors() == [author2, author2])
        
    def test_magazines_can_be_found_by_name(self):
        '''magazine can be found by name'''
        assert(callable(Magazine.find_by_name) and magazine4 in Magazine.find_by_name("Genesis"))
        
    def test_magazine_can_return_article_titles(self):
        '''magazine can return article titles'''
        assert(callable(Magazine.article_titles) and \
            magazine4.article_titles() == [article7.title, article8.title, "ML"])
        
    def test_get_contributing_autors_of_magazine(self):
        '''You can get contributing author of magazine'''
        assert(callable(Magazine.contributing_authors) and \
            magazine2.contributing_authors() == [author3])
        
        
class TestArticle:
    '''Article exists'''
    def test_article_instance_has_author_magazine_title_attributes(self):
        '''Article should have author magazine and title attributes'''
        assert(hasattr(article1, "author") and hasattr(article1, "magazine") and hasattr(article1, "title"))
        
    
    def test_author_magazine_title_attributes_values_should_not_change(self):
        '''author, magazine and title attribute values should not be changed'''
        try:
            article1.author = author1
            article1.magazine = magazine2
            article1.title = "Some Name"
        except:
            pass
        
        assert(article1.author == author3 and \
            article1.magazine == magazine1 and \
            article1.title == "Introduction to python")
        
    def test_article_title_all_returns_correct_value(self):
        '''title attributes and all method return correct values'''
        assert(article3.title == "Active Records" and all_articles == Article.all())
        
    def test_artile_instance_author_and_magazine_returns_correct_values(self):
        '''article instance attributes(author and magazine) return correnct values'''
        assert(article2.author == author3 and article2.magazine == magazine2)
        
