# Engineering Project I (Makersbnb)

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/engineering_projects/makersbnb/HOW_TO_COACH.x.md)_

This week you will:

* Learn to work and communicate effectively as part of a team to build a web
  application.
* Learn to break down projects into tasks and assign them to pairs.
* Learn to use agile ceremonies to organise your work and improve your
  processes.
* Learn to use the developer workflow to plan, implement and peer-review
  features.

<!-- OMITTED -->

## Introduction

Your coach will share the teams with you this morning. Once you have them,
create a private slack channel with all team members and invite your coach to
that channel.

Get together on a Zoom call (or gather in front of the same screen) and watch
[this introduction video.](https://www.youtube.com/watch?v=eHHY9EYZtUE)

<!-- OMITTED -->

## Project Setup

1. Create a private slack channel with all team members and invite the coach
   leading this week to that channel.
2. One member in your group [should fork the seed repo for this
   project](https://github.com/makersacademy/makersbnb-ruby-seed), and add the
   other members of your group as collaborators. Everyone will pull and push to
   this fork.
3. Add a link to this repo to the description of your team's slack channel.
4. [Read the project specification together](./specification.md)
5. Decide how you will work, by creating a small team charter — [here's a
   template you can
   use](https://docs.google.com/document/d/1JbXksrTlu_-kCvq-ITzLucvFvv3QOFN9P_LsTRfQ3kM/edit).
6. Create a Trello board for your project, [using this
   template.](https://trello.com/b/g9JBypiG)
7. Start turning the headline specifications into user stories and create one
   Trello ticket in the column "Backlog (all TODO)". 
8. Get a break, and then start [your first
   sprint](#agile-sprints-and-ceremonies).

## Agile Sprints and Ceremonies

Agile software teams work in sprints. At the beginning of a new sprint, the team
decides which features to work on in that sprint, and what to leave for later.
This week, you will work with shorter sprints of roughly two days. Here is a
suggested schedule:
  * Monday to Tuesday - Sprint #1
  * Wednesday to Thursday - Sprint #2
  * Friday - Sprint #3
  * [Stand-up every morning](./pills/how_to_run_standup.md) (15 min) after your peer groups check-ins.
    * This should ideally last no more than 15 minutes.
    * Everyone shares what they've worked on the previous day, what they'll work
      on today, and any blockers that need the attention of the team.
  * [Retro at the end of both sprints](./pills/how_to_run_retro.md)
      * Use these retros to reflect on your work as team, and bring up any
        issues. This is not a session to discuss technical details or review
        code, but rather think of _how_ the team worked so far, and what could
        be improved.

<!-- OMITTED -->

To start your first sprint:
  1. Get together as a team.
  2. Pick a few tickets from the tickets backlog, and move them to the "Current
     sprint" column — remember your goal is to get them done within this first
     sprint, so it's better to start with less initially. For this first sprint,
     pick tickets [relevant to the MVP of your project
     only](#minimum-viable-product-mvp). You can always extend the sprint with
     more tickets, if you find you're working faster than expected.
  3. Assign the first tickets to pairs.
  4. Get into your pairs, [watch this
     video](https://www.youtube.com/watch?v=DDInr8vDQs0) and draw a diagram of the key stages of a developer workflow together.
  5. Start planning your MVP (Minimum Viable Product)!

<!-- OMITTED -->

## Developer Workflow

[Watch this video with your pair _before_ starting to work your first
ticket.](https://www.youtube.com/watch?v=DDInr8vDQs0)

[A written description of the workflow is also available
here](./pills/developer_workflow.md)

## Minimum viable product (MVP)

The smallest thing that implements the core idea. Think about what this is for
Airbnb. Build those user stories first. This MVP will not include many of the most
exciting features in the specification.

If your specification asks for a car, don't build the wheels in the first week,
the doors in the second week, etc. The customer can't try it! Instead, build a
skateboard in the first week. 

The MVP allows for an 'iterative' development of the project. That means that you try out a
basic version of your project, get feedback on it, then use that feedback to improve the product
or build new features. This ensures that what you are writing is very valuable to customers.

Aim to get to your MVP by the *end of Tuesday* - this is the 'skateboard' of your project.

## Breaking down user stories into tasks

Make sure each user story is small enough to be completable in less than half a
day.

Some items in the spec include more than one feature. e.g. "Any signed up user
can list a new space". Break this into two user stories and prioritise the one
that gets you as close as possible to a product.

Use the customer's language (the domain language) in the user stories. Most
words in the user stories should appear in the spec.

Avoid splitting the work on the different "layers" of the program (e.g one pair
working on the HTML view and one pair working on the Sinatra code). When working
on a user story, you will have to work on all these different components — [a
feature will involve work on all the different layers of your web
application.](https://www.visual-paradigm.com/scrum/user-story-splitting-vertical-slice-vs-horizontal-slice/#:~:text=layers%20as%20possible.-,Vertical%20Slice%20vs%20Horizontal%20Slice,-A%20user%20story)

### Creating tickets from your tasks

A *clear title*, that includes a specific succinct description of the technical
aspects of the ticket e.g. not "Make a homepage", but more like "Build a
navigation bar".

Include the *user story* as a starting point. This will bring focus to what the
task is, and ensure that you have clarity of the end goal of the technical task
i.e. the user's needs.

*Acceptance criteria* is useful to answer some key questions to you should have
at the beginning - what will tell you that this feature is definitely completed?
For example, with our navigation bar, is it that it allows us to navigate to the
right pages, or is that it has the correct styling with agreed theme colours?

*Testing* this is part of acceptance criteria but deserves its own category. It
can make a world of difference to think about what kind of tests you want to
include as part of a particular feature, and will again bring your focus from
the beginning to TDD.

*Documentation / Links* and any other additional information that will help the
developer working on the ticket complete the task e.g. a great tutorial, a
template for a navigation bar, the file path for useful code to complete this
ticket.

## Things to watch out for

* **Working overtime** — make sure your take breaks and swap pairs regularly.
  It's easy to get lost in the work and stretch yourself, but remember that this
  week's goal is also to learn how to work effectively. A team that is exhausted
  is not a great team to work in!
* **Your body's health** - Make sure you're not sitting on the computer all day!
  As a general rule, make sure you take a break and walk around every 45 mins to an hour, 
  and to give your eyes regular breaks from the screen. It can be useful to have a little 
  non-screen activity to bring your focus to in your breaks.
* **Rushing to get things done** - releasing features is important, but you
  shouldn't sacrifice your process in order to rush ahead. It's often better to
  start slow, and invest more time into deep learning and having strong
  processes and communication, so it pays off on the long run.
* **Sidelining testing** - more than ever, TDD and other software engineering
  practices you've learned so far will be important this week. Make sure that
  you don't skip over them. They will slow you down a bit at first, but it will
  pay off on the long run. If you din't they're slowing you down _too much_,
  maybe there is something to correct in your process — your coach can support
  with this.
* **Everyone's voice isn't heard** - it's important that everyone in the team
  gets their say on the project and how the team works, and that everyone feels
  like they can contribute, even if you're at different technical levels. If you
  feel that something isn't quite right, stand-ups or retros are a good place to
  raise it, in order to get the team to a better place. If you're not sure how
  to approach it, get in touch with your coach so they can support.

## Web Development Tools and Guidance

[The guidance from the web applications
materials](https://github.com/makersacademy/web-applications#going-further) can
be helpful to implement common patterns, such as user sign up and login, or
loading static files (CSS, images, etc.). 

This week you might find it useful to expand your web development tool kit -
[this pill includes some helpful resources for building user-friendly
applications](https://github.com/makersacademy/course/blob/main/pills/web_development_tools.md).

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/engineering-project-1&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/engineering-project-1&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/engineering-project-1&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/engineering-project-1&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/engineering-project-1&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fengineering-project-1&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fengineering-project-1&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fengineering-project-1&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fengineering-project-1&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fengineering-project-1&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
