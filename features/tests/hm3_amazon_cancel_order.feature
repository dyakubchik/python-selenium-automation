# Created by dmitr at 2/9/2021
Feature: Amazon Cancel Order
  # Enter feature description here

  Scenario Outline: User can cancel an order
    Given Open Amazon cancel order page
    When Input <search_query> into help library search field
    Then Search results for <result> are shown on help page

    Examples:
    |search_query|result   |
    |Cancel Order|Cancel Items or Orders|
