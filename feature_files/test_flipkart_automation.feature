Feature: Automation Test for flipkart



  Scenario: Verify Add to cart flow
	  Given I select English Language
	  When I search products
	  Then I select a product
	  Then I verify product added to cart
