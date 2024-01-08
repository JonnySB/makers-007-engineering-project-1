# Design Specification:

- Any signed-up user can list a new space.
- Users can list multiple spaces.
- Users should be able to name their space, provide a short description of the space, and a price per night.
- Users should be able to offer a range of dates where their space is available.
- Any signed-up user can request to hire any space for one night, and this should be approved by the user that owns that space.
- Nights for which a space has already been booked should not be available for users to book that space.
- Until a user has confirmed a booking request, that space can still be booked for that night.

# User Stories:

1.  As a user (host/ guest),
    So that I can sign up,
    I want to be able to enter my details and create a user account.

    Questions:
    - Do you want authentication/ login for any user using the web-app? No need for MVP. Keep simple.
    - What details are required for the sign up?
    - Do users sign up as guests/hosts respectively, or do they have the ability to do both?

2.  As a guest,
    So that I can view all available spaces,
    I want to see a list of all the spaces.

    Questions:
    - How would you like this list to be sorted?
    - What information should be displayed? Availability? Name, description, price, availability (extension: photo)
    - Can you then click on a space and view it in more detail? (user story 8) keep simple for MVP
    - Do users still want to see those spaces that are currently unavailable? yes, just can't book it

4.  As a host,
    So that I can list a space,
    I want to be able to add a space to the list.

    Questions:
    - Each listing has an owner? Maybe not for MVP but ideally for demo
    
5.  As a host,
    So that I can list multiple spaces,
    I want to be able to list multiple spaces.

    Questions:
    - How do you imagine you will be able to manage your listings?
    - What CRUD applications are required? Updating probably out of scope. Assess after MVP.

6.  As a host,
    So that I can provide details about a specific space,
    I want to be able to add a name, description and price.

    Questions:
    - 

7.  As a host,
    So that I provide availablity for my space,
    I want to be able to offer a range of dates of availablity.

    Questions:
    - Is this just a start and end date? yes for now. Dates join table 
    - Calendar package?

8.  As a guest,
    So that I can book a space,
    I want to be able to make a booking request for a specific space on a specific
    date.

    Questions:
    - Calendar with view of available/unavailable dates? Simplistic for MVP
    - More simplistic with error messages? 
    - Is this achievable from list view or must user be taken to details page?
    - Can a user only book one night at a time? Yes

9.  As a host,
    So that I rent a space to another user,
    I want to be able to confirm a booking request (as per user story 6)

    Questions:
    - How is the host expected to accept request? For MVP, perhaps booking is auto-confirmed 

10.  As a guest,
    So that I can hire a space,
    I want to be able to send my booking request to the space owner.

    Questions:
    - Is this a duplication of user story 8?
    

11.  As a host,
    So that I avoid booking clashes,
    I want to make my listing unavailable when a booking is confirmed.

    Questions:
    - How is the guest expected to know when their booking is confirmed? Confirmed/declined?



