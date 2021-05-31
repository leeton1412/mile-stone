# Cake-Station - A Shop To Purchase Brownies and Cakes 


![Responsive Image](https://github.com/leeton1412/mile-stone/blob/master/documentaion/testing/images/screen1.png)

## Introduction

Cake-Station is a site desgin for gamers to purchase their dream cakes. Cakes will be themed all on games and movies.

It will land people on the products page showing all products. These can be filtered with an easy search. 
### Cakes
* Brownies
* Cakes
* All Cakes

### Games
* GTA
* Street Fighter
* Red Dead Redemption
* Crash Bandicoot

The selection sets what sort of cakes the user wants to display. Due to time restrictions not all are present 

Search bar can be used to find specific cakes

The main purpose of the web app is to allow people to quickly purchase gaming treats

The web app can be viewed on Desktop, Tablet and Mobile devices. Click [here]() to view.

## Table of Content

1. [UX](#ux)
    * [Goals](#goals)
        * [Cake-Station Goals](#cake-station-goals)
        * [Business goals](#business-goals)
        * [Customer goals](#customer-goals)
    * [User Stories](#user-stories)
        * [Gaming Session](#Gaming-Session)
    * [Design](#design)
        * [Colors](#colors)
        * [Font](#font)
    * [Wireframes](#wireframes)
2. [Features](#features)
    * [Existing Features](#existing-features)
        * [Features](#features)
    * [Features left to implement](#features-left-to-implement)
    * [Bugs and Fixes for Future Releases After Testing](#bugs-and-fixes-for-future-releases-after-testing)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
    * [Hosting on Heroku](#hosting-on-heroku)
6. [Credits](#credits)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)
        * [Pages used for information](#pages-used-for-information)
        * [I received advice and encouragement from](#i-received-advice-and-encouragement-from)

## UX

### Goals

#### Cake-Station Goals

The goal of this web app is to allow gamers to find their dream food. It aims for easy repeat use.

**Target audience is:**

* Gamers who are looking to plan a gaming night with friends.
* Gamers who are looking to compete in long time-scale activities 
* Gamers who are looking to compete competitivley 
* Any Person who is into gaming
* Any age group.
 

#### Business goals

* Create Repeat Business.
* Easy to use.
* Easy to purchase.


#### Customer goals

* Great food
* Quality Prices

Both business and customer goals are addressed through user stories.


### User Stories

#### Gamers

* As a Gamer, I want my web app to display products cleanly.
* As a Gamer, I want my web app to be simple to navigate.
* As a Gamer, I want my web app to be responsive on all devices.
* As a Gamer, I want my web app to be bug free and useable.
* As a Gamer, I want my web app to load quickly.
* As a Gamer, I want my web app to use as little of the users data as possible.
* As a Gamer, I want my web app to offer a quick purchase route.


### Design

#### Colors

Following colours have been used:
* ![#aba69b](https://placehold.it/15/aba69b/000000?text=+) #aba69b (Grey Shade) 
* ![#27272a](https://placehold.it/15/27272a/000000?text=+) #27272a (Very dark) 
* ![#141024](https://placehold.it/15/141024/000000?text=+) #141024 (Very dark) 
* ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) #ffffff (White) 
* ![#505050](https://placehold.it/15/#505050/000000?text=+) #505050 (Very Dark Grey)    
* ![#969696](https://placehold.it/15/#969696/000000?text=+) #969696 (Dark Grey)


#### Font

The Fonts I used for this project are **New Tegomin** and **Serif** with the font weights: 
* 400 - for all all elements.


### Wireframes

Wireframes can be found [here](documentation/wire-frames/wireframes.md)

## Features

### Existing Features

* **Layout and Style**
    * I wanted the web app to have an appearance that was associated with baking. Its designed with a darker tone to help appeal more to gamers at the same time. My aim was to provide users with quick access as the web app had loaded and eradicate anytime wasting, with the colour scheme and fonts used I believe I have been able to achieve this.
    * All forms generated using Crispy Form.
    * AllAuth used for quick and easy registration.
    * Toasts used to deliver messages to the user.

* **Navigation bar**
    * This provides the user with quick access to their shopping bag, search function and product selection
    * If a user is a super user they gain access to edit and delete items from the database to make the need for admin redundant.
    * The search function will pick up any favourites a customer may have and provide easy purchases. 

* **Footer**
    * Codepen Footer From Sherif Hamdy
    * Provides quick information about the company.
    * Social buttons that can be linked to the accounts.
    * Social media links - facebook, Twitter, Instagram.
    * A contact information area. Which can be built into a quick contact point
    * Access back to products page quickly.

* **Checkout Powered By Stripe**
    * A Checkout form which is easy to fill in and provides quick payment via Stripe.
    * Information save options to save it for a logged in user.
    * Toasts to display successfull purchases
    * Success page to show the order being completed.
    * Stripe elements used for easy styling 

* **Profile**
    * User profile that will display order history and delivery information.
    * Update information button that will update the users information.

* **Super User Access**
    * As mentioned above extra buttons to provide CRUD functionality for superusers.
    * Basic and easy to use buttons. 

* **Product Display**
    * Clicking on a product will load the product with more information
    * Provides the ability to add the product to the shopping basket.
    * Buttons to return to shopping or procceed to checkout. 

* **Shopping Bag View** 
    * Will allow users to update shopping bag.
    * Will Show customers how many items they are about to purchase.
    * Show Description of the product.

* **Product Model**
    * Products Desgined to store more information for further use
    * Categories to help sort the products.
    * Order Model to help track orders.


### Features left to implement

* **More Merchandise** - To enable potential customers to browse more gaming related products.
* **Email Contact** - To enable an email function for customers to easily get in touch.
* **Recipies** - To enable recipies for users who are subscribed to the site to gain accesss to recipies. This is stored in the product models.
* **Tracking User Behaviour** - Use an analytics tool such as [Hotjar](https://www.hotjar.com/) to view user behaviour.
* **Further Styling** - Site requires further styling to get desired feel.
* **Search functionality** - Better use of Categories to provide better search options once products grow in number.


### Bugs and Fixes for Future Releases After Testing

* **Nav bar mobile and bag on Mobile**
    * 2 main issues have arose after static files implemented. Nav Bar on mobile is no longer clean and responsive. Bag is no longer responsive. Due to time restrictions i will not be able to fix this

* **JavaScript**
    * Issue with Remove function on bag view. This can still be achieved via update bag. Due to time restrictions this has not been fixed.

* **Update information**
    * Update information is currently not updating. Due to time restrictions this has not been fixed

* **Email widget**
    * Email widget currently has been deactivated due to a bug. Due to time restrictions this has not been fixed but left in to help flow of website


## Technologies Used

### Languages

* HTML - base language for this project.
* CSS - used for styling the HTML code.
* JavaScript - used to make the web app interactive and activate certain functionality.
* Python3 - Used to interact and use Django Frameworks.

### Libraries

* [Bootstrap](https://getbootstrap.com/) - used for responsive grid system, styling, modals and Toasts.
* [JQuery](https://jquery.com/) & [Popper](https://popper.js.org/) - were used in conjunction with the Bootstrap library and Javascript.
* [FontAwseome](https://fontawesome.com/) - used for all icons on the site.
* [Google Fonts](https://fonts.google.com/) - used for the New Tegomin fonts.
* [Unsplash](https://unsplash.com/) - used for all images.
* [Bulma](https://bulma.io/) - used to help style content.
* [Django-Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - used to create a clean display for forms.
* [Stripe](https://stripe.com/gb) - used to create a quick and easy checkout process.

### Tools

* [Gitpod](https://www.gitpod.io) - used as IDE for this project.
* [Git](https://git-scm.com/) - used for version control.
* [Github](https://github.com/) - used to host repository and live website.
* [Balsamiq](https://balsamiq.com/) - used for creation of mockups.
* [Am I Responsive](http://ami.responsivedesign.is/) - used for testing purposes as well as creating the image to display the web pages on different devices.
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used for testing and debugging.
* [w3 html validator](https://validator.w3.org/) - used to test and validate my html code.
* [w3 css validator](https://jigsaw.w3.org/) - used to test and validate my css code.
* [Free Formatter](https://www.freeformatter.com/) - used to format my html, css and javascript code.
* [Browserstack](https://www.browserstack.com/) - used to test my site on different browsers.
* [Color Scheme Designer](http://colorschemedesigner.com/) - used to test colour combinations.
* [jshint](https://jshint.com/) - used to validate my Javascript code.


## Testing

Testing information can be found [here](documentation/testing/testing.md)

## Deployment

This web app was developed in Gitpod and pushed to the remote repository, GitHub.

**Used commands during deployment:**
* `git add .` - to add the files to the staging area.
* `git commit -m "text message here"` - to commit the files.
* `git push` - to push to origin master branch on to GitHub.
* `git status` - to see the current status of the files.

### Hosting on Heroku

* Log into Heroku.
* Click Create new app.
* Give it a name and select nearest region. Then click create app.
* Then on resource tab create postgres database. Then select free plan.
* Pip3 install dj-databse-url and psycopg2-binary to auto install apps on Heroku.
* Go to settings.py and import dj-database-url then set default database to be the Heroku var.
* Then run migrations with "python3 manage.py migrate".
* Set if statment in settings to use "DATABASE_URL".
* Install gunicorn and freeze requirements
* Create Procfile and create web Dyno
* Disbale static for your app once logged into Heroku
* Set allowed hosts in settings.py
* Commit changes and push to github and then heroku
* set heroku to be a repo with heroku git:remote -a cakestation
* Generate a secret key and set in heroku
* Set the secret key in settings.py to get it from the environment.
* Set up AWS account and use to host static.
* Create a bucket and store static files in there
* Enable Static Hosting.
* Create a user group.
* Create a policy.
* Create A user
* Download the cv3 file and save.
* Back in gitpod install boto3 and django-storages
* Add storages to installed apps.
* In settings set the correct bucket you want to connect to.
* Set your keys in heroku variables and set USE_AWS to true.
* Disable the collect static var.
* Git add and commit changes.
* The app can now be launched through its heroku web address.


### Media

**All Images & Audio**
   * All of the images used in the web app are free and do not require permission to use.



### Acknowledgements

#### Examples and Tutorials and Samples

* [Code Institute](https://codeinstitute.net/) - I used Boutique Ado as a guide on how to complete this project.

   

#### Pages used for information

* [W3schools](https://www.w3schools.com/)
* [W3C](https://www.w3.org/)
* [Stack overflow](https://stackoverflow.com/)
* [CSS-Tricks](https://css-tricks.com/)
* [MDN web docs](https://developer.mozilla.org/)
* [Codepen](https://codepen.io/)

#### I received advice and encouragement from
   * Tutor Support (CI online webchat)
   * Chantelle Turner (Partner)
   * Ian Westwood (Work Colleague)
   * Scott and Tim (Tutor Support)

## Disclaimer

**This web page was created for educational purposes only.** 











