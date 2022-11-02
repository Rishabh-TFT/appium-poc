Feature: Automation Test for flipkart



  Scenario: Verify search functionality
		When I open flipkart and search for a device
		Then I select device and click on add to cart option
		Then I go to my my cart and verify the added device