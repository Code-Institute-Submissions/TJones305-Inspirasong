# Inspirasong

####  A link to the live site is here: [Inspirasong](https://inspirasong.herokuapp.com/) 

 **This is a social media type website enabling people to share their musical inspirations.** 
 **Users are able to create, read, update and delete thier own posts**

## User Experience (UX) User stories

### First Time Visitor Goals 
- As a First Time Visitor, I want to easily understand the main purpose of the site. 
- As a First Time Visitor, I want to be able to easily navigate throughout the site. 
- As a First Time Visitor, I want the page visually appealing.

### Returning Visitor Goals 
- As a Returning Visitor, I want to read other user posts. 
- As a Returning Visitor, I want to have control of my posts.

## Design 

### **Colour Scheme** 
The main colour used for the site was purple, the developer felt that this was a neutral colour that wouldn't evoke bias to masculine or feminine feel. Text colour is predominantly varying shades of purple, and white where a dark purple background has been used. 

### **Typography** 
Seven font styles were used on the site, courtesy of Google Fonts, the most predominant style was Play with the fallback of sans-serif and the other styles used on headings and buttons to theme the genre pages had fallback of cursive.
Other fonts used were Zen Tokyo Zoo (Inspirasong title found throughout site), Metal Mania(to theme rock buttons and post page), Bangers (to theme pop buttons and post page), Zen Dots (to theme dance buttons and post page), Staatliches (to theme rap buttons and post page)and Bebas Neue (to theme other buttons and post page)

### **Imagery** 
The developer wanted to integrate a sense of musical fun and added hero images for each genre page that had a feel for that genre.
Rock has a poster with various rock bands on it, Pop a man jammin' to his music through headphones, Rap a mid mic-drop, Dance a set of decks, and other a world surrounded by musical notes. 

### **Wireframes** 

1. Desktop

![Wireframe Desktop](/README_images/wireframe-inspirasong-website.pdf "Wireframe Desktop")

2. Tablet

![Wireframe Tablet](/README_images/wireframe-inspirasong-tablet.pdf "Wireframe Tablet")

3. Mobile

![Wireframe Mobile](/README_images/wireframe-inspirasong-mobile.pdf "Wireframe Mobile")

### **Features**
- Responsive on most devices sizes
- Interactive elements (Burger menu (mobile devices only), sidenav, dropdown boxes on post creation, date pickers, collapsible on user profile, modal used to confirm post deletion, registarion and login)

> ## Technologies Used 

### **Languages Used** 
HTML5 
CSS3
JavaScript3
Python3

### **Frameworks, Libraries & Programs Used** 

- Materialize 1.0: Materialize was used to assist with the responsiveness and styling of the website. Specific features include - navbars, burger menu, date picker, modal, collapsible. 
 
- Google Fonts: Google fonts was used to import the seven fonts on the site into the style.css file. 

- Font Awesome: Font Awesome was used on forms and buttons to add icons for aesthetic and UX purposes. 

- jQuery: jQuery came with Materialize to make the navbar responsive, along with the other features taken from Materialize. 
 
- Git: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

- GitHub: GitHub is used to store the projects code after being pushed from Git. 

- Balsamiq: Balsamiq was used to produce wireframes during the design process.

- Heroku: Heroku was use as the platform to deploy the app.

- Mongo DB: Mongo DB was used to store the colections of the app.

-Jinja: Jinja templating was used extensively throughout the site.

> ## Testing 
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

### **W3C Markup Validator**

![Markup Validator Report](/README_images/markup-validator.jpg "Markup Validator")
    The Markup Validator highlighted 2 errors. 1 related to href attribute on h4, this was to apply Jinja on the brand logo so when 
    clicked it took the user to the home page, however the developer has now removed this href. the other error relates to a div being a child of a ul.
    The div was placed as such to enable the hero image to load onto the side nav, without it the sidebar was solid black. The developer has decided to
    remove the image, despite it adding a professional touch. 

### **W3C CSS Validator**  

![CSS Validator Report](/README_images/css-validator.jpg "CSS Validator")
	The result of the CSS validator highlighted 3 errors. One error is part of Materialize's CDN. The other Two relate to the rainbow 
    colour scheme created for the main title. The developer feels that this is a justified error to create a wow effect for the user. 

### **Lighthouse** 
![Lighthouse Report Desktop](/README_images/lighthouse-desktop.jpg "Lighthouse Report Desktop")
![Lighthouse Report Mobile](/README_images/lighthouse-mobile.jpg "Lighthouse Report Mobile")


> ## Testing User Stories from User Experience (UX) Section

##  *First Time Visitor Goals*  
- As a First Time Visitor, I want to easily understand the main purpose of the page.  

Upon arriving at the site the base page immediately gives the user an clear overview of the expected content.

![Base Page](/README_images/home_page.jpg "Base Page")

The genre buttons at the bottom of the page give further depth into what can be expected from the content of the site.

![Genre Buttons](/README_images/genre_buttons.jpg "Genre Buttons")

- As a First Time Visitor, I want to be able to easily navigate throughout the site.  

The user can easily navigate through the page wherever they are on the page. 
At the top of the page the user has the option to jump to the main pages and at the bottom of each page are the button links to each genre.

![Navbar](/README_images//navbar.jpg "Navbar")

Once registered a user can simpply login in, but should they wander the the registration page by mistake, there is a link to login
both on the navbar and at the bottom of the registration page.

![Registration page](/README_images//register.jpg"Registration page")

- As a First Time Visitor, I want the page visually appealing.

The user is greeted by bright colours when arriving on the page, which creates a welcoming and postive feeling.
The themed fonts add to the occasion by creating a fun look that is aligned with their genre.

![Base Page](/README_images/home_page.jpg "Base Page")

### *Returning Visitor* 

- As a Returning Visitor, I want to read other user posts. 

Each genre displays only the posts that have a corresponding genre e.g. dance displays posts with the genre of dance.
On these pages all posts of that genre are displayed, showing the credentials of their creator (username) and date of creation.

![Dance Page](/README_images/genre_page.jpg "Dance Page")

- As a Returning Visitor, I want to have control of my posts. 

From the picture above you can see that each post a user creates will be managable by way of either editing the post or deleting it.


## **Further Testing** 
- The Website was tested on Google Chrome, Opera, Microsoft Edge and Safari browsers. 
- The website was viewed on a variety of devices such as Desktop, Laptop, iPad Air & iPhoneX. Other devices were tested through the inspect web developer tools.

##  **Known Bugs** 
- Modal on small width devices
The delete modal doesn't seem to appear on the different genre pages when clicked, despite working as required on the profile page. This seems to affect small mobile screens (280-340px).

> ## Deployment 

### **Heroku**  
The project was deployed to Heroku using the following steps...

1. Before you can deploy your app to Heroku, you need to initialize a local Git repository and commit your application code to it.
2. The heroku create CLI command creates a new empty application on Heroku, along with an associated empty Git repository. If you run this command from your app’s root directory, the empty Heroku Git repository is automatically set as a remote for your local repository.
3. You can use the git remote command to confirm that a remote named heroku has been set for your app
4. To deploy your app to Heroku, you typically use the git push command to push the code from your local repository’s master or main branch to your heroku remote
5. Use this same command whenever you want to deploy the latest committed version of your code to Heroku.
6. Note that Heroku only deploys code that you push to master or main. Pushing code to another branch of the heroku remote has no effect. 

### **Forking the GitHub Repository** 
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository 
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### **Making a Local Clone**  
1. Log in to GitHub and locate the GitHub Repository Under the repository name, click "Clone or download". 
2. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link. 
3. Open Git Bash Change the current working directory to the location where you want the cloned directory to be made. 
4. Type git clone, and then paste the URL you copied in Step 3. $ git clone https://github.com//TJones305/Inspirasong Press Enter. 
5. Your local clone will be created. $ git clone https://github.com//TJones305/Inspirasong

> ### *Credits*  

- Materialize: Bootstrap Library used throughout the project to make site responsive using the Bootstrap Grid System. Also for the navbar and accordion base code.

- MDN Web Docs: For Pattern Validation code. Code was modified to better fit my needs.

- Google Fonts: For use of their brilliant Fonts

- Font Awesome: For use of their icons.

- Content: All content was written by the developer.


> ## Acknowledgements 
- My Mentor Gerry McBride for constructive feedback and continuous.

- Student support at Code Institute for their helpful advice and guidance.