from playwright.sync_api import Page, expect

# Tests for your routes go here
"""
When I call GET /spaces
I get a list of spaces back
"""
def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    name_element = page.locator(".t-space-name")
    expect(name_element).to_have_text(["Space1", "Space2", "Space3", "Space4", "Space5"])
    description_element = page.locator(".t-space-description")
    expect(description_element).to_have_text(["Example description 1", 
                                            "Example description 2", 
                                            "Example description 3", 
                                            "Example description 4", 
                                            "Example description 5"])
    price_element = page.locator(".t-space-price")
    expect(price_element).to_have_text(["£130.0" for _ in range(5)])

"""
When we create a new space
We see it in the spaces index
"""
def test_create_space(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text=List a space")
    page.fill("input[name='name']", "Test Name")
    page.fill("input[name='description']", "Test Description")
    page.fill("input[name='price']", "100")
    # When log in functionality is developed, must include test for correct user_id
    page.click("text=List my space")
    name_element = page.locator(".t-space-name")
    expect(name_element).to_have_text(["Space1", "Space2", "Space3", "Space4", "Space5", "Test Name"])
    description_element = page.locator(".t-space-description")
    expect(description_element).to_have_text(["Example description 1", 
                                            "Example description 2", 
                                            "Example description 3", 
                                            "Example description 4", 
                                            "Example description 5",
                                            "Test Description"])
    price_element = page.locator(".t-space-price")
    expect(price_element).to_have_text(["£130.0" for _ in range(5)] + ["£100.0"])
