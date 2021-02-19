# Created by dmitr at 1/24/2021
Feature: Amazon Search Test
  # Enter feature description here

  Scenario Outline: User can search for a Watches
    Given Open Amazon page
    When Input <search_query> into Amazon search field
    And Click on Amazon search icon
    Then Product results for <result> are shown on Amazon
    And Page URL has <search_query> in it

    Examples:
    |search_query|result   |
    |Watches     |"Watches"|
    |Dress       |"Dress"  |

  Scenario: User can search for a Dress
    Given Open Amazon page
    When Input Dress into Amazon search field
    And Click on Amazon search icon
    Then Product results for "Dress" are shown on Amazon
    And Page URL has Dress in it


  Scenario: User can add a product to the card
    Given Open Amazon page
    When Search for coffee mug
    And Click on the first product
    And Click on Add to card button
    Then Verify card has 1 item


  Scenario: User can add a product to the card
    Given Open Amazon page
    When Search for shoes
    And Click on the first product
    And Select shoes size
    And Click on Add to card button
    Then Verify card has 1 item