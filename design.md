# Design Specification:

- Any signed-up user can list a new space.
- Users can list multiple spaces.
- Users should be able to name their space, provide a short description of the space, and a price per night.
- Users should be able to offer a range of dates where their space is available.
- Any signed-up user can request to hire any space for one night, and this should be approved by the user that owns that space.
- Nights for which a space has already been booked should not be available for users to book that space.
- Until a user has confirmed a booking request, that space can still be booked for that night.
- Any signed-up user can list a new space.

# User Stories:

1.  As a user (host/ guest),
    So that I can sign up,
    I want to be able to enter my details and create a user account.

2.  As a host,
    So that I can list a space,
    I want to be able to list a space

3.  As a host,
    So that I can list multiple spaces,
    I want to be able to list multiple spaces.

4.  As a host,
    So that I can provide details about a specific space,
    I want to be able to add a name, description and price.

5.  As a host,
    So that I provide availablity for my space,
    I want to be able to offer a range of dates of availablity.

6.  As a guest,
    So that I can book a space,
    I want to be able to make a booking request for a specific space on a specific
    date.

7.  As a host,
    So that I rent a space to another user,
    I want to be able to approve a specific request (as per user story 6)

8.  As a host,
    So that I can manage my bookings
    I want to be able to confirm my bookings.

9.  As a host,
    So that I avoid booking clashes,
    I want to make my listing unavailable when a booking is confirmed.

10. As a guest,
    When I look at listings
    I want to only see available listings.

Follow up questions:

- Does the client want proper authentication/ login for any user using the web-app.
- Do you want a view for the host and a view for the guests.
