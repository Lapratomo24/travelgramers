![TravelGramers logo](https://res.cloudinary.com/dbybmxt1u/image/upload/v1661624047/readme-logo_hlx5pd.png)

Welcome to TravelGramers!

Traveling is a wonderful experience. It is one of the best ways to forget the hustle and bustle of a stress-filled life in the city. Through travels, you can discover not only new places, but also new cultures, cuisines, and ways of life. You experience lots of new things by visiting places you have never been to, and you may create new bonds with people you have never met before. Each of this moment is a memory waiting to be told. 

TravelGramers is a blog created for one purpose: for travel enthusiasts to tell their tales. You can share your most unique and interesting travel stories with others. After creating your blog account, you will be able to create a blog post and share your travel experience. Oh, and don't forget to include your best photo!

The creation of this blog is intended to showcase a Full-Stack web application in a real-world context using an MVC framework and related technologies. Heroku is used to deploy the application on a webpage.

[Visit TravelGramers Blog](https://travelgramers-blog.herokuapp.com/)

## Table of Content

## Objective

TravelGramers is a travel blog that is targeted to a specific audience: those who share the love of travel, regardless of demographics. The blog displays a paginated list of blog posts belonging to various different users. Each post can be viewed and interacted with. Users can create an account to be able to create a new post on the blog. Logging in is not necessary to view the available posts on the blog, although logged-in users can click the like button on each post as well as leave comments to interact with one another. They will also be able to update their post(s) to add more information, or they can choose to delete them entirely should they feel like doing so.

## User Experience

### Agile Methodology

As part of the requirements to start this project, an Agile Methodology was used in order to draft and develop the site. This approach played an important part during the planning phase as I managed to break down the project into smaller tasks.

[Github Projects](https://github.com/users/Lapratomo24/projects/6/views/1) was used to set up a Kanban Board. Please see the attached screenshots below for the completed rundown of the phases.

<details><summary><b>Phase 1</b></summary>

![Agile](media/img/agile/agile_phase1.png)
</details><br />

<details><summary><b>Phase 2</b></summary>

![Agile](media/img/agile/agile_phase2.png)
</details><br />

<details><summary><b>Phase 3</b></summary>

![Agile](media/img/agile/agile_phase3.png)
</details><br />

<details><summary><b>Phase 4</b></summary>

![Agile](media/img/agile/agile_phase4.png)
</details><br />

<details><summary><b>Phase 5</b></summary>

![Agile](media/img/agile/agile_phase5.png)
</details><br />

There are 14 issues, or in other words, User Stories that were planned and documented as the project was being developed in order to achieve the desired result. These issues were then further classified as 4 main Epics as follows.

### User Stories

**Epic - Site Administration**
- As a site administrator, I would like to be able to create, read, update, and delete posts from the admin page so that I can manage the blog's content.

**Epic - Site Navigation**
- As a user, I would like to be able to immediately understand the purpose of the website so that I can use it to the full extent.
- As a user, I would like to be able to navigate through the pages of the site with ease so that I can keep track of where I am.
- As a user, I would like to be able to see a paginated list of posts so that I can select which post I would like to view.
- As a user, I would like to be able to view each post in detail so that I can read the post's content in detail.
- As a user, I would like to be able to see the number of likes on each post without having to view it in detail.
- As a user, I would like to be able to click the social media buttons so that I can interact with the creator of the site.
- As a user, I would like to be able to see each post's date and time of creation so that I can find out when the post was published.
- As a user, I would like to be able to see if an error occurs so that I can address it.
- As a user, I would like to be able to get a notification so that I can tell whether my registration, login, and logout attempts are successful.

**Epic - User Profile**
- As a user, I would like to be able to register a blog account so that I can have my own blog account.
- As a user, I would like to be able to log in so that I can fully interact with the site.
- As a user, I would like to be able to see my post-login status immediately so that can know my login is successful.
- As a user, I would like to be able to log out so that I can prevent another user from using my account.

**Epic - Post Management**
- As a user, I would like to be able to create a post so that I can share my travel experience on the site.
- As a user, I would like to be able to edit/update my own post(s) so that I can always add more information to it.
- As a user, I would like to be able to delete my own post(s) so that I can be fully in control as a post owner.
- As a user, I would like to be able to log in so that I would be able to edit/update or delete my post(s).
- As a user, I would like to be able to leave and remove a like so that I can interact with the posts belonging to other users.
- As a user, I would like to be able to leave a comment (or more) so that I can interact with the posts belonging to other users.

## Design

As stated previously, this blog website follows the same initial setup as the tutorial. The design of the homepage, as well as subsequent pages, may look similar to the finished website shown in the tutorial, albeit adjusted with my own design. 

### Data Model

Due to strict time constraints, I decided to develop a blog website which follows the same initial setup as Matt Rudge's Django Blog Tutorial, therefore there are only 2 data models: Post and Comment. And for the sake of simplicity, 2 things are adjusted: The status of a new post is automatically set to published, and comments made by users will also be automatically approved and displayed on the comment section. The database model is as follows:

![Database](media/img/database.png)

### Logo

I created the TravelGramers logo, seen at the top of this readme file, on [Canva](https://www.canva.com/), which has always been my go-to design tool for many years.

### Wireframes

Similary, Canva was also used to create the wireframes for TravelGramers. The following are the wireframes for each page on the finished website.

<details><summary><b>Homepage (not logged in)</b></summary>

![Wireframes](media/img/wireframes/wireframe_home1.png)
</details><br />

<details><summary><b>Homepage (logged in)</b></summary>

![Wireframes](media/img/wireframes/wireframe_home2.png)
</details><br />

<details><summary><b>Create Page</b></summary>

![Wireframes](media/img/wireframes/wireframe_create.png)
</details><br />

<details><summary><b>Post Detail Page (not logged in)</b></summary>

![Wireframes](media/img/wireframes/wireframe_post1.png)
</details><br />

<details><summary><b>Post Detail Page (logged in)</b></summary>

![Wireframes](media/img/wireframes/wireframe_post2.png)
</details><br />

<details><summary><b>Update Page</b></summary>

![Wireframes](media/img/wireframes/wireframe_update.png)
</details><br />

<details><summary><b>Delete Page</b></summary>

![Wireframes](media/img/wireframes/wireframe_delete.png)
</details><br />

<details><summary><b>About Page</b></summary>

![Wireframes](media/img/wireframes/wireframe_about.png)
</details><br />

<details><summary><b>Signup Page</b></summary>

![Wireframes](media/img/wireframes/wireframe_signup.png)
</details><br />

<details><summary><b>Login Page</b></summary>

![Wireframes](media/img/wireframes/wireframe_login.png)
</details><br />

<details><summary><b>Logout Page</b></summary>

![Wireframes](media/img/wireframes/wireframe_logout.png)
</details><br />

### Color Scheme

The color scheme was derived from [mycolor.space](https://mycolor.space/). I use a predominantly white ash color for the background of the body as well as the navigation bar, blue-ish green for the post tile, buttons, and page headers, as well as blue for the footer.

![Color](media/img/colors.png)

### Font Style

The main font families used for the design of this project are [Poppins](https://fonts.google.com/specimen/Poppins?query=poppin) and [Abril Fatface](https://fonts.google.com/specimen/Abril+Fatface?query=abril) from Google Fonts.

### Images

All of the images displayed on the posts, as well as the hero image, belong to me. I am a travel enthusiast myself, hence why I decided to create this travel blog website. I fully guarantee that you will not find the exact same images online.

## Structure and Features

TravelGramers consists of multiple pages, albeit the structure is quite simple to navigate. Every page is described in detail below which includes the available features.

### Homepage

The homepage is where users will find a paginated list of blog posts. The posts are preceded by a navigation bar at the top of the screen and followed by a footer section down at the bottom, both of which are visible across all pages.

- The navigation bar consists of a TravelGramers logo on the left and 4 navigation items on the right which include home, about, log in, and sign up. The latter 2 are replaced by create and log out whenever a user logs in with their account. Between the navigation bar and the posts, a hero image is displayed, on top of which a big TravelGramers logo can be seen. 

<details><summary><b>Navbar and Hero Image</b></summary>

![Features](media/img/features/homepage1.png)
</details><br />

- Just below the hero image, a tagline that says "Share your unique travel experience" invites users to create a post on the blog. Once logged in, users will see a 'tell your story' button underneath the tagline which redirects to the create page. The first set of 3 posts then follows.

<details><summary><b>Tagline and 1st Set of Posts</b></summary>

![Features](media/img/features/homepage2.png)
</details><br />

- Below the second set of 3 posts is a next button which indicates that the page is paginated by 6 posts per page.

<details><summary><b>2nd Set of Post and Next Button</b></summary>

![Features](media/img/features/homepage3.png)
</details><br />

- The footer includes a copyright text and 2 social media icons which when clicked will redirect users to the blog author's Instagram and LinkedIn pages, respectively.

<details><summary><b>Footer</b></summary>

![Features](media/img/features/homepage4.png)
</details><br />








**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
