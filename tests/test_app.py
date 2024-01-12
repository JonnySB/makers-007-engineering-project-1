from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository
from lib.user import User
import pytest

"""
When I call GET /spaces
I get a list of spaces back
"""


def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    name_element = page.locator(".t-space-name")
    expect(name_element).to_have_text(
        ["Space1", "Space2", "Space3", "Space4", "Space5"]
    )
    description_element = page.locator(".t-space-description")
    expect(description_element).to_have_text(
        [
            "Example description 1",
            "Example description 2",
            "Example description 3",
            "Example description 4",
            "Example description 5",
        ]
    )
    price_element = page.locator(".t-space-price")
    expect(price_element).to_have_text(["£130.00/ night" for _ in range(5)])


"""
When we click on space 3's details
We see the info for that space including a list of booking dates
And can book a certain date
"""


def test_details_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    page.click("a[href='/spaces/3']")
    name_element = page.locator(".t-space-name")
    expect(name_element).to_have_text("Space3")
    description_element = page.locator(".t-space-description")
    expect(description_element).to_have_text("Example description 3")
    price_element = page.locator(".t-space-price")
    expect(price_element).to_have_text("£130.00/ night")
    date_element = page.locator(".t-space-date")
    expect(date_element).to_have_text(["2024-05-10", "2024-05-11", "2024-05-12"])
    availability_element = page.locator(".t-space-availability")
    expect(availability_element).to_have_text(["Available", "Available", "Available"])
    page.click("a[href='/spaces/rent/8/3']")
    expect(availability_element).to_have_text(["Available", "Unavailable", "Available"])


"""
When we create a new space
We see it in the /spaces index
And can see the dates listed on the details page
"""


# @pytest.mark.skip()
def test_create_space(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces/new")
    # page.click("text=List a space")
    page.fill("input[name='name']", "Test Name")
    page.fill("input[name='description']", "Test Description")
    page.fill("input[name='price']", "100")
    page.fill("input[name='available_from']", "2024-03-26")
    page.fill("input[name='available_to']", "2024-03-29")
    page.click("button[type='submit']")
    name_element = page.locator(".t-space-name")
    expect(name_element).to_have_text(
        ["Space1", "Space2", "Space3", "Space4", "Space5", "Test Name"]
    )
    description_element = page.locator(".t-space-description")
    expect(description_element).to_have_text(
        [
            "Example description 1",
            "Example description 2",
            "Example description 3",
            "Example description 4",
            "Example description 5",
            "Test Description",
        ]
    )
    price_element = page.locator(".t-space-price")
    expect(price_element).to_have_text(
        ["£130.00/ night" for _ in range(5)] + ["£100.00/ night"]
    )
    page.click("a[href='/spaces/6']")
    date_element = page.locator(".t-space-date")
    expect(date_element).to_have_text(
        ["2024-03-26", "2024-03-27", "2024-03-28", "2024-03-29"]
    )


"""
When we create a user
We see it in the users table
"""


def test_create_user(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/signup")

    page.fill("input[name=username]", "user6")
    page.fill("input[name=email]", "user6@user.com")
    page.fill("input[name=password]", "Password")
    page.fill("input[name=confirm_password]", "Password")

    page.click("text='Sign Up'")

    repository = UserRepository(db_connection)

    users = repository.all()
    assert users == [
        User(1, "user1", "user1@user.com", "Password"),
        User(2, "user2", "user2@user.com", "Password"),
        User(3, "user3", "user3@user.com", "Password"),
        User(4, "user4", "user4@user.com", "Password"),
        User(5, "user5", "user5@user.com", "Password"),
        User(6, "user6", "user6@user.com", "Password"),
    ]
