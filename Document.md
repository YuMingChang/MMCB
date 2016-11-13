# MaMaCrazyBuy (Django1.10)

記載網頁製作所遇到個一些問題，以方便未來他人或自己查閱。


## Settings.py
每個Django專案中都會有的**setting.py**。

### INSTALLED_APPS
內建原有的** INSTALLED_APPS**，用於存放所有於網頁製作所需要的APPS，有些原生、有些來自開發人員新增還有些屬於第三方皆放於此。因此為了方便查閱得以分成以下三個List。
	
	INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

### Static files

	
## Models.py

* [ugettext() vs. ugettext_lazy()](http://stackoverflow.com/questions/4160770/when-should-i-use-ugettext-lazy)
* [ForeignKey、ManyToManyField、OneToOneField](http://www.cnblogs.com/linxiyue/p/3667418.html)
* [The value of 'list_display' must not be a many-to-many field.](http://stackoverflow.com/questions/18108521/many-to-many-in-list-display-django)
* [Multiple Images In Django](http://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django)

## Views.py

* [request.POST or None](http://stackoverflow.com/questions/35891598/handling-post-data-in-django-forms)
* [Django: catch all errors and display the type of error and message](http://stackoverflow.com/questions/7791261/django-catch-all-errors-and-display-the-type-of-error-and-message)

## Template Tag
Django 在 django.template 子模組中實作了一個 recursive descent parser。當你的 template 被讀入時，會經過這個 parser 處理成 AST，接著一個 renderer 負責將這個 AST 輸出成字串。[Github](https://github.com/uranusjr/django-tutorial-for-programmers/blob/master/29-template-tags-explained.md)

### Block
Defines a block that can be overridden by child templates. See [Template inheritance](https://docs.djangoproject.com/en/1.9/ref/templates/language/#template-inheritance) for more information.

####base template setup

	<html>
	<head>
	
	{% block js-head %} Tags that need to go up top  {% endblock js-head %}
	
	</head>
	<body>
	{% block header %}  Header {% endblock header %}
	
	{% block body %} Body goes here {% endblock body %}
	
	{% block footer %}  Footer {% endblock footer %}
	
	{% block js-foot %}  All other javascript goes here {% endblock js-foot %}
	</body>
	</html>
	
`Reference:` [Base TemplateTag Block Setup](http://stackoverflow.com/questions/4101458/how-to-put-javascript-at-the-bottom-of-django-pages-when-using-templatetags)



### For Loop
	
	{% for i in "0123456789" %}
		Do something
	{% endfor %}

`Reference:` [Numeric ForLoop In Django Templates](http://stackoverflow.com/questions/1107737/numeric-for-loop-in-django-templates)

### include


### dict

* [How to Access dict elements in templates](http://stackoverflow.com/questions/1275735/how-to-access-dictionary-element-in-django-template)

## JavaScript
### getElement
[how to get value of text input field?](http://stackoverflow.com/questions/11563638/javascript-how-to-get-value-of-text-input-field)

### Window Location
The window.location object can be used to get the current page address (URL) and to redirect the browser to a new page.

`Reference:`[w3schools Window Location](http://www.w3schools.com/js/js_window_location.asp)

### Django TemplateTag Variables in JS
The {{variable}} is substituted directly into the HTML. Do a view source; it isn't a "variable" or anything like it. It's just rendered text.

Having said that, you can put this kind of substitution into your JavaScript.

	<script type="text/javascript"> 
	   var a = "{{someDjangoVariable}}";
	</script>

[Django Template Variables and Javascript](http://stackoverflow.com/questions/298772/django-template-variables-and-javascript)

### 'yes and no' alert
> You’re probably looking for [JS confirm()](http://stackoverflow.com/questions/9334636/javascript-yes-no-alert), which displays a prompt and returns true or false based on what the user decided:
	
	if (confirm('Are you sure you want to save this thing into the database?')) {
	    // Save it!
	} else {
	    // Do nothing!
	}


## jQuery
jQuery 是一套物件導向式簡潔輕量級的 **JavaScript Library**。透過 jQuery 你可以用最精簡少量的程式碼來輕鬆達到跨瀏覽器 DOM 操作、事件處理、設計頁面元素動態效果、AJAX 互動等。

jQuery is a fast and concise **JavaScript Library** that simplifies HTML document traversing, event handling, animating, and Ajax interactions for rapid web development. jQuery is designed to change the way that you write JavaScript.

* [How To Show And Hide Input Fields Based On Radio Button Selection](http://stackoverflow.com/questions/17621515/how-to-show-and-hide-input-fields-based-on-radio-button-selection)
* [How do I get values of input element with the same name as an javascript array?](http://stackoverflow.com/questions/7157632/how-do-i-get-values-of-input-element-with-the-same-name-as-an-javascript-array)
* [How can I know which radio button is selected via jQuery?](http://stackoverflow.com/questions/596351/how-can-i-know-which-radio-button-is-selected-via-jquery)

### MutipleEvnet
	$('.ui .item').on({
        mouseenter: function() {
            $(this).removeClass('active');
            $(this).addClass('active');
        },
        mouseleave: function() {
            $(this).removeClass('active');
        }
    });
    
`Reference:` [MuitiEvent Handlers To One Selector](http://stackoverflow.com/questions/8608145/jquery-on-method-with-multiple-event-handlers-to-one-selector)

### Sticky(Follow Scrolling UI）

## Third Party Library
### Allauth
Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

[Django-allauth Facebook error](https://stackoverflow.com/questions/37876656/django-allauth-facebook-error)
[Create third party Facebook islogin in Django](https://www.youtube.com/watch?v=1yqKNQ3ogKQ)
[How to clean up Django login message from framework](http://stackoverflow.com/questions/25744425/how-to-clean-up-django-login-message-from-framework)

## Recommended Reading
### Python3 Learning
* [PythonTutorial](http://openhome.cc/Gossip/CodeData/PythonTutorial/)
* [Python3 Online Course(Github)](https://github.com/nguyen-toan/Python3)
* [Understanding Python Decorators in 12 Easy Steps!](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)

### WebDevelopment Learning
* [CSS Layout Learning](http://zh-tw.learnlayout.com/)
* [Js and Py3 Learning by 廖雪峰](http://www.liaoxuefeng.com/)
* [Django Tutorial](http://daikeren.github.io/django_tutorial/)
* [Django Girl Tutorials](https://djangogirlstaipei.herokuapp.com/tutorials/)
* [Try Django 1.9(Youtube)](https://www.youtube.com/watch?v=yfgsklK_yFo&index=1&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy)
* [Django Database Field Types](http://blog.csdn.net/pipisorry/article/details/45725953)

### WebDevelopment Concept
![http-decision-diagram](https://raw.githubusercontent.com/for-GET/http-decision-diagram/master/httpdd.png)

* [Logout: GET or POST?](http://stackoverflow.com/questions/3521290/logout-get-or-post)
* []()
* []()

### WebDevelopment Material
* [泡在網上的日子](http://www.jcodecraeer.com/)

### HTML
* [DOM 中 Property 和 Attribute 的区别](http://www.cnblogs.com/elcarim5efil/p/4698980.html)

### Python Tricks
* [Initializing Multiple Lists/Line](http://stackoverflow.com/questions/2402646/python-initializing-multiple-lists-line)
* []()

### Questions
* [What the difference between using Django redirect and HttpResponseRedirect?](http://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect)
* [request.POST.get('sth') vs request.POST['sth'] - difference?](http://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference)
* [Django - no such table exception](http://stackoverflow.com/questions/34548768/django-no-such-table-exception)
### BUG TAG
* when you reconstructed, **urlpatterns names** and **user's permission** need to care
* the space on the menu bar need to fixed.
* realize Bootstrap & SemanticUI **grid** difference.
* unification of the **argument name** in views and templates.
* please dont use button onclick redirect address, like (base.html):

	DONT Use:
	
		<button class="btn" onclick="window.location='{% provider_login_url "facebook" %}'; "> 結帳 </button></a>
		
	Use:
		
		<a class="item" href="{% url 'store' %}"><i class="gift icon"></i> 商店 </a>
		or
		<a href="{% url 'checkout:page' %}"><button class="btn btn-success btn-lg btn-block"> 結帳 </button></a>
		
* frontend form page need to interactive with user, plase return feedback like: **errors or messages**.

* member/models/field Name 'accounts' -> 'card_number' & 'sexual' -> 'gender' & ForeignKey -> OneToOneField
