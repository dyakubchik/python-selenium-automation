# Created by dmitr at 2/14/2021
Feature: Amazon Sign In Test
  # Enter feature description here

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click sign in from popup
    Then Verify Sigh in page opens
    # Enter steps here