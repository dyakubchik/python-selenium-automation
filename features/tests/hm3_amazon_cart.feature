# Created by dmitr at 2/9/2021
Feature: Amazon Cancel Order
  # Enter feature description here

  Scenario: User can check cart is empty
    Given Open Amazon page
    When Click on Amazon cart icon
    Then Verify Your Amazon Cart is empty are shown on the page

